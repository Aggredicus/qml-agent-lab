# QML Experiment Plan

## Experiment Name

`name_here`

## Date

`YYYY-MM-DD`

## Author / Agent

`name_or_agent_here`

## Goal

Describe the question this experiment is trying to answer.

Example:

> Compare a classical SVM baseline against a quantum kernel classifier on a small binary classification dataset.

## Task Type

- [ ] Classification
- [ ] Regression
- [ ] Clustering
- [ ] Embedding / feature map comparison
- [ ] Other: `describe`

## Dataset

Dataset name:

Dataset source:

Dataset size:

Number of features:

Target variable:

Known limitations:

## Hypothesis

Write a modest hypothesis.

Example:

> A quantum feature map may produce a different kernel geometry than the classical baseline, but this experiment is educational and not evidence of quantum advantage.

## Classical Baseline

Model:

Preprocessing:

Metrics:

Random seed:

Expected output:

## QML Candidate

Framework:

- [ ] Qiskit Machine Learning
- [ ] PennyLane
- [ ] Other: `describe`

Method:

- [ ] Quantum kernel
- [ ] QNN
- [ ] Variational circuit
- [ ] Hybrid quantum-classical layer
- [ ] Other: `describe`

Encoding / feature map:

Ansatz:

Backend or simulator:

Qubits:

Shots:

Circuit depth, if known:

Optimizer, if applicable:

## Evaluation Plan

Train/test split:

Metrics:

Number of runs:

Random seeds:

Comparison method:

## Reproducibility Notes

Environment:

Dependencies:

Hardware:

Simulator:

Known sources of randomness:

## Claim Strength

Choose one:

- [ ] Educational
- [ ] Experimental
- [ ] Competitive
- [ ] Promising
- [ ] Strong evidence

## Limitations

- Limitation 1
- Limitation 2
- Limitation 3

## Next Steps

- [ ] Build dataset card
- [ ] Implement classical baseline
- [ ] Implement QML candidate
- [ ] Evaluate results
- [ ] Write model card
- [ ] Run claims review
