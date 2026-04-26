import json
import sys
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "benchmarks" / "results"


def list_experiments():
    return [f.stem for f in RESULTS_DIR.glob("*.json")]


def run_experiment(name):
    path = RESULTS_DIR / f"{name}_baseline.json"
    if not path.exists():
        return {"error": "experiment not found"}
    return json.load(open(path))


def get_results():
    results = []
    for f in RESULTS_DIR.glob("*.json"):
        results.append(json.load(open(f)))
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python server.py [list_experiments|get_results|run_experiment]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "list_experiments":
        print(json.dumps(list_experiments(), indent=2))
    elif cmd == "get_results":
        print(json.dumps(get_results(), indent=2))
    elif cmd == "run_experiment":
        if len(sys.argv) < 3:
            print("Provide experiment name")
        else:
            print(json.dumps(run_experiment(sys.argv[2]), indent=2))
