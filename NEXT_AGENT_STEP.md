# Next Agent Step

If you are an AI agent or new contributor, follow this sequence:

1. Read `machine_index.json`
2. Review `AGENT.md`
3. Review `TASK_BOARD.md`
4. Query the ontology for any files you plan to modify:

```bash
python scripts/query_ontology.py file <path>
python scripts/query_ontology.py reviewers <path>
python scripts/query_ontology.py gates <path>
```

5. Select one item from **Ready** or **Backlog**
6. Open the corresponding task file in `tasks/` if it exists
7. Create a contribution packet in `agent_contributions/`
8. Make the smallest possible change to complete the task
9. Run validation:

```bash
python scripts/validate_repo.py
python scripts/validate_ontology.py
python benchmarks/runner.py
python mcp/server.py get_results
```

10. Submit a Pull Request using the PR template

## Important

- Always include a classical baseline
- Do not claim quantum advantage without evidence
- Document limitations clearly
- If the ontology marks a file as high risk or `review_required=true`, keep the change small and request review from the relevant agent role or human maintainer
- Do not enable auto-merge, automatic expensive benchmark execution, or uncontrolled agent loops

## After Your Contribution

Update `TASK_BOARD.md` if appropriate to guide the next contributor.

If repo structure, governance roles, benchmark artifacts, or review-routing rules changed, update the ontology files and run:

```bash
python scripts/validate_ontology.py
```

## v1.2 Planning Note

The `v1.1` branch keeps a single bundled GraphML ontology as the stable query target. A future `v1.2` branch may introduce modular GraphML source files, a build script, and stronger validation for merging those modules into the bundled ontology.

This creates a recursive improvement loop across contributors while keeping changes small, reviewable, and evidence-aligned.
