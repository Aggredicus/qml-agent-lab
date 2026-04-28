#!/usr/bin/env python3
"""Query the qml-agent-lab governance ontology.

This script intentionally uses only the Python standard library so agents can
inspect ontology routing without installing project dependencies.
"""

from __future__ import annotations

import argparse
import difflib
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_PATH = REPO_ROOT / "ontology" / "agent_team_governance_ontology.graphml"
GRAPHML_NS = {"g": "http://graphml.graphdrawing.org/xmlns"}


@dataclass(frozen=True)
class Edge:
    """Simple directed edge representation."""

    source: str
    target: str
    attrs: dict[str, str]


@dataclass
class Ontology:
    """Parsed GraphML ontology."""

    nodes: dict[str, dict[str, str]]
    edges: list[Edge]

    @property
    def outgoing(self) -> dict[str, list[Edge]]:
        result: dict[str, list[Edge]] = {}
        for edge in self.edges:
            result.setdefault(edge.source, []).append(edge)
        return result

    @property
    def incoming(self) -> dict[str, list[Edge]]:
        result: dict[str, list[Edge]] = {}
        for edge in self.edges:
            result.setdefault(edge.target, []).append(edge)
        return result


def load_ontology(path: Path = ONTOLOGY_PATH) -> Ontology:
    """Load GraphML and normalize key IDs to their attr.name values."""

    if not path.exists():
        raise FileNotFoundError(f"Ontology file not found: {path}")

    tree = ET.parse(path)
    root = tree.getroot()

    key_names: dict[str, str] = {}
    for key in root.findall("g:key", GRAPHML_NS):
        key_id = key.attrib.get("id")
        attr_name = key.attrib.get("attr.name")
        if key_id and attr_name:
            key_names[key_id] = attr_name

    graph = root.find("g:graph", GRAPHML_NS)
    if graph is None:
        raise ValueError(f"No <graph> element found in {path}")

    nodes: dict[str, dict[str, str]] = {}
    for node in graph.findall("g:node", GRAPHML_NS):
        node_id = node.attrib.get("id", "")
        if node_id:
            nodes[node_id] = _data_attrs(node, key_names)

    edges: list[Edge] = []
    for edge in graph.findall("g:edge", GRAPHML_NS):
        source = edge.attrib.get("source", "")
        target = edge.attrib.get("target", "")
        if source and target:
            edges.append(Edge(source=source, target=target, attrs=_data_attrs(edge, key_names)))

    return Ontology(nodes=nodes, edges=edges)


def _data_attrs(element: ET.Element, key_names: dict[str, str]) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for data in element.findall("g:data", GRAPHML_NS):
        key = data.attrib.get("key", "")
        name = key_names.get(key, key)
        attrs[name] = data.text or ""
    return attrs


def resolve_node(query: str, ontology: Ontology) -> str | None:
    """Resolve a node ID, file path, label, or bare agent name to a node ID."""

    if query in ontology.nodes:
        return query

    candidates = []
    if not query.startswith("file:"):
        candidates.append(f"file:{query}")
    if not query.startswith("agent:"):
        candidates.append(f"agent:{query}")

    for candidate in candidates:
        if candidate in ontology.nodes:
            return candidate

    for node_id, attrs in ontology.nodes.items():
        if attrs.get("path") == query or attrs.get("label") == query:
            return node_id

    return None


def close_matches(query: str, ontology: Ontology, limit: int = 8) -> list[str]:
    searchable = set(ontology.nodes)
    for node_id, attrs in ontology.nodes.items():
        for key in ("path", "label"):
            value = attrs.get(key)
            if value:
                searchable.add(value)
    return difflib.get_close_matches(query, sorted(searchable), n=limit, cutoff=0.35)


def relationship(edge: Edge) -> str:
    return edge.attrs.get("relationship", "")


def node_label(node_id: str, ontology: Ontology) -> str:
    attrs = ontology.nodes.get(node_id, {})
    label = attrs.get("label")
    return f"{label} ({node_id})" if label and label != node_id else node_id


def print_summary(ontology: Ontology) -> None:
    node_types = Counter(attrs.get("node_type", "unknown") for attrs in ontology.nodes.values())
    rel_types = Counter(relationship(edge) or "unknown" for edge in ontology.edges)
    high_risk_files = [
        node_id
        for node_id, attrs in ontology.nodes.items()
        if attrs.get("node_type") == "file" and attrs.get("risk_level") == "high"
    ]
    review_required_files = [
        node_id
        for node_id, attrs in ontology.nodes.items()
        if attrs.get("node_type") == "file" and attrs.get("review_required") == "true"
    ]

    print("# Ontology Summary\n")
    print(f"- Nodes: {len(ontology.nodes)}")
    print(f"- Edges: {len(ontology.edges)}")
    print(f"- High-risk files: {len(high_risk_files)}")
    print(f"- Review-required files: {len(review_required_files)}")
    print("\n## Node types")
    for node_type, count in sorted(node_types.items()):
        print(f"- {node_type}: {count}")
    print("\n## Relationship types")
    for rel_type, count in sorted(rel_types.items()):
        print(f"- {rel_type}: {count}")


def print_file(query: str, ontology: Ontology) -> int:
    node_id = resolve_node(query, ontology)
    if not node_id:
        return print_not_found(query, ontology)

    attrs = ontology.nodes[node_id]
    print(f"# File: {attrs.get('path') or attrs.get('label') or node_id}\n")
    print(f"- Node ID: {node_id}")
    print(f"- Label: {attrs.get('label', '')}")
    print(f"- Path: {attrs.get('path', '')}")
    print(f"- File type: {attrs.get('file_type', '')}")
    print(f"- Owner agent: {attrs.get('owner_agent', '')}")
    print(f"- Risk level: {attrs.get('risk_level', '')}")
    print(f"- Review required: {attrs.get('review_required', '')}")
    print(f"- Description: {attrs.get('description', '')}")

    print_list("Owners", owners_for(node_id, ontology))
    print_list("Suggested reviewers", reviewers_for(node_id, ontology))
    print_list("Review gates", gates_for(node_id, ontology))
    print_list("Risks", risks_for(node_id, ontology))
    print_edges("Outgoing relationships", ontology.outgoing.get(node_id, []), ontology, forward=True)
    print_edges("Incoming relationships", ontology.incoming.get(node_id, []), ontology, forward=False)
    return 0


def print_agent(query: str, ontology: Ontology) -> int:
    node_id = resolve_node(query, ontology)
    if not node_id:
        return print_not_found(query, ontology)

    attrs = ontology.nodes[node_id]
    print(f"# Agent: {attrs.get('label') or node_id}\n")
    print(f"- Node ID: {node_id}")
    print(f"- Description: {attrs.get('description', '')}")

    owned_files = sorted(
        edge.target
        for edge in ontology.outgoing.get(node_id, [])
        if relationship(edge) == "owns" and ontology.nodes.get(edge.target, {}).get("node_type") == "file"
    )
    review_files = sorted(
        edge.source for edge in ontology.incoming.get(node_id, []) if relationship(edge) == "requires_review_by"
    )
    gates = sorted(
        edge.target
        for edge in ontology.outgoing.get(node_id, [])
        if ontology.nodes.get(edge.target, {}).get("node_type") == "review_gate"
    )
    risks = sorted(
        edge.target
        for edge in ontology.outgoing.get(node_id, [])
        if ontology.nodes.get(edge.target, {}).get("node_type") == "risk"
    )
    workflows = sorted(
        {edge.source for edge in ontology.incoming.get(node_id, []) if ontology.nodes.get(edge.source, {}).get("node_type") == "workflow"}
        | {edge.target for edge in ontology.outgoing.get(node_id, []) if ontology.nodes.get(edge.target, {}).get("node_type") == "workflow"}
    )

    print_list("Owned files", [node_label(item, ontology) for item in owned_files])
    print_list("Files requiring this reviewer", [node_label(item, ontology) for item in review_files])
    print_list("Review gates enforced", [node_label(item, ontology) for item in gates])
    print_list("Governed risks", [node_label(item, ontology) for item in risks])
    print_list("Related workflows", [node_label(item, ontology) for item in workflows])
    return 0


def owners_for(node_id: str, ontology: Ontology) -> list[str]:
    attrs = ontology.nodes.get(node_id, {})
    owners = set()
    owner_agent = attrs.get("owner_agent")
    if owner_agent:
        owners.add(owner_agent)
        owners.add(f"agent:{owner_agent}")

    for edge in ontology.incoming.get(node_id, []):
        if relationship(edge) == "owns":
            owners.add(edge.source)
    return sorted(node_label(owner, ontology) if owner in ontology.nodes else owner for owner in owners)


def reviewers_for(node_id: str, ontology: Ontology) -> list[str]:
    reviewers = set()

    for edge in ontology.outgoing.get(node_id, []):
        if relationship(edge) == "requires_review_by":
            reviewers.add(edge.target)

    attrs = ontology.nodes.get(node_id, {})
    owner_agent = attrs.get("owner_agent")
    if owner_agent:
        owner_id = f"agent:{owner_agent}"
        reviewers.add(owner_id if owner_id in ontology.nodes else owner_agent)

    path = attrs.get("path", "")
    file_type = attrs.get("file_type", "")

    if "benchmarks/results/" in path or file_type == "benchmark_result":
        reviewers.update([
            "agent:EvaluatorAgent",
            "agent:ClassicalBaselineEngineer",
            "agent:EthicsClaimsReviewer",
            "agent:SchemaGuardianAgent",
        ])
    if path.startswith("examples/"):
        reviewers.update(["agent:ExperimentEngineer", "agent:EvaluatorAgent"])
    if path in {"AGENT.md", "machine_index.json", "TASK_BOARD.md", "NEXT_AGENT_STEP.md", "CONTRIBUTION_LOG.md"}:
        reviewers.add("agent:RepoStewardAgent")
    if "claims" in path.lower() or "claim" in file_type.lower():
        reviewers.add("agent:EthicsClaimsReviewer")

    return sorted(node_label(item, ontology) if item in ontology.nodes else item for item in reviewers)


def gates_for(node_id: str, ontology: Ontology) -> list[str]:
    gates = set()
    attrs = ontology.nodes.get(node_id, {})
    path = attrs.get("path", "")
    file_type = attrs.get("file_type", "")

    for reviewer_text in reviewers_for(node_id, ontology):
        reviewer_id = reviewer_text.split(" (")[-1].rstrip(")") if " (" in reviewer_text else reviewer_text
        if reviewer_id in ontology.nodes:
            for edge in ontology.outgoing.get(reviewer_id, []):
                if ontology.nodes.get(edge.target, {}).get("node_type") == "review_gate":
                    gates.add(edge.target)

    if "benchmarks/results/" in path or file_type == "benchmark_result":
        gates.update(["gate:Gate_BaselineIntegrity", "gate:Gate_Reproducibility", "gate:Gate_ClaimDiscipline", "gate:Gate_Validation"])
    if attrs.get("risk_level") == "high" or attrs.get("review_required") == "true":
        gates.add("gate:Gate_SmallChange")
    if path in {"AGENT.md", "machine_index.json", "TASK_BOARD.md", "NEXT_AGENT_STEP.md"}:
        gates.add("gate:Gate_HumanApproval")

    return sorted(node_label(item, ontology) if item in ontology.nodes else item for item in gates)


def risks_for(node_id: str, ontology: Ontology) -> list[str]:
    risks = set()
    attrs = ontology.nodes.get(node_id, {})
    path = attrs.get("path", "")
    file_type = attrs.get("file_type", "")

    for edge in ontology.outgoing.get(node_id, []) + ontology.incoming.get(node_id, []):
        other = edge.target if edge.source == node_id else edge.source
        if ontology.nodes.get(other, {}).get("node_type") == "risk":
            risks.add(other)

    if "benchmarks/results/" in path or file_type == "benchmark_result":
        risks.update(["risk:Risk_MissingClassicalBaseline", "risk:Risk_UnsupportedQuantumAdvantageClaims", "risk:Risk_BenchmarkGaming"])
    if path.startswith("examples/"):
        risks.update(["risk:Risk_MissingClassicalBaseline", "risk:Risk_UnsupportedQuantumAdvantageClaims"])
    if path in {"AGENT.md", "machine_index.json", "TASK_BOARD.md", "NEXT_AGENT_STEP.md"}:
        risks.update(["risk:Risk_UncontrolledAgentLoops", "risk:Risk_LargeUnreviewedRewrite"])
    if path == "mcp/server.py":
        risks.add("risk:Risk_UncontrolledAgentLoops")

    return sorted(node_label(item, ontology) if item in ontology.nodes else item for item in risks)


def print_list(title: str, items: Iterable[str]) -> None:
    items = list(dict.fromkeys(items))
    print(f"\n## {title}")
    if not items:
        print("- None found")
        return
    for item in items:
        print(f"- {item}")


def print_edges(title: str, edges: list[Edge], ontology: Ontology, *, forward: bool) -> None:
    print(f"\n## {title}")
    if not edges:
        print("- None found")
        return
    for edge in sorted(edges, key=lambda item: (relationship(item), item.source, item.target)):
        other = edge.target if forward else edge.source
        direction = "->" if forward else "<-"
        rel = relationship(edge) or "related"
        print(f"- {direction} {node_label(other, ontology)} [{rel}]")


def print_collection(kind: str, query: str, ontology: Ontology) -> int:
    node_id = resolve_node(query, ontology)
    if not node_id:
        return print_not_found(query, ontology)

    if kind == "owners":
        print_list("Owners", owners_for(node_id, ontology))
    elif kind == "reviewers":
        print_list("Suggested reviewers", reviewers_for(node_id, ontology))
    elif kind == "gates":
        print_list("Review gates", gates_for(node_id, ontology))
    elif kind == "risks":
        print_list("Risks", risks_for(node_id, ontology))
    else:
        raise ValueError(f"Unsupported collection kind: {kind}")
    return 0


def print_not_found(query: str, ontology: Ontology) -> int:
    print(f"ERROR: No ontology node matched: {query}", file=sys.stderr)
    matches = close_matches(query, ontology)
    if matches:
        print("\nClose matches:", file=sys.stderr)
        for match in matches:
            print(f"- {match}", file=sys.stderr)
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query the qml-agent-lab governance ontology.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("summary", help="Print graph counts and type summaries.")

    for command in ("file", "agent", "risks", "gates", "reviewers", "owners"):
        subparser = subparsers.add_parser(command, help=f"Query ontology {command}.")
        subparser.add_argument("query", help="Path, node ID, label, or agent name.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        ontology = load_ontology()
    except (FileNotFoundError, ET.ParseError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.command == "summary":
        print_summary(ontology)
        return 0
    if args.command == "file":
        return print_file(args.query, ontology)
    if args.command == "agent":
        return print_agent(args.query, ontology)
    if args.command in {"risks", "gates", "reviewers", "owners"}:
        return print_collection(args.command, args.query, ontology)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
