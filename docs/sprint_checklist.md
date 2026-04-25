# Repository Quality Checklist

This checklist verifies that `qml-agent-lab` remains consistent, professional, and aligned with its agent-first QML research-lab identity.

## Current Release State

- [ ] `VERSION` matches the README badge.
- [ ] `VERSION` matches `CITATION.cff`.
- [ ] `CHANGELOG.md` includes the current release.
- [ ] README benchmark summaries match the latest result files.
- [ ] Citation metadata points to the correct repository.

## Core Repository Structure

- [ ] `README.md` exists.
- [ ] `AGENT.md` exists.
- [ ] `LICENSE` exists.
- [ ] `.gitignore` exists.
- [ ] `requirements.txt` exists.
- [ ] `VERSION` exists.
- [ ] `CHANGELOG.md` exists.
- [ ] `CITATION.cff` exists.
- [ ] `CONTRIBUTING.md` exists.
- [ ] `CODE_OF_CONDUCT.md` exists.
- [ ] `SECURITY.md` exists.
- [ ] `pyproject.toml` exists.
- [ ] `agents/` directory exists.
- [ ] `templates/` directory exists.
- [ ] `docs/` directory exists.
- [ ] `examples/` directory exists.
- [ ] `results/` directory exists.

## Agent Files

- [ ] `agents/qml_researcher.md`
- [ ] `agents/qml_architect.md`
- [ ] `agents/classical_baseline_engineer.md`
- [ ] `agents/experiment_engineer.md`
- [ ] `agents/evaluator.md`
- [ ] `agents/ethics_claims_reviewer.md`
- [ ] `agents/documentation_agent.md`

Each agent file should include:

- [ ] Mission
- [ ] Inputs
- [ ] Outputs
- [ ] Allowed actions
- [ ] Escalation conditions
- [ ] Checklist

## Templates

- [ ] `templates/experiment_plan.md`
- [ ] `templates/dataset_card.md`
- [ ] `templates/qml_model_card.md`
- [ ] `templates/comparison_report.md`

Each template should include:

- [ ] Required metadata
- [ ] Classical baseline fields
- [ ] QML candidate fields
- [ ] Limitations section
- [ ] Claim review or claim strength section
- [ ] Review checklist

## Examples

Starter examples:

- [ ] `examples/classical_baseline_stub.py`
- [ ] `examples/qiskit_quantum_kernel_stub.py`
- [ ] `examples/qiskit_qnn_stub.py`
- [ ] `examples/pennylane_qnode_stub.py`

Functional benchmark examples:

- [ ] `examples/moons_quantum_kernel_comparison.py`
- [ ] `examples/iris_quantum_kernel_comparison.py`

Each example should:

- [ ] Run as a normal Python script.
- [ ] Use local toy or built-in data.
- [ ] Handle missing imports gracefully.
- [ ] Print readable output.
- [ ] Include a classical baseline where relevant.
- [ ] Avoid unsupported claims.
- [ ] Document limitations or print a claim review.

## Results

Current benchmark records:

- [ ] `results/moons_quantum_kernel_comparison_2026-04-25.md`
- [ ] `results/moons_quantum_kernel_comparison_2026-04-25.json`
- [ ] `results/iris_quantum_kernel_comparison_2026-04-25.md`
- [ ] `results/iris_quantum_kernel_comparison_2026-04-25.json`

Each result record should include:

- [ ] Dataset details
- [ ] Environment details
- [ ] Classical baseline configuration
- [ ] QML candidate configuration
- [ ] Metrics
- [ ] Confusion matrix or equivalent when applicable
- [ ] Interpretation
- [ ] Claim review
- [ ] Known limitations
- [ ] Recommended next steps

## Documentation

- [ ] README explains project purpose.
- [ ] README includes quickstart.
- [ ] README includes agent team.
- [ ] README includes workflow.
- [ ] README includes functional benchmark summaries.
- [ ] README includes project governance/style section.
- [ ] README includes “What this repo is not.”
- [ ] README includes roadmap.
- [ ] `docs/qml_tooling_map.md` explains framework choices.
- [ ] `docs/sprint_checklist.md` reflects the current repo state.

## Claim Safety

- [ ] No unsupported quantum advantage claims.
- [ ] Educational examples are labeled clearly.
- [ ] Classical baseline requirement is visible.
- [ ] Single-seed benchmark limitations are visible.
- [ ] QML underperformance is documented honestly where observed.
- [ ] Ethics & Claims Reviewer exists.
- [ ] Claim strength levels are defined in `AGENT.md`.

## Dependency and Scope Check

- [ ] Dependencies remain minimal.
- [ ] No Docker added unless explicitly justified.
- [ ] No CI added unless explicitly requested.
- [ ] No notebooks added unless explicitly requested.
- [ ] No package build metadata added unless the project intentionally becomes installable.
- [ ] No cloud services required.
- [ ] `pyproject.toml` remains style/tooling config, not package metadata.

## Agent-First Identity Check

The repo should continue to feel like:

```text
agents + templates + runnable examples + verified results
```

Not like a prematurely abstracted Python package.

Before major structural changes, ask:

- [ ] Does this make Cursor agents more effective?
- [ ] Does this preserve low-token navigation?
- [ ] Does this improve experiment discipline?
- [ ] Does this avoid unnecessary abstraction?
- [ ] Does this keep classical baselines central?

## Release Readiness

Before tagging or describing a release:

- [ ] Version fields are aligned.
- [ ] Changelog entry exists.
- [ ] README badge is updated.
- [ ] New examples are documented.
- [ ] New results are linked.
- [ ] Claims are reviewed.
- [ ] Limitations are included.
