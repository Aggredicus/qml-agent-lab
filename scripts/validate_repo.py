"""Validate QML Agent Lab repository metadata.

This script performs lightweight structural checks only. It does not run
benchmarks, train models, call cloud services, or trigger automation.
"""

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BENCHMARK_DIR = ROOT / "benchmarks" / "results"
CONTRIB_DIR = ROOT / "agent_contributions"
ALLOWED_CLAIM_STATUS = {
    "quantum_underperforms",
    "quantum_matches_classical",
    "quantum_outperforms_classical",
    "quantum_not_run",
    "inconclusive",
    "not_applicable",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def as_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def validate_benchmark(path: Path, errors: list[str]) -> None:
    data = load_json(path)
    prefix = str(path.relative_to(ROOT))

    required = [
        "experiment_id",
        "dataset",
        "version",
        "classical_baseline",
        "delta_vs_classical",
        "claim_status",
        "limitations",
    ]
    for key in required:
        require(key in data, f"{prefix}: missing required field {key}", errors)

    baseline = data.get("classical_baseline") or {}
    c_acc = as_float(baseline.get("accuracy"))
    q_model = data.get("quantum_model") or None
    q_acc = as_float(q_model.get("accuracy")) if isinstance(q_model, dict) else None

    require(c_acc is not None, f"{prefix}: invalid classical accuracy", errors)
    require(isinstance(data.get("limitations"), list) and len(data.get("limitations", [])) > 0,
            f"{prefix}: limitations must be a non-empty list", errors)

    status = data.get("claim_status")
    require(status in ALLOWED_CLAIM_STATUS, f"{prefix}: invalid claim_status {status}", errors)

    if c_acc is not None and q_acc is not None:
        expected_delta = round(q_acc - c_acc, 6)
        recorded_delta = as_float(data.get("delta_vs_classical"))
        require(recorded_delta is not None and abs(recorded_delta - expected_delta) < 1e-6,
                f"{prefix}: delta_vs_classical does not match quantum - classical", errors)

        if q_acc > c_acc:
            expected_status = "quantum_outperforms_classical"
        elif abs(q_acc - c_acc) < 1e-6:
            expected_status = "quantum_matches_classical"
        else:
            expected_status = "quantum_underperforms"
        require(status == expected_status,
                f"{prefix}: claim_status should be {expected_status} for recorded scores", errors)

    if q_acc is None:
        require(status == "quantum_not_run", f"{prefix}: missing quantum accuracy should use quantum_not_run", errors)


def validate_contribution_packet(path: Path, errors: list[str]) -> None:
    data = load_json(path)
    prefix = str(path.relative_to(ROOT))
    required = ["contribution_id", "contribution_type", "goal", "human_review_required"]
    for key in required:
        require(key in data, f"{prefix}: missing required field {key}", errors)
    require(data.get("human_review_required") is True,
            f"{prefix}: human_review_required must be true", errors)
    if "claim_status" in data:
        require(data["claim_status"] in ALLOWED_CLAIM_STATUS,
                f"{prefix}: invalid claim_status {data['claim_status']}", errors)


def main() -> int:
    errors: list[str] = []

    for path in sorted(BENCHMARK_DIR.glob("*.json")):
        validate_benchmark(path, errors)

    for path in sorted(CONTRIB_DIR.glob("*.json")):
        validate_contribution_packet(path, errors)

    if errors:
        print("Validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: benchmark results and contribution packets look consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
