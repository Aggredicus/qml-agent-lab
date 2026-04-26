# Branch Registry

This file records the intended status of repository branches so humans and AI agents can quickly understand which branches are active, archived, or retired.

## Active Branches

| Branch | Status | Purpose |
|---|---|---|
| `main` | Active | Canonical stable branch. All new work should branch from here. |

## Archived Branches

| Branch | Status | Purpose |
|---|---|---|
| `archive/agent-v0.2.0-mcp-benchmark-lab` | Archived | Preserves the v0.2.0 MCP benchmark lab development state. |
| `archive/kanban-board` | Archived | Preserves the recursive Kanban and contribution-system development state. |

## Retired Branches

These branches have been merged and archived. They should not receive new work.

| Branch | Replacement Archive |
|---|---|
| `agent-v0.2.0-mcp-benchmark-lab` | `archive/agent-v0.2.0-mcp-benchmark-lab` |
| `kanban-board` | `archive/kanban-board` |

## Branch Rules

1. `main` is the source of truth.
2. New work should start from `main`.
3. `archive/*` branches are historical snapshots.
4. Retired branches should not be used for new pull requests.
5. If a branch is complete, archive it before deletion or retirement.

## Agent Guidance

If you are an AI agent:

- Use `main` unless explicitly instructed otherwise.
- Do not open pull requests from retired branches.
- Do not modify `archive/*` branches.
- If branch cleanup is needed, propose it through a contribution packet or use `scripts/archive_branch.sh` with human approval.
