# Sprint Checklist

This checklist verifies that `qml-agent-lab` is ready for a first GitHub publication.

## Repository Structure

- [ ] `README.md` exists
- [ ] `AGENT.md` exists
- [ ] `LICENSE` exists
- [ ] `.gitignore` exists
- [ ] `requirements.txt` exists
- [ ] `agents/` directory exists
- [ ] `templates/` directory exists
- [ ] `docs/` directory exists
- [ ] `examples/` directory exists

## Agent Files

- [ ] `agents/qml_researcher.md`
- [ ] `agents/qml_architect.md`
- [ ] `agents/classical_baseline_engineer.md`
- [ ] `agents/experiment_engineer.md`
- [ ] `agents/evaluator.md`
- [ ] `agents/ethics_claims_reviewer.md`
- [ ] `agents/documentation_agent.md`

Each agent file includes:

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

Each template includes:

- [ ] Purpose
- [ ] Required metadata
- [ ] Limitations section
- [ ] Review checklist

## Examples

- [ ] `examples/qiskit_quantum_kernel_stub.py`
- [ ] `examples/qiskit_qnn_stub.py`
- [ ] `examples/pennylane_qnode_stub.py`

Each example:

- [ ] Runs as a normal Python script
- [ ] Uses local toy data or tiny input
- [ ] Handles missing imports gracefully
- [ ] Prints clear output
- [ ] Avoids large training loops
- [ ] Avoids unsupported claims

## Documentation

- [ ] README explains project purpose
- [ ] README includes quickstart
- [ ] README includes agent team
- [ ] README includes workflow
- [ ] README includes “What this repo is not”
- [ ] README includes roadmap
- [ ] `docs/qml_tooling_map.md` explains framework choices
- [ ] `docs/sprint_checklist.md` is complete

## Claim Safety

- [ ] No unsupported quantum advantage claims
- [ ] Educational examples labeled clearly
- [ ] Classical baseline requirement is visible
- [ ] Limitations are required in templates
- [ ] Ethics & Claims Reviewer exists
- [ ] Claim strength levels are defined

## Dependency Check

- [ ] Dependencies are minimal
- [ ] No Docker added
- [ ] No CI added
- [ ] No notebooks added
- [ ] No package build system added
- [ ] No cloud services required

## Publication Readiness

- [ ] Repo can be understood in under 5 minutes
- [ ] Repo is useful even before running examples
- [ ] Cursor can use `AGENT.md` as operating instructions
- [ ] Future experiments can reuse templates
- [ ] v0.1.0 release notes can be written

## Suggested v0.1.0 Release Notes

```markdown
# qml-agent-lab v0.1.0

Initial release.

Includes:
- Cursor/Codex-ready AGENT.md
- QML development agent team
- Reusable experiment templates
- QML tooling map
- Starter Qiskit and PennyLane examples
- Sprint checklist for publication readiness

This release focuses on agent orchestration, documentation discipline, and safe QML experimentation.
```
