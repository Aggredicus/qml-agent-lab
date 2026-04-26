# Next Agent Step

If you are an AI agent or new contributor, follow this sequence:

1. Read `machine_index.json`
2. Review `TASK_BOARD.md`
3. Select one item from **Ready** or **Backlog**
4. Open the corresponding task file in `tasks/` if it exists
5. Create a contribution packet in `agent_contributions/`
6. Make the smallest possible change to complete the task
7. Run validation:

```bash
python benchmarks/runner.py
python mcp/server.py get_results
```

8. Submit a Pull Request using the PR template

## Important

- Always include a classical baseline
- Do not claim quantum advantage without evidence
- Document limitations clearly

## After Your Contribution

Update `TASK_BOARD.md` if appropriate to guide the next contributor.

This creates a recursive improvement loop across contributors.
