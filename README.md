# QML Agent Lab

**Agent-first research environment for Quantum Machine Learning (QML).**

This repository enables **human developers and AI agents** to collaboratively explore QML with:

- reproducible benchmarks  
- enforced classical baselines  
- honest performance reporting  
- structured contribution workflows  
- ontology-aware agent governance  
- grounded evaluation and reputation tracking

---

## 🧠 Core Principle

> Every QML experiment must include a classical baseline.

This repository explicitly avoids hype and unsupported claims.

---

## 🔬 Verified Benchmarks

### Moons Dataset
- Classical RBF SVM: **0.900**
- Qiskit Quantum Kernel SVM: **0.700**
- Result: **Quantum underperforms**

### Iris (versicolor vs virginica)
- Classical RBF SVM: **0.880**
- Qiskit Quantum Kernel SVM: **0.600**
- Result: **Quantum underperforms**

---

## ⚠️ Interpretation

- QML does **not automatically outperform** classical ML
- Small datasets are insufficient to claim advantage
- Honest benchmarking is required for progress

---

## 🧩 Repository Structure

```
agents/                 → agent role definitions
templates/              → reusable experiment templates
examples/               → runnable QML + classical scripts
benchmarks/             → verified result fixtures
mcp/                    → local agent command interface
agent_contributions/    → structured contribution packets
scripts/                → validation + helper tools
ontology/               → GraphML governance ontology + inventories

docs/                   → governance, rubric, and review systems

TASK_BOARD.md           → Kanban system
NEXT_AGENT_STEP.md      → next-step prompt for agents
AGENT.md                → full agent operating instructions
CONTRIBUTION_LOG.md     → project memory + reputation tracking
```

---

## 🕸️ Ontology-Aware Governance

Version `v1.1` adds a GraphML governance ontology that maps:

- files and folders,
- agent roles,
- owner agents,
- review gates,
- risks,
- workflows,
- policies,
- validation paths.

Agents should query the ontology before modifying governed files:

```bash
python scripts/query_ontology.py file benchmarks/results/moons_baseline.json
python scripts/query_ontology.py reviewers examples/iris_quantum_kernel_comparison.py
python scripts/query_ontology.py gates benchmarks/results/iris_baseline.json
```

The ontology is a routing and governance map. It does not replace human judgment.

---

## 🔁 Contribution Loop

```
Contributor or Agent arrives
→ Reads instructions
→ Queries ontology for touched files
→ Selects task
→ Creates contribution packet
→ Runs validation scripts
→ Submits PR with rubric self-assessment
→ Human or agent reviewer assigns score
→ Reputation updated in contribution log
→ System evolves
```

---

## 🧪 Validation

Run locally:

```bash
python scripts/validate_repo.py
python scripts/validate_ontology.py
```

These checks cover:

- benchmark schema correctness
- claim status alignment
- contribution packet structure
- ontology GraphML/CSV/manifest consistency
- high-risk file ownership and review routing

Optional safe read-only result inspection:

```bash
python mcp/server.py get_results
```

---

## 📊 Benchmark Rules

All results must include:

- classical baseline
- quantum model (if present)
- delta vs classical
- claim status
- limitations

---

## 🧠 Contribution Evaluation System

Each PR must include:

- rubric-based self-assessment
- ontology review for changed files
- justification for scores
- confidence level

Reviewers:

- assign adjusted score
- may override contributor score
- update reputation in `CONTRIBUTION_LOG.md`

---

## 🛑 Guardrails

- No auto-merge
- No automatic expensive benchmark execution
- No unsupported quantum advantage claims
- No large unreviewed changes
- No missing baselines
- Query the ontology before changing high-risk files

---

## 🏁 Current Status

```
Version: v1.1.0
State: Ontology-aware governance branch
Ready for: Pull request review
```

---

## 🧠 Final Note

If you are a contributor or agent:

> Make the smallest useful improvement.  
> Query the ontology before touching governed files.  
> Report honestly.  
> Justify your reasoning.  
> Leave the system better than you found it.
