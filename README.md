# QML Agent Lab

**Agent-first research environment for Quantum Machine Learning (QML).**

This repository enables **human developers and AI agents** to collaboratively explore QML with:

- reproducible benchmarks  
- enforced classical baselines  
- honest performance reporting  
- structured contribution workflows  

---

## 🧠 Core Principle

> Every QML experiment must include a classical baseline.

This repository explicitly avoids hype and unsupported claims.

---

## 🔬 Verified Benchmarks (v0.3.0)

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
tasks/                  → executable task definitions

TASK_BOARD.md           → Kanban system
NEXT_AGENT_STEP.md      → next-step prompt for agents
AGENT.md                → full agent operating instructions
RELEASE_CHECKLIST.md    → release validation checklist
```

---

## 🤖 Agent Entry Point

If you are an AI agent:

1. Read:
   - `machine_index.json`
   - `AGENT.md`
   - `TASK_BOARD.md`
   - `NEXT_AGENT_STEP.md`

2. Select one small task

3. Create a contribution packet in:
```
agent_contributions/
```

4. Submit a pull request

---

## 🔁 Contribution Loop

```
Agent arrives
→ Reads instructions
→ Selects task
→ Creates contribution packet
→ Submits PR
→ Human review
→ System evolves
```

---

## 🧪 MCP Interface

Run locally:

```bash
python mcp/server.py list_experiments
python mcp/server.py run_experiment moons
```

This interface is:
- deterministic
- safe
- non-executing (no heavy compute)

---

## 📊 Benchmark Rules

All results must include:
- classical baseline
- quantum model (if present)
- delta vs classical
- claim status
- limitations

---

## 🧠 Claim Status System

| Status | Meaning |
|------|--------|
| quantum_underperforms | Worse than baseline |
| quantum_matches_classical | Equivalent |
| quantum_outperforms_classical | Better |
| quantum_not_run | Baseline only |

---

## 🛑 Guardrails

- No auto-merge
- No auto-run benchmarks
- No unsupported quantum advantage claims
- No large unreviewed changes
- No missing baselines

---

## 🗺️ Roadmap

- Expand benchmark suite
- Add controlled QML experiments
- Build leaderboard visualization
- Introduce contribution reputation system
- Enable structured agent participation at scale

---

## 🏁 Current Status

```
Version: v0.3.0
State: Stable, pre-1.0
Ready for: Controlled agent contribution
```

---

## 🧠 Final Note

If you are an agent:

> Make the smallest useful improvement.  
> Report honestly.  
> Leave the system better than you found it.
