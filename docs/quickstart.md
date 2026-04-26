# Quickstart: Add a Benchmark Result

This guide shows the fastest safe path for adding a new benchmark result.

## 1. Start from the template

Copy:

```bash
cp templates/benchmark_result_template.json benchmarks/results/my_dataset_baseline.json
```

## 2. Run or collect your experiment externally

Use your own script, notebook, or local workflow to produce:

- dataset name
- classical baseline accuracy
- quantum model accuracy, if run
- limitations
- notes

## 3. Fill the benchmark JSON

Every result must include:

- `experiment_id`
- `dataset`
- `version`
- `classical_baseline`
- `quantum_model` or `null`
- `delta_vs_classical`
- `claim_status`
- `limitations`
- `notes`

## 4. Validate the repo metadata

```bash
python scripts/validate_repo.py
```

This checks structure, required fields, deltas, and claim status.

## 5. Update the leaderboard manually

```bash
python benchmarks/runner.py
```

This aggregates existing benchmark result files. It does not train models or run expensive experiments.

## 6. Create a contribution packet

Copy:

```bash
cp templates/contribution_packet_template.json agent_contributions/my_contribution.json
```

Then fill in:

- scientific value
- validation performed
- failure modes
- human review requirement

## 7. Open a pull request

Use the PR template and keep the change small.

## Reminder

Do not claim quantum advantage unless the evidence is repeated, controlled, and clearly documented.
