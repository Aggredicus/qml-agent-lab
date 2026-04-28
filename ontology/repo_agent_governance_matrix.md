# QML Agent Lab — Repo Agent Governance Matrix

## Agent Ownership Matrix

| Agent | Owns / Reviews | Required When |
|---|---|---|
| RepoStewardAgent | `AGENT.md`, `machine_index.json`, dependency/boundary policies | Repo-wide governance, automation, dependency, or structural changes. |
| QMLResearcherAgent | research docs, source registry, citations | New methods, papers, claims, or framework evaluations. |
| QMLArchitectAgent | QML examples, tooling map, experiment architecture | Encoding, ansatz, backend, feature-map or QML framework changes. |
| ClassicalBaselineEngineer | classical baselines and benchmark comparison integrity | Any new QML benchmark or QML model result. |
| ExperimentEngineer | runnable scripts in `examples/` | Code implementation or experiment script changes. |
| EvaluatorAgent | benchmark methodology, runner, results, leaderboard | Any metric, result, split, dataset, or comparison change. |
| EthicsClaimsReviewer | claims policy, limitations, published language | Any README/report/result wording implying QML performance or advantage. |
| DocumentationAgent | README, templates, quickstart, reports, cards | Documentation, templates, model/dataset card updates. |
| ContributionReviewerAgent | contribution log, rubric, reputation delta | PR review, contribution packets, scoring, reputation updates. |
| TaskBoardCuratorAgent | task board, next-agent step, tasks | Task additions, task movement, next-agent workflow changes. |
| SchemaGuardianAgent | schemas, validation script, machine-readable artifacts | Schema/result/packet structure changes. |
| MCPInterfaceAgent | `mcp/server.py` | Local command interface or agent command changes. |
| SecuritySafetyAgent | automation boundaries, secrets, external calls | Anything that could auto-run, auto-merge, call external services, or leak secrets. |

## Mandatory Review Gates

| Gate | Trigger | Primary Agent |
|---|---|---|
| BaselineIntegrity | New/changed benchmark or QML result | ClassicalBaselineEngineer |
| Reproducibility | Dataset/split/seed/metric/backend/environment changes | EvaluatorAgent |
| ClaimDiscipline | Any language about performance, superiority, advantage, or significance | EthicsClaimsReviewer |
| SmallChange | Broad rewrites, repo structure, dependency changes | RepoStewardAgent |
| Validation | Schema/result/packet/benchmark artifacts | SchemaGuardianAgent |
| HumanApproval | Auto-run, auto-merge, uncontrolled loops, expensive automation | RepoStewardAgent + SecuritySafetyAgent |

## PR Routing Rules

1. If a PR touches `benchmarks/results/*`, route to EvaluatorAgent, ClassicalBaselineEngineer, EthicsClaimsReviewer, and SchemaGuardianAgent.
2. If a PR touches `examples/*`, route to ExperimentEngineer and either QMLArchitectAgent or ClassicalBaselineEngineer depending on model type.
3. If a PR touches `docs/qml_claims_policy.md`, route to EthicsClaimsReviewer and RepoStewardAgent.
4. If a PR touches `AGENT.md`, `machine_index.json`, `TASK_BOARD.md`, `NEXT_AGENT_STEP.md`, or `CONTRIBUTION_LOG.md`, route to RepoStewardAgent and the relevant governance agent.
5. If a PR adds dependencies, route to RepoStewardAgent and SecuritySafetyAgent.
6. If a PR modifies `mcp/server.py`, route to MCPInterfaceAgent and SecuritySafetyAgent.

## Golden Rule

The repo should become more honest, reproducible, auditable, and useful to future agents after every accepted contribution.
