# QML Agent Lab

**QML Agent Lab** is a lightweight agent operating system for designing, implementing, evaluating, and documenting quantum machine learning experiments in AI-assisted development workflows.

This repository is built for developers using Cursor, Codex, ChatGPT, or similar AI coding tools who want a reusable team of QML-aware agents.

The goal is not to claim quantum advantage. The goal is to make QML experimentation more disciplined, reproducible, and useful.

## Core Principle

Every QML experiment must include a classical baseline.

QML models should be compared against simple and strong classical methods before any claims are made.

## What This Repo Provides

- A reusable `AGENT.md` operating prompt for Cursor/Codex-style tools
- Specialized agent role files for QML development
- Templates for experiment plans, dataset cards, model cards, and comparison reports
- Starter Python examples for classical baselines, Qiskit Machine Learning, and PennyLane
- A functional Moons benchmark comparing a classical RBF SVM against a Qiskit quantum kernel SVM
- Verified benchmark results in Markdown and JSON formats
- A tooling map for choosing the right QML framework
- A sprint checklist for keeping development focused and publishable

## Agent Team

| Agent | Purpose |
|---|---|
| QML Researcher | Finds and summarizes relevant QML methods, papers, docs, and repos |
| QML Architect | Designs the QML approach, circuit structure, encoding, backend, and constraints |
| Classical Baseline Engineer | Builds classical ML baselines before QML models are evaluated |
| Experiment Engineer | Implements small, reproducible scripts and experiments |
| Evaluator | Checks metrics, leakage, reproducibility, and fair comparison |
| Ethics & Claims Reviewer | Prevents exaggerated claims and flags unsupported conclusions |
| Documentation Agent | Maintains README files, model cards, reports, and experiment notes |

## Default Workflow

1. Define the task.
2. Create a dataset card.
3. Build the classical baseline.
4. Build the QML candidate.
5. Evaluate both under the same conditions.
6. Write a QML model card.
7. Write a comparison report.
8. Review claims for accuracy and humility.
9. Commit only reproducible, well-documented work.

## Quickstart

Recommended Python version: **Python 3.10 or 3.11**.

Qiskit and PennyLane dependencies can change over time, so use a clean virtual environment for the most reliable results.

Clone the repo:

```bash
git clone https://github.com/Aggredicus/qml-agent-lab.git
cd qml-agent-lab
```

Create a Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the classical baseline first:

```bash
python examples/classical_baseline_stub.py
```

Then run the functional Moons comparison:

```bash
python examples/moons_quantum_kernel_comparison.py
```

Or try the smaller QML starter examples:

```bash
python examples/pennylane_qnode_stub.py
python examples/qiskit_quantum_kernel_stub.py
python examples/qiskit_qnn_stub.py
```

Each example is intentionally small and educational.

## Functional Benchmark: Moons Quantum Kernel Comparison

The first complete comparison script is:

```bash
python examples/moons_quantum_kernel_comparison.py
```

It compares:

| Model | Purpose |
|---|---|
| `StandardScaler + SVC(kernel='rbf')` | Classical nonlinear baseline |
| `FidelityQuantumKernel + SVC(kernel='precomputed')` | QML candidate using a Qiskit quantum feature map |

The script uses `sklearn.datasets.make_moons`, scales QML inputs into a gate-angle-friendly range, computes explicit train/test quantum kernel matrices, prints metrics, and includes a claim review.

This benchmark is useful for workflow testing and geometric intuition. It is not evidence of quantum advantage.

## Latest Benchmark Result

Current verified single-seed result:

| Model | Accuracy |
|---|---:|
| Classical RBF SVM | 0.900 |
| Qiskit quantum kernel SVM | 0.700 |

The classical baseline outperformed the initial QML candidate by 0.200 accuracy points on this toy setup.

Full results:

- `results/moons_quantum_kernel_comparison_2026-04-25.md`
- `results/moons_quantum_kernel_comparison_2026-04-25.json`

This result is educational and does not support claims of quantum advantage.

## Suggested Cursor Workflow

Open this repo in Cursor and use `AGENT.md` as the main operating instruction.

For a new experiment, ask Cursor:

```text
Using AGENT.md, create a new QML experiment plan for a small binary classification task. Start with the dataset card and classical baseline.
```

Then proceed incrementally:

```text
Now implement only the classical baseline.
```

```text
Now implement a QML candidate using the smallest reasonable circuit.
```

```text
Now evaluate both and write a comparison report.
```

## What This Repo Is Not

This repo is not:

- A full QML framework
- A production quantum computing platform
- A claim that QML beats classical ML
- A replacement for Qiskit, PennyLane, Cirq, TensorFlow Quantum, or Mitiq
- A large benchmark suite
- A cloud quantum hardware integration layer

This repo is a lightweight coordination layer for AI-assisted QML development.

## Current Framework Priorities

| Framework | Role |
|---|---|
| Qiskit Machine Learning | Quantum kernels, QNNs, Qiskit-native workflows |
| PennyLane | Differentiable hybrid quantum-classical experiments |
| scikit-learn | Classical baselines |
| NumPy | Small numerical examples |

## Future Roadmap

### v0.2.0 — Real Benchmark Runner

Add small reproducible benchmark scripts for:

- Iris
- Breast cancer dataset
- Tiny ecological toy dataset
- Seed-sweep reporting for Moons

### v0.3.0 — Report Generator

Generate Markdown reports from experiment JSON.

### v0.4.0 — Cursor Rules Pack

Add `.cursor/rules/` for reusable QML development rules.

### v0.5.0 — Quantum Geometry Visualizer

Visualize classical feature spaces, quantum feature maps, kernel matrices, and embedding similarities.

## Release Philosophy

Small is good.

A useful QML repo should make experiments:

- Easier to repeat
- Easier to compare
- Easier to document
- Easier to review honestly
- Easier for AI agents to extend

## License

MIT License.
