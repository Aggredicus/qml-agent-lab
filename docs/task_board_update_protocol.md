# Task Board Update Protocol

The task board is controlled to prevent conflicting edits.

## Rules

- Agents MUST NOT directly edit `TASK_BOARD.md`.
- Agents must propose changes through contribution packets.
- Humans review and apply accepted changes.

## Allowed Actions

Agents may:

- Suggest new tasks
- Suggest re-prioritization
- Suggest task completion updates

Agents may not:

- Directly modify board structure
- Remove tasks without justification

## Workflow

1. Agent creates a contribution packet proposing a board change
2. Human reviews the proposal
3. Human updates `TASK_BOARD.md`
4. Change is logged in `CONTRIBUTION_LOG.md`

## Goal

Keep the board consistent, conflict-free, and aligned with project priorities.
