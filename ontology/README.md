# Agent Team Governance Ontology

This folder contains the machine-readable governance ontology for `qml-agent-lab`.

The ontology describes the repository as a graph of files, folders, agent roles, review gates, risks, workflows, policies, benchmark artifacts, validation scripts, and ownership boundaries. It is meant to help human contributors and AI agents make small, evidence-aligned, reviewable changes.

The core rule remains:

> Every QML experiment must include a classical baseline.

## Files

| File | Purpose |
|---|---|
| `agent_team_governance_ontology.graphml` | Full GraphML graph of repository governance relationships. |
| `AGENT_TEAM_ONTOLOGY.md` | Human-readable overview of the ontology. |
| `repo_agent_governance_matrix.md` | Agent ownership and review-routing matrix. |
| `ontology_nodes.csv` | Flat inventory of ontology nodes for auditing. |
| `ontology_edges.csv` | Flat inventory of ontology edges for auditing. |
| `ontology_manifest.json` | Manifest with expected graph counts and source limitations. |

## Why GraphML?

GraphML is portable, text-based, version-control friendly, and readable by common graph tools. It lets the repo represent governance as data instead of leaving it only in prose.

That makes questions like these machine-answerable:

- Which agent owns this file?
- Which review gates apply to a benchmark fixture?
- Which risks are associated with a claims-policy change?
- Which validation scripts should run before a PR?
- Which files are high-risk or require review?

## Node Types

The ontology includes nodes such as:

- `repository`
- `directory`
- `file`
- `agent_role`
- `principle`
- `workflow`
- `policy`
- `risk`
- `review_gate`

## Relationship Types

Important edge relationships include:

- `contains`
- `owns`
- `requires_review_by`
- `defines`
- `defines_role`
- `governs`
- `depends_on`
- `mitigates`
- `enforces`
- `requires_baseline`
- `designs_qml_candidate`
- `implements_candidate`
- `evaluates_results`
- `reviews_claims`
- `routes_task`
- `reviews_packet`
- `runs_validation`
- `scores_contribution`

## How Agents Should Use This

Before modifying a file, agents should query the ontology to identify:

1. the owner agent,
2. required reviewers,
3. review gates,
4. related risks,
5. validation expectations.

Example:

```bash
python scripts/query_ontology.py file benchmarks/results/moons_baseline.json
python scripts/query_ontology.py reviewers examples/iris_quantum_kernel_comparison.py
python scripts/query_ontology.py gates benchmarks/results/iris_baseline.json
```

If a file is high-risk or `review_required=true`, keep the change small and request review from the relevant agent role or human maintainer.

## How Humans Can Use This

Human reviewers can use the ontology to check whether a PR has routed itself through the right governance path.

For example, a PR that changes `benchmarks/results/*` should trigger review concerns around:

- baseline integrity,
- reproducibility,
- claim discipline,
- schema validation,
- benchmark gaming.

## Query Examples

```bash
python scripts/query_ontology.py summary
python scripts/query_ontology.py file benchmarks/results/moons_baseline.json
python scripts/query_ontology.py agent EthicsClaimsReviewer
python scripts/query_ontology.py risks examples/moons_quantum_kernel_comparison.py
python scripts/query_ontology.py gates benchmarks/results/iris_baseline.json
python scripts/query_ontology.py reviewers examples/iris_quantum_kernel_comparison.py
python scripts/query_ontology.py owners AGENT.md
```

## Validation

Run:

```bash
python scripts/validate_ontology.py
```

The validator checks that:

- GraphML, CSV, and manifest files exist,
- GraphML parses successfully,
- manifest counts match GraphML counts,
- CSV counts match manifest counts,
- CSV edge endpoints exist in the node inventory,
- high-risk file nodes have owners,
- high-risk file nodes require review,
- benchmark result files are governed by evaluator review,
- governance files require review.

## Extending the Ontology

Future ontology versions can add:

- Python import edges,
- function-level dependencies,
- script input/output relationships,
- JSON schema field usage,
- benchmark result provenance,
- test coverage relationships,
- PR-template routing checks.

The current ontology is a governance ontology, not a complete AST/import dependency graph.

## v1.1 Scope

`v1.1` keeps one bundled GraphML file as the stable query target.

This is intentional. A single bundled ontology is easier to validate, hash, query, and review while the repository establishes ontology-aware editing as a normal workflow.

For `v1.1`, do not split the ontology into multiple GraphML modules unless a human maintainer explicitly requests that scope change.

## v1.2 Modular Ontology Roadmap

A future `v1.2` branch may introduce modular GraphML source files while continuing to generate one bundled GraphML artifact for query tools.

A likely structure is:

```text
ontology/modules/
  00_repo.graphml
  01_files_and_directories.graphml
  02_agents.graphml
  03_principles.graphml
  04_workflows.graphml
  05_risks.graphml
  06_review_gates.graphml
  07_ownership.graphml
  08_policy_links.graphml
  09_benchmark_governance.graphml
  10_validation_links.graphml
```

Expected v1.2 tooling:

- `scripts/build_ontology_bundle.py` to merge modules into `agent_team_governance_ontology.graphml`,
- module-aware validation for duplicate IDs and orphan edges,
- generated CSV inventories from the merged graph,
- manifest-controlled merge order,
- per-module ownership and review routing.

The design goal for v1.2 should be:

> Small modular GraphML files are the editable source. The bundled GraphML, CSV inventories, and manifest are generated audit/query artifacts.

## Regeneration Guidance

When the repo structure changes significantly:

1. update `ontology_nodes.csv`,
2. update `ontology_edges.csv`,
3. regenerate `agent_team_governance_ontology.graphml`,
4. update `ontology_manifest.json`,
5. run `python scripts/validate_ontology.py`,
6. document the ontology change in the PR.

Do not let the ontology become an unreviewed authority. It is a routing and governance map that supports human judgment.
