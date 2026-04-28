# Repo Agent Governance Matrix

Repository: `Aggredicus/qml-agent-lab`

This matrix maps major repo areas to responsible agent roles, review gates, and governance risks.

| Area | Primary Agent | Required Reviewer | Purpose | Key Risks | Required Checks |
|---|---|---|---|---|---|
| `AGENT.md` | Documentation Agent | Maintainer / Human Reviewer | Defines agent operating laws | Governance drift, unsafe autonomy | Keep laws aligned with repo principles |
| `machine_index.json` | Documentation Agent | Experiment Engineer | Machine-readable repo entrypoints | Stale entrypoints, broken agent routing | Validate paths and schemas |
| `TASK_BOARD.md` | Documentation Agent | Maintainer / Human Reviewer | Human/agent Kanban system | Task sprawl, unsafe autonomous task mutation | Human approval for board changes |
| `NEXT_AGENT_STEP.md` | Documentation Agent | Maintainer / Human Reviewer | New-agent onboarding sequence | Recursive agent loops, missing guardrails | Ensure small-task discipline |
| `CONTRIBUTION_LOG.md` | Maintainer / Human Reviewer | Ethics & Claims Reviewer | Project memory and reputation tracking | Reputation gaming, unfair scoring | Use rubric, reward reproducibility |
| `agents/` | Documentation Agent | Maintainer / Human Reviewer | Role definitions | Role overlap, vague responsibilities | Keep roles small and operational |
| `templates/` | Documentation Agent | Evaluator Agent | Reusable experiment artifacts | Missing required fields | Preserve baseline and limitations fields |
| `examples/` | Experiment Engineer | Evaluator Agent | Runnable examples | Heavy dependencies, irreproducibility | Graceful imports, small scripts |
| `benchmarks/` | Evaluator Agent | Classical Baseline Engineer | Benchmark results and aggregation | Missing baselines, benchmark gaming | Same dataset/split/metric, schema validation |
| `benchmarks/results/` | Evaluator Agent | Ethics & Claims Reviewer | Stored benchmark fixtures | Overstated result interpretation | Verify claim status vs delta |
| `schemas/` | Experiment Engineer | Evaluator Agent | Validation schema | Schema drift, incompatible results | Validate sample fixtures |
| `mcp/` | Experiment Engineer | Maintainer / Human Reviewer | Lightweight local command interface | Uncontrolled execution, expensive runs | No auto-run expensive benchmarks |
| `scripts/` | Experiment Engineer | Evaluator Agent | Validation and helper scripts | Silent failure, destructive helpers | Clear errors, no hidden automation |
| `docs/qml_claims_policy.md` | Ethics & Claims Reviewer | Maintainer / Human Reviewer | Claim discipline | Quantum hype | Weaken claims beyond evidence |
| `docs/benchmark_methodology.md` | Evaluator Agent | Classical Baseline Engineer | Fair comparison rules | Leakage, unfair comparisons | Same dataset/split/metric |
| `docs/contribution_value_rubric.md` | Maintainer / Human Reviewer | Ethics & Claims Reviewer | Contribution scoring | Accuracy-only incentives | Reward signal, reproducibility, honesty |
| `tasks/` | Documentation Agent | Maintainer / Human Reviewer | Task definitions | Unsafe task expansion | Keep tasks bounded and reviewable |
| `agent_contributions/` | Contributor Agent | Maintainer / Human Reviewer | Structured contribution packets | Unreviewed edits, missing validation | Packet includes risks, validation, limitations |
| `ontology/` | Documentation Agent | Maintainer / Human Reviewer | Agent governance graph artifacts | Stale ontology | Regenerate after major repo changes |

## Default Review Routing

- New QML method: QML Researcher Agent → QML Architect Agent → Classical Baseline Engineer → Evaluator Agent → Ethics & Claims Reviewer.
- New benchmark result: Classical Baseline Engineer → Evaluator Agent → Ethics & Claims Reviewer → Maintainer / Human Reviewer.
- New docs/templates: Documentation Agent → relevant domain agent → Maintainer / Human Reviewer.
- New scripts/MCP changes: Experiment Engineer → Evaluator Agent → Maintainer / Human Reviewer.
- New governance policy: Documentation Agent → Ethics & Claims Reviewer → Maintainer / Human Reviewer.

## Non-Negotiable Gates

1. Classical baseline required for every QML experiment.
2. Claims must match evidence.
3. Limitations must be documented.
4. Changes must be small and reviewable.
5. No auto-merge or uncontrolled agent loops.
6. No large dependency additions without explicit justification.
7. Negative or inconclusive results are acceptable when reproducible and honestly reported.
