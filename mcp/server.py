"""Lightweight local MCP-style command interface for QML Agent Lab.

This is intentionally simple: it exposes stable JSON-returning commands that
agents and humans can call locally without enabling automatic execution.
"""

import json
import sys
from pathlib import Path
from typing import Any

RESULTS_DIR = Path(__file__).resolve().parent.parent / "benchmarks" / "results"


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _canonical_experiment_name(path: Path) -> str:
    name = path.stem
    return name.removesuffix("_baseline")


def _resolve_experiment_path(name: str) -> Path:
    normalized = name.removesuffix(".json").removesuffix("_baseline")
    return RESULTS_DIR / f"{normalized}_baseline.json"


def list_experiments() -> list[dict[str, str]]:
    experiments = []
    for path in sorted(RESULTS_DIR.glob("*.json")):
        experiments.append({
            "name": _canonical_experiment_name(path),
            "result_file": str(path.relative_to(RESULTS_DIR.parent.parent)),
        })
    return experiments


def run_experiment(name: str) -> dict[str, Any]:
    """Return the current verified fixture for an experiment.

    This command intentionally does not trigger expensive training or quantum
    simulation. It reads the existing benchmark fixture for safe agent use.
    """
    path = _resolve_experiment_path(name)
    if not path.exists():
        return {"error": "experiment not found", "requested": name}
    return _load_json(path)


def get_results() -> list[dict[str, Any]]:
    return [_load_json(path) for path in sorted(RESULTS_DIR.glob("*.json"))]


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python mcp/server.py [list_experiments|get_results|run_experiment] [name]")
        return 1

    cmd = argv[1]

    if cmd == "list_experiments":
        print(json.dumps(list_experiments(), indent=2))
        return 0
    if cmd == "get_results":
        print(json.dumps(get_results(), indent=2))
        return 0
    if cmd == "run_experiment":
        if len(argv) < 3:
            print(json.dumps({"error": "provide experiment name"}, indent=2))
            return 1
        print(json.dumps(run_experiment(argv[2]), indent=2))
        return 0

    print(json.dumps({"error": "unknown command", "command": cmd}, indent=2))
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
