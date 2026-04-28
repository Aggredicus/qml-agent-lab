# QML Agent Lab — Full Agent Governance Ontology

Repository: `Aggredicus/qml-agent-lab`  
Ontology artifact: `agent_team_governance_ontology.graphml`  
Generated purpose: make the repo's agent roles, files, policies, review gates, risks, workflows, and validation paths explicit as a portable GraphML knowledge graph.

## 1. Executive Summary

`qml-agent-lab` is already structured as an agent-first QML research environment. Its core design principle is baseline-first and evidence-first QML experimentation: every QML experiment must include a classical baseline, every claim must match the evidence, and contributions should remain small, auditable, and reproducible.

This ontology turns that governance model into a machine-readable graph. It is designed so Cursor, Copilot, Codex, or a future repo agent can ask questions like:

- Which agent owns this file?
- Which review gate applies before changing a benchmark result?
- Which policy mitigates unsupported quantum-advantage claims?
- Which validation scripts must run before a contribution is proposed?
- Which docs define the agent workflow?

## 2. Delivered Files

| File | Purpose |
|---|---|
| `agent_team_governance_ontology.graphml` | Full GraphML ontology for the repo. |
| `AGENT_TEAM_ONTOLOGY.md` | Human-readable explanation of the ontology. |
| `ontology_nodes.csv` | Flat node inventory for auditing. |
| `ontology_edges.csv` | Flat relationship inventory for auditing. |
| `repo_agent_governance_matrix.md` | Agent ownership, review routing, and governance gates. |
| `ontology_manifest.json` | Machine-readable artifact manifest. |

## 3. Node Types

The GraphML uses the following major node types:

- `repository`
- `directory`
- `file`
- `agent_role`
- `principle`
- `workflow`
- `policy`
- `risk`
- `review_gate`

## 4. Edge Relationship Types

Important relationship types include:

- `contains`
- `owns`
- `requires_review_by`
- `defines`
- `defines_role`
- `governs`
- `depends_on`
- `mitigates`
- `enforces`
- `creates_plan_and_cards`
- `requires_baseline`
- `designs_qml_candidate`
- `implements_candidate`
- `evaluates_results`
- `reviews_claims`
- `routes_task`
- `reviews_packet`
- `runs_validation`
- `scores_contribution`

## 5. Recommended Agent Team

| Agent | Core Responsibility |
|---|---|
| RepoStewardAgent | Protects repo boundaries, small changes, no auto-merge/auto-run, dependency restraint, ontology integrity. |
| QMLResearcherAgent | Researches QML concepts, papers, official docs, uncertainty, and implementation-relevant facts. |
| QMLArchitectAgent | Designs QML experiment architecture, feature maps, ansatz choices, backends, and extension points. |
| ClassicalBaselineEngineer | Enforces classical baselines before QML candidates. |
| ExperimentEngineer | Implements small runnable scripts and examples. |
| EvaluatorAgent | Compares models under controlled conditions. |
| EthicsClaimsReviewer | Prevents unsupported quantum advantage claims and enforces limitations. |
| DocumentationAgent | Maintains README, docs, cards, reports, tooling maps, and checklists. |
| ContributionReviewerAgent | Scores contributions, reviews packets, and maintains reputation guidance. |
| TaskBoardCuratorAgent | Maintains task board, next-agent instructions, and task proposal workflow. |
| SchemaGuardianAgent | Maintains schemas, validation scripts, result fixtures, and machine-readable contracts. |
| MCPInterfaceAgent | Maintains the local command interface without uncontrolled automation. |
| SecuritySafetyAgent | Reviews secrets, external calls, dependency additions, and uncontrolled agent loops. |

## 6. Governance Interpretation

The repo has a strong governance spine:

```text
machine_index.json
  -> tells agents entrypoints, experiments, schemas

AGENT.md
  -> defines operating laws, roles, experiment workflow, PR checklist

TASK_BOARD.md + NEXT_AGENT_STEP.md
  -> route contributors into small tasks

agent_contributions/
  -> captures contribution packets before direct edits

scripts/validate_repo.py + benchmarks/runner.py + mcp/server.py
  -> validate benchmark/result state

docs/qml_claims_policy.md + docs/benchmark_methodology.md + docs/contribution_value_rubric.md
  -> enforce scientific honesty and review discipline

CONTRIBUTION_LOG.md
  -> records accepted/proposed/rejected/simulated contributions and reputation guidance
```

## 7. High-Risk Areas

The ontology marks these as high-governance areas:

- Benchmark result fixtures
- Benchmark runner
- Result schema
- Claims policy
- Contribution rubric
- Task board and next-agent flow
- MCP interface
- AGENT operating instructions
- Contribution log

Changes to these areas should trigger review by at least one governance agent and, when relevant, human review.

## 8. How to Use the GraphML

Python example:

```python
import networkx as nx

G = nx.read_graphml('agent_team_governance_ontology.graphml')

# Find files owned by the EthicsClaimsReviewer
owned = [
    target for source, target, data in G.edges(data=True)
    if source == 'agent:EthicsClaimsReviewer' and data.get('relationship') == 'owns'
]
print(owned)
```

Potential agent queries:

```text
Before editing examples/moons_quantum_kernel_comparison.py, which agents and review gates apply?
Which files mitigate unsupported quantum advantage claims?
Which tasks are governed by the TaskBoardCuratorAgent?
Which validation files depend on schemas/experiment_result.schema.json?
```

## 9. Next Improvements

1. Add this ontology to the repo under `ontology/agent_team_governance_ontology.graphml`.
2. Add an `ontology/README.md` explaining how agents should query it.
3. Add a small script `scripts/query_ontology.py` for common questions.
4. Generate a visual SVG/PNG from the GraphML.
5. Add repo CI or local validation that checks the ontology against known files.
6. Extend with import/dependency analysis from actual Python AST parsing.
7. Add PR-template hooks mapping touched files to required agents.
