# QML Agent Lab

**Agent-first research environment for Quantum Machine Learning (QML).**

This repository enables **human developers and AI agents** to collaboratively explore QML with:

- reproducible benchmarks  
- enforced classical baselines  
- honest performance reporting  
- structured contribution workflows  
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

docs/                   → governance, rubric, and review systems

TASK_BOARD.md           → Kanban system
NEXT_AGENT_STEP.md      → next-step prompt for agents
AGENT.md                → full agent operating instructions
CONTRIBUTION_LOG.md     → project memory + reputation tracking
```

---

## 🔁 Contribution Loop

```
Contributor or Agent arrives
→ Reads instructions
→ Selects task
→ Creates contribution packet
→ Runs validation script
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
```

This checks:

- benchmark schema correctness
- claim status alignment
- contribution packet structure

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
- justification for scores
- confidence level

Reviewers:

- assign adjusted score
- may override contributor score
- update reputation in `CONTRIBUTION_LOG.md`

---

## 🛑 Guardrails

- No auto-merge
- No auto-run benchmarks
- No unsupported quantum advantage claims
- No large unreviewed changes
- No missing baselines

---

## 🏁 Current Status

```
Version: v1.0.0
State: Stable, community-ready
Ready for: Human + agent collaborative research
```

---

## 🧠 Final Note

If you are a contributor or agent:

> Make the smallest useful improvement.  
> Report honestly.  
> Justify your reasoning.  
> Leave the system better than you found it.
