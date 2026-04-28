# QML Agent Lab Task Board

This board is a lightweight Kanban system for humans and AI agents.

Goal: improve quantum machine learning benchmarks over time while preserving classical baselines, reproducibility, honest claims, and ontology-aware governance.

## Start Here

New contributors should choose one small task, create a contribution packet, run local validation, and open a pull request.

Agents should read these files first:

1. `machine_index.json`
2. `AGENT.md`
3. `TASK_BOARD.md`
4. `NEXT_AGENT_STEP.md`
5. `agent_contributions/README.md`
6. `ontology/README.md`

Agents should query the ontology before modifying governed files:

```bash
python scripts/query_ontology.py file <path>
python scripts/query_ontology.py reviewers <path>
python scripts/query_ontology.py gates <path>
```

## Backlog

| ID | Task | Difficulty | Output |
|---|---|---:|---|
| B-001 | Add Breast Cancer classical baseline | Easy | result JSON + notes |
| B-002 | Add Wine dataset classical baseline | Easy | result JSON + notes |
| B-003 | Add Digits 0 vs 1 benchmark | Medium | script + result JSON |
| B-004 | Add Seed sweep for Moons | Medium | multiple result JSON files |
| B-005 | Add Seed sweep for Iris | Medium | multiple result JSON files |
| B-006 | Try alternate Qiskit feature maps on Moons | Medium | comparison report |
| B-007 | Try PennyLane QNN on Moons | Medium | result JSON + limitations |
| B-008 | Add runtime and environment metadata to results | Easy | schema-compatible result update |
| B-009 | Improve leaderboard generation | Easy | sorted leaderboard with deltas |
| B-010 | Add Markdown report generator | Medium | generated report from JSON |
| B-011 | Add dynamic task generation proposal workflow | Medium | task proposal template + review rules |
| B-012 | Build visual dashboard concept for benchmark and task status | Medium | dashboard plan or simple static page |
| B-013 | Design contributor reputation system | Medium | scoring policy + anti-gaming rules |
| B-014 | Plan modular GraphML ontology source layout for v1.2 | Medium | module layout proposal + migration plan |
| B-015 | Add ontology bundle builder for v1.2 | Medium | script plan or implementation for module → bundle generation |
| B-016 | Add ontology module validation for v1.2 | Medium | validation rules for cross-module edges, duplicate IDs, and bundle counts |

## Ready

| ID | Task | Prompt |
|---|---|---|
| R-001 | Improve Moons benchmark | Use `tasks/improve_moons_accuracy.json` and submit a contribution packet. |
| R-002 | Improve Iris benchmark | Use `tasks/improve_iris_accuracy.json` and submit a contribution packet. |
| R-003 | Reduce QNN overfitting | Use `tasks/reduce_qnn_overfitting.json` and document train-test gap. |
| R-004 | Propose dynamic task generation | Create a safe workflow for agents to suggest new tasks without editing the board directly. |
| R-005 | Draft dashboard architecture | Design a static dashboard for benchmarks, leaderboard, tasks, and contribution packets. |
| R-006 | Draft reputation policy | Define how contributor quality can be recognized without encouraging benchmark gaming. |
| R-007 | Draft v1.2 modular ontology plan | Propose how `ontology/modules/` should split repo, agents, risks, workflows, ownership, benchmark governance, and validation links. |

## In Progress

Move a task here in your PR description if you are actively working on it.

## Review

Pull requests should include:

- Contribution packet
- Classical baseline
- Claim status
- Ontology query output for changed files
- Validation commands
- Limitations

## Done

Completed tasks should remain traceable through PRs and result files.

## v1.2 Roadmap

`v1.1` establishes one stable bundled GraphML ontology plus query and validation scripts.

A future `v1.2` branch may introduce:

- modular GraphML source files under `ontology/modules/`,
- a manifest-controlled merge order,
- a bundle builder that generates `agent_team_governance_ontology.graphml`,
- generated CSV inventories,
- per-module ownership and review routing,
- validation for duplicate IDs, orphan edges, cross-module links, and bundle consistency.

Until that work is explicitly started, the bundled GraphML file remains the source of truth.

## Guardrails

- No auto-merge.
- No automatic expensive benchmark execution.
- No unsupported quantum advantage claims.
- No result without a classical baseline.
- Small, reviewable PRs only.
- Reputation must reward quality, reproducibility, and honesty, not just higher quantum scores.
- Agents may propose new tasks, but humans approve board changes.
- Ontology changes should be validated with `python scripts/validate_ontology.py`.
