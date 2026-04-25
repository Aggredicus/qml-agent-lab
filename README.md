# QML Agent Lab

![Version](https://img.shields.io/badge/version-0.1.5-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-experimental-orange)

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
- Functional Moons and Iris benchmarks comparing classical RBF SVMs against Qiskit quantum kernel SVMs
- Verified benchmark results in Markdown and JSON formats
- Open-source project hygiene files for contribution, citation, conduct, security, and Python style conventions
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

Then run the functional benchmark examples:

```bash
python examples/moons_quantum_kernel_comparison.py
python examples/iris_quantum_kernel_comparison.py
```

Or try the smaller QML starter examples:

```bash
python examples/pennylane_qnode_stub.py
python examples/qiskit_quantum_kernel_stub.py
python examples/qiskit_qnn_stub.py
```

Each example is intentionally small and educational.

## Functional Benchmarks

### Moons Quantum Kernel Comparison

```bash
python examples/moons_quantum_kernel_comparison.py
```

| Model | Accuracy |
|---|---:|
| Classical RBF SVM | 0.900 |
| Qiskit quantum kernel SVM | 0.700 |

Full results:

- `results/moons_quantum_kernel_comparison_2026-04-25.md`
- `results/moons_quantum_kernel_comparison_2026-04-25.json`

### Iris Quantum Kernel Comparison

```bash
python examples/iris_quantum_kernel_comparison.py
```

This benchmark uses the harder binary Iris subset: `versicolor` vs `virginica`, with petal length and petal width as the two features.

| Model | Accuracy |
|---|---:|
| Classical RBF SVM | 0.880 |
| Qiskit quantum kernel SVM | 0.600 |

Full results:

- `results/iris_quantum_kernel_comparison_2026-04-25.md`
- `results/iris_quantum_kernel_comparison_2026-04-25.json`

These results are educational and do not support claims of quantum advantage.

## Project Governance and Style

This project includes standard open-source hygiene files:

| File | Purpose |
|---|---|
| `CONTRIBUTING.md` | Contribution workflow and experiment standards |
| `CODE_OF_CONDUCT.md` | Community and scientific-integrity expectations |
| `SECURITY.md` | Security and AI-agent safety notes |
| `CITATION.cff` | Citation metadata for research-adjacent reuse |
| `pyproject.toml` | Black, Ruff, and pytest style configuration |

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

- Breast cancer dataset
- Tiny ecological toy dataset
- Seed-sweep reporting for Moons and Iris

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
