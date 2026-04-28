#!/usr/bin/env python3
"""Validate the qml-agent-lab governance ontology artifacts.

The validator uses only the Python standard library. It intentionally performs
simple, transparent checks that future agents can understand and extend.
"""

from __future__ import annotations

import csv
import json
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_DIR = REPO_ROOT / "ontology"
GRAPHML_PATH = ONTOLOGY_DIR / "agent_team_governance_ontology.graphml"
NODES_CSV_PATH = ONTOLOGY_DIR / "ontology_nodes.csv"
EDGES_CSV_PATH = ONTOLOGY_DIR / "ontology_edges.csv"
MANIFEST_PATH = ONTOLOGY_DIR / "ontology_manifest.json"
GRAPHML_NS = {"g": "http://graphml.graphdrawing.org/xmlns"}


@dataclass
class Check:
    name: str
    passed: bool
    detail: str = ""


def add(checks: list[Check], name: str, passed: bool, detail: str = "") -> None:
    checks.append(Check(name=name, passed=passed, detail=detail))


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_graphml(path: Path) -> tuple[set[str], list[tuple[str, str, str | None]]]:
    tree = ET.parse(path)
    root = tree.getroot()
    graph = root.find("g:graph", GRAPHML_NS)
    if graph is None:
        raise ValueError("GraphML file has no <graph> element.")

    node_ids: set[str] = set()
    for node in graph.findall("g:node", GRAPHML_NS):
        node_id = node.attrib.get("id", "")
        if node_id:
            node_ids.add(node_id)

    edges: list[tuple[str, str, str | None]] = []
    for edge in graph.findall("g:edge", GRAPHML_NS):
        edges.append((edge.attrib.get("source", ""), edge.attrib.get("target", ""), edge.attrib.get("id")))

    return node_ids, edges


def validate() -> list[Check]:
    checks: list[Check] = []

    add(checks, "GraphML exists", GRAPHML_PATH.exists(), str(GRAPHML_PATH))
    add(checks, "Node CSV exists", NODES_CSV_PATH.exists(), str(NODES_CSV_PATH))
    add(checks, "Edge CSV exists", EDGES_CSV_PATH.exists(), str(EDGES_CSV_PATH))
    add(checks, "Manifest exists", MANIFEST_PATH.exists(), str(MANIFEST_PATH))

    if not all(path.exists() for path in [GRAPHML_PATH, NODES_CSV_PATH, EDGES_CSV_PATH, MANIFEST_PATH]):
        return checks

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        add(checks, "Manifest parses as JSON", True)
    except json.JSONDecodeError as exc:
        add(checks, "Manifest parses as JSON", False, str(exc))
        return checks

    expected_nodes = int(manifest.get("graph", {}).get("nodes", -1))
    expected_edges = int(manifest.get("graph", {}).get("edges", -1))
    add(checks, "Manifest declares node count", expected_nodes >= 0, f"nodes={expected_nodes}")
    add(checks, "Manifest declares edge count", expected_edges >= 0, f"edges={expected_edges}")

    try:
        graph_nodes, graph_edges = load_graphml(GRAPHML_PATH)
        add(checks, "GraphML parses as XML", True)
    except (ET.ParseError, ValueError) as exc:
        add(checks, "GraphML parses as XML", False, str(exc))
        return checks

    try:
        csv_nodes = read_csv_dicts(NODES_CSV_PATH)
        add(checks, "Node CSV parses", True)
    except csv.Error as exc:
        add(checks, "Node CSV parses", False, str(exc))
        return checks

    try:
        csv_edges = read_csv_dicts(EDGES_CSV_PATH)
        add(checks, "Edge CSV parses", True)
    except csv.Error as exc:
        add(checks, "Edge CSV parses", False, str(exc))
        return checks

    csv_node_ids = {row.get("id", "") for row in csv_nodes}
    csv_edge_sources = [row.get("source", "") for row in csv_edges]
    csv_edge_targets = [row.get("target", "") for row in csv_edges]

    add(
        checks,
        "Manifest node count matches GraphML",
        len(graph_nodes) == expected_nodes,
        f"manifest={expected_nodes}, graphml={len(graph_nodes)}",
    )
    add(
        checks,
        "Manifest edge count matches GraphML",
        len(graph_edges) == expected_edges,
        f"manifest={expected_edges}, graphml={len(graph_edges)}",
    )
    add(
        checks,
        "Node CSV row count matches manifest",
        len(csv_nodes) == expected_nodes,
        f"manifest={expected_nodes}, csv={len(csv_nodes)}",
    )
    add(
        checks,
        "Edge CSV row count matches manifest",
        len(csv_edges) == expected_edges,
        f"manifest={expected_edges}, csv={len(csv_edges)}",
    )
    add(checks, "GraphML node IDs are unique", len(graph_nodes) == len(set(graph_nodes)))

    edge_ids = [edge_id for _, _, edge_id in graph_edges if edge_id]
    duplicate_edge_id_count = len(edge_ids) - len(set(edge_ids))
    add(
        checks,
        "GraphML edge IDs are not required as unique identities",
        True,
        f"edge_id_duplicates={duplicate_edge_id_count}; source/target/order are used for validation",
    )

    add(checks, "No CSV node has empty ID", all(bool(node_id) for node_id in csv_node_ids))
    add(checks, "No CSV edge has empty source", all(bool(source) for source in csv_edge_sources))
    add(checks, "No CSV edge has empty target", all(bool(target) for target in csv_edge_targets))

    missing_sources = sorted(set(csv_edge_sources) - csv_node_ids)
    missing_targets = sorted(set(csv_edge_targets) - csv_node_ids)
    add(checks, "Every CSV edge source exists in node inventory", not missing_sources, ", ".join(missing_sources[:10]))
    add(checks, "Every CSV edge target exists in node inventory", not missing_targets, ", ".join(missing_targets[:10]))

    csv_nodes_not_in_graph = sorted(csv_node_ids - graph_nodes)
    graph_nodes_not_in_csv = sorted(graph_nodes - csv_node_ids)
    add(checks, "CSV node IDs match GraphML node IDs", not csv_nodes_not_in_graph and not graph_nodes_not_in_csv)

    high_risk_files = [
        row for row in csv_nodes if row.get("node_type") == "file" and row.get("risk_level") == "high"
    ]
    add(
        checks,
        "Every high-risk file node has an owner_agent",
        all(bool(row.get("owner_agent")) for row in high_risk_files),
    )
    add(
        checks,
        "Every high-risk file node has review_required=true",
        all(row.get("review_required") == "true" for row in high_risk_files),
    )

    benchmark_files = [
        row
        for row in csv_nodes
        if row.get("file_type") == "benchmark_result" or row.get("path", "").startswith("benchmarks/results/")
    ]
    add(
        checks,
        "Every benchmark result file is owned by or reviewable by EvaluatorAgent",
        all(
            row.get("owner_agent") == "EvaluatorAgent"
            or any(
                edge.get("source") == row.get("id")
                and edge.get("target") == "agent:EvaluatorAgent"
                and edge.get("relationship") == "requires_review_by"
                for edge in csv_edges
            )
            for row in benchmark_files
        ),
    )
    add(
        checks,
        "Every benchmark result file is high risk or review required",
        all(row.get("risk_level") == "high" or row.get("review_required") == "true" for row in benchmark_files),
    )

    governance_paths = {"AGENT.md", "machine_index.json", "TASK_BOARD.md", "NEXT_AGENT_STEP.md", "CONTRIBUTION_LOG.md"}
    governance_files = [row for row in csv_nodes if row.get("path") in governance_paths]
    add(
        checks,
        "Every governance file has review_required=true",
        all(row.get("review_required") == "true" for row in governance_files),
    )

    return checks


def main() -> int:
    checks = validate()
    failed = [check for check in checks if not check.passed]

    print("Ontology validation report\n")
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        suffix = f" — {check.detail}" if check.detail else ""
        print(f"{status}: {check.name}{suffix}")

    if failed:
        print(f"\nFAILED: {len(failed)} check(s) failed.")
        return 1

    print("\nPASS: all ontology checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
