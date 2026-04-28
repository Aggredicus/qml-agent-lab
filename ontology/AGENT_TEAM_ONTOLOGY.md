# Agent Team Governance Ontology

Repository: `Aggredicus/qml-agent-lab`

This document summarizes the Agent Team Governance Ontology for `qml-agent-lab`. The ontology formalizes the repository as a graph of agents, files, folders, policies, review gates, risks, workflows, tasks, benchmark artifacts, and governance constraints.

The purpose is to make the repository easier for human developers and AI agents to navigate safely, improve incrementally, and review without losing the project’s core scientific discipline.

## Core Interpretation

`qml-agent-lab` is an agent-first research environment for quantum machine learning. Its central governance principle is:

> Every QML experiment must include a classical baseline.

The ontology treats this rule as a first-class governance node connected to benchmark files, evaluation roles, PR review rules, claim discipline, and contribution scoring.

## Ontology Layers

The ontology is organized into the following layers:

1. **Repository Structure Layer** — root files, folders, scripts, docs, benchmarks, examples, templates, schemas, MCP interface, tasks, and contribution packets.
2. **Agent Role Layer** — QML Researcher, QML Architect, Classical Baseline Engineer, Experiment Engineer, Evaluator, Ethics & Claims Reviewer, Documentation Agent, and Maintainer/Human Reviewer.
3. **Governance Principle Layer** — baseline-first rule, no unsupported quantum advantage claims, small reversible changes, manual validation, no auto-merge, and no uncontrolled agent loops.
4. **Workflow Layer** — contribution loop, benchmark loop, review loop, reputation update loop, and next-agent sequence.
5. **Risk Layer** — quantum hype, missing baseline, benchmark gaming, dependency bloat, unreviewed automation, overbuilt abstractions, irreproducible results, and misleading claims.
6. **Review Gate Layer** — baseline integrity check, claims discipline check, dependency review, benchmark methodology review, contribution rubric review, and human approval.

## Primary Agent Roles

### QML Researcher Agent

Responsible for researching QML methods, papers, frameworks, and implementation-relevant tradeoffs. This role should summarize uncertainty and recommend small next actions.

### QML Architect Agent

Responsible for experiment design, model/circuit architecture, framework selection, feature-map choices, ansatz choices, backend decisions, and extension planning.

### Classical Baseline Engineer

Responsible for baseline-first comparison design. This agent must be invoked before treating a QML result as meaningful.

### Experiment Engineer

Responsible for runnable scripts and small implementation changes. This role must keep examples lightweight, readable, and graceful when optional dependencies are missing.

### Evaluator Agent

Responsible for checking same dataset, same split, same metric, leakage avoidance, reproducibility, baseline inclusion, and honest comparison.

### Ethics & Claims Reviewer

Responsible for weakening claims that exceed evidence, preventing unsupported quantum advantage claims, and ensuring limitations are explicit.

### Documentation Agent

Responsible for README updates, templates, dataset cards, model cards, comparison reports, task board updates, sprint checklists, and contributor guidance.

### Maintainer / Human Reviewer

Responsible for final approval, reputation update decisions, task board governance, and preventing uncontrolled automation.

## High-Value Governance Relationships

- `AGENT.md` defines the operating laws for all AI agents.
- `machine_index.json` exposes machine-readable repo entrypoints and schemas.
- `TASK_BOARD.md` manages human/agent Kanban tasks.
- `NEXT_AGENT_STEP.md` defines the recursive next-agent onboarding path.
- `CONTRIBUTION_LOG.md` records project memory and reputation updates.
- `docs/qml_claims_policy.md` governs allowed and disallowed result claims.
- `docs/benchmark_methodology.md` governs fair comparisons.
- `docs/contribution_value_rubric.md` governs contribution scoring.
- `scripts/validate_repo.py` validates benchmark schema and contribution structure.
- `benchmarks/runner.py` aggregates existing benchmark results without uncontrolled expensive execution.
- `mcp/server.py` exposes a lightweight local command interface.

## Recommended Agent Use Pattern

Before changing the repo, an AI agent should:

1. Read `machine_index.json`.
2. Read `AGENT.md`.
3. Read `TASK_BOARD.md`.
4. Read `NEXT_AGENT_STEP.md`.
5. Choose one small task.
6. Create or update a contribution packet.
7. Ensure every QML experiment includes a classical baseline.
8. Run validation locally.
9. Submit a small, reviewable change.
10. Avoid unsupported claims, auto-merge, auto-benchmark loops, or dependency sprawl.

## GraphML Use

The companion GraphML file, `agent_team_governance_ontology.graphml`, encodes this governance structure as nodes and typed edges. This makes it possible for future agents to query relationships such as:

- Which files define governance rules?
- Which agent reviews benchmark claims?
- Which files must be checked before modifying benchmark results?
- Which risks apply to a new QML experiment?
- Which scripts validate the repository?
- Which docs should be updated after a benchmark contribution?

## Design Principle

The ontology is not intended to replace human judgment. It is a map that helps agents operate with more context, restraint, and accountability.

The correct behavior for future agents is:

> Make the smallest useful improvement, preserve baselines, document limitations, validate locally, and leave the system easier for the next agent to understand.
