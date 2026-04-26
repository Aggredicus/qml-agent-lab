# Contribution Log

This file records accepted or simulated contributions that shaped QML Agent Lab.

The purpose is to make project evolution visible to humans and AI agents without relying only on raw commit history.

## Contribution Status Key

| Status | Meaning |
|---|---|
| Accepted | Merged or incorporated into the repository |
| Proposed | Suggested but not yet merged |
| Simulated | Tested in agent simulation, not necessarily merged |
| Rejected | Reviewed and declined |

---

## v0.3.0

### Core Infrastructure

| Contribution | Type | Status | Notes |
|---|---|---|---|
| `v0.2.0_mcp_benchmark_system` | infrastructure | Accepted | Added MCP interface, benchmark runner, schemas, tasks, and Agent Contribution Mode. |
| `v0.3.0_recursive_kanban_quality_fixes` | governance | Accepted | Added task board, next-agent guide, restored AGENT.md, improved MCP and benchmark validation. |
| `readme_human_agent_polish` | documentation | Accepted | Updated README to serve both human developers and AI agents. |
| `branch_lifecycle_system` | governance | Accepted | Added branch registry and archive helper script. |

### Agent Simulation Contributions

| Contribution | Type | Status | Notes |
|---|---|---|---|
| `breast_cancer_classical_baseline_001` | benchmark_result | Simulated | Proposed a baseline-only Breast Cancer benchmark fixture for future QML comparison. |
| `dashboard_architecture_plan_001` | improvement | Simulated | Proposed a static dashboard architecture without new frontend dependencies. |
| `claims_language_review_001` | claim_review | Simulated | Proposed a QML claims policy and language audit. |

---

## Contribution Principles

Accepted contributions should:

- Preserve classical baselines
- Document limitations
- Avoid unsupported quantum advantage claims
- Keep changes small and reviewable
- Improve clarity for both humans and agents

## Future Use

When a contribution is accepted, add a short row here with:

- contribution ID
- type
- status
- notes

This log is not a replacement for Git history. It is a readable project memory layer.
