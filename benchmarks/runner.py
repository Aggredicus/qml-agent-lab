"""Benchmark aggregation and validation for QML Agent Lab.

Loads result fixtures, validates required fields, recomputes deltas, and
writes a leaderboard. Does not run experiments automatically.
"""

import json
from pathlib import Path
from typing import Any

RESULTS_DIR = Path(__file__).resolve().parent / "results"
LEADERBOARD_PATH = Path(__file__).resolve().parent / "leaderboard.json"
REPO_VERSION = "v1.0.0"


def _safe_float(x: Any) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def load_results() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for file in sorted(RESULTS_DIR.glob("*.json")):
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if "classical_baseline" not in data:
            raise ValueError(f"Missing classical baseline in {file}")

        c = _safe_float(data["classical_baseline"].get("accuracy"))
        q = _safe_float((data.get("quantum_model") or {}).get("accuracy"))

        if c is None:
            raise ValueError(f"Invalid classical accuracy in {file}")

        if q is not None:
            data["delta_vs_classical"] = round(q - c, 6)
        else:
            data["delta_vs_classical"] = None

        status = data.get("claim_status")
        if q is None:
            expected = "quantum_not_run"
        elif abs(q - c) < 1e-6:
            expected = "quantum_matches_classical"
        elif q > c:
            expected = "quantum_outperforms_classical"
        else:
            expected = "quantum_underperforms"

        if status != expected:
            data["claim_status"] = expected

        results.append(data)
    return results


def update_leaderboard(results: list[dict[str, Any]]) -> dict[str, Any]:
    def q_acc(x: dict[str, Any]) -> float:
        q = (x.get("quantum_model") or {}).get("accuracy")
        return _safe_float(q) or 0.0

    leaderboard = {
        "repo_version": REPO_VERSION,
        "principle": "Every QML experiment must include a classical baseline.",
        "benchmarks": sorted(results, key=q_acc, reverse=True),
    }

    with LEADERBOARD_PATH.open("w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2)

    return leaderboard


def print_summary(results: list[dict[str, Any]]) -> None:
    print("\nQML Agent Lab Benchmark Summary\n")

    best_classical = max(results, key=lambda r: r["classical_baseline"]["accuracy"])
    best_quantum = max(results, key=lambda r: (r.get("quantum_model") or {}).get("accuracy") or 0)
    largest_delta = max(results, key=lambda r: abs(r.get("delta_vs_classical") or 0))

    print(f"Best classical: {best_classical['dataset']} ({best_classical['classical_baseline']['accuracy']:.3f})")
    print(f"Best quantum: {best_quantum['dataset']}")
    print(f"Largest delta: {largest_delta['dataset']} ({largest_delta['delta_vs_classical']})")

    for r in results:
        c = r["classical_baseline"]["accuracy"]
        q = (r.get("quantum_model") or {}).get("accuracy")
        d = r.get("delta_vs_classical")
        print(f"{r['dataset']}: classical={c:.3f}, quantum={q if q is not None else 'NA'}, delta={d}")


if __name__ == "__main__":
    results = load_results()
    update_leaderboard(results)
    print_summary(results)
