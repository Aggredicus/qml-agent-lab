# Contribution Log

This file records accepted, proposed, rejected, and simulated contributions that shaped QML Agent Lab.

The purpose is to make project evolution visible to humans and AI agents without relying only on raw commit history.

## Contribution Status Key

| Status | Meaning | Reputation Guidance |
|---|---|---|
| Accepted | Merged or incorporated into the repository | Usually positive |
| Proposed | Suggested but not yet merged | Neutral |
| Simulated | Tested in agent simulation, not necessarily merged | Neutral |
| Rejected | Reviewed and declined | Negative only if unsafe, careless, misleading, or repeatedly low-effort |

---

## Review-Guided Reputation Process

Reputation is not updated by remote automation.

During review, a human maintainer or authorized agent should:

1. Read the contributor's self-score and justification.
2. Assign a reviewer score using `docs/contribution_value_rubric.md`.
3. Use `scripts/calculate_reputation_delta.py` to calculate a suggested delta.
4. Decide whether to accept, adjust, or reject the suggested delta.
5. Add or update a row in this log after the PR decision.

Reviewer score overrides contributor self-score.

Honest negative, inconclusive, or failed experiments should not be penalized when they are reproducible, well-documented, and scientifically useful.

---

## Reputation Delta Guide

| Reviewer Score | Accepted PR | Rejected PR |
|---:|---:|---:|
| 0-3 | 0 | -2 |
| 4-6 | +1 | -1 |
| 7-8 | +2 | 0 |
| 9-10 | +3 | 0 |

Use this as guidance, not an automatic remote rule.

---

## Log Fields

Contribution rows may include:

- `Self Score`: contributor's rubric score, 0-10
- `Reviewer Score`: adjusted reviewer score, 0-10
- `Confidence`: contributor confidence in self-score, 0-1
- `Reputation Delta`: reviewer-guided reputation change

---

## v0.3.0

### Core Infrastructure

| Contribution | Type | Status | Self Score | Reviewer Score | Confidence | Reputation Delta | Notes |
|---|---|---|---:|---:|---:|---:|---|
| `v0.2.0_mcp_benchmark_system` | infrastructure | Accepted | 8 | 8 | 0.8 | +2 | Added MCP interface, benchmark runner, schemas, tasks, and Agent Contribution Mode. |
| `v0.3.0_recursive_kanban_quality_fixes` | governance | Accepted | 9 | 9 | 0.8 | +3 | Added task board, next-agent guide, restored AGENT.md, improved MCP and benchmark validation. |
| `readme_human_agent_polish` | documentation | Accepted | 7 | 7 | 0.7 | +2 | Updated README to serve both human developers and AI agents. |
| `branch_lifecycle_system` | governance | Accepted | 7 | 7 | 0.7 | +2 | Added branch registry and archive helper script. |

### Agent Simulation Contributions

| Contribution | Type | Status | Self Score | Reviewer Score | Confidence | Reputation Delta | Notes |
|---|---|---|---:|---:|---:|---:|---|
| `breast_cancer_classical_baseline_001` | benchmark_result | Simulated | 7 | 7 | 0.7 | 0 | Proposed a baseline-only Breast Cancer benchmark fixture for future QML comparison. |
| `dashboard_architecture_plan_001` | improvement | Simulated | 6 | 6 | 0.7 | 0 | Proposed a static dashboard architecture without new frontend dependencies. |
| `claims_language_review_001` | claim_review | Simulated | 8 | 8 | 0.8 | 0 | Proposed a QML claims policy and language audit. |

---

## Contribution Principles

Accepted contributions should:

- Preserve classical baselines
- Document limitations
- Avoid unsupported quantum advantage claims
- Keep changes small and reviewable
- Improve clarity for both humans and agents

## Future Use

When a contribution is accepted or reviewed, add a row with:

- contribution ID
- type
- status
- self score
- reviewer score
- confidence
- reputation delta
- notes

This log is not a replacement for Git history. It is a readable project memory layer.
