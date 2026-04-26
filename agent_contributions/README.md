# Agent Contribution Mode

Agent Contribution Mode is the safe path for AI coding agents to suggest improvements to this repository.

Agents should not make broad, uncontrolled changes. Instead, they should create a small contribution packet that explains the goal, files affected, validation plan, and scientific claims.

## Rules

1. Human review is required before merge.
2. Every QML experiment must include a classical baseline.
3. Claims must match benchmark evidence.
4. Agents should prefer small, reversible changes.
5. Agents should not enable automatic benchmark execution without explicit human approval.

## Recommended Flow

1. Read `machine_index.json`.
2. Choose one task from `tasks/`.
3. Create a contribution packet from a template.
4. Add or modify the smallest necessary files.
5. Run manual validation commands locally.
6. Submit the packet with the PR.

## Contribution Packet Types

- Experiment submission
- Benchmark result submission
- Improvement proposal
- Claim review

This mode keeps the project open to agentic AI development while preserving scientific discipline and human agency.
