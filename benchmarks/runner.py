import json
from pathlib import Path

RESULTS_DIR = Path(__file__).parent / "results"
LEADERBOARD_PATH = Path(__file__).parent / "leaderboard.json"


def load_results():
    results = []
    for file in RESULTS_DIR.glob("*.json"):
        with open(file, "r") as f:
            data = json.load(f)
            if "classical_baseline" not in data:
                raise ValueError(f"Missing classical baseline in {file}")
            results.append(data)
    return results


def update_leaderboard(results):
    leaderboard = {
        "repo_version": "v0.2.0",
        "principle": "Every QML experiment must include a classical baseline.",
        "benchmarks": sorted(
            results,
            key=lambda x: (x.get("quantum_model", {}).get("accuracy") or 0),
            reverse=True,
        ),
    }

    with open(LEADERBOARD_PATH, "w") as f:
        json.dump(leaderboard, f, indent=2)

    return leaderboard


def print_summary(results):
    print("\nQML Agent Lab Benchmark Summary\n")
    for r in results:
        c = r["classical_baseline"]["accuracy"]
        q = r.get("quantum_model", {}).get("accuracy")
        d = r["delta_vs_classical"]
        print(f"{r['dataset']}: classical={c:.3f}, quantum={q:.3f}, delta={d:.3f}")


if __name__ == "__main__":
    results = load_results()
    leaderboard = update_leaderboard(results)
    print_summary(results)
