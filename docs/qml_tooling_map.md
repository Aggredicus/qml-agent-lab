# QML Tooling Map

This document summarizes the main tools currently relevant to this repository.

The purpose is to help agents choose the smallest appropriate framework for each experiment.

## Tooling Philosophy

Use the lightest tool that can answer the research question.

Do not add a framework just because it is interesting.

Every QML experiment must include a classical baseline.

## Qiskit Machine Learning

### Best For

- Quantum kernels
- Quantum support vector classifiers
- Quantum neural networks
- Qiskit-native workflows
- Educational QML examples
- IBM Quantum ecosystem compatibility

### Useful Concepts

- Quantum kernels
- Fidelity quantum kernels
- Variational quantum classifiers
- EstimatorQNN
- SamplerQNN
- TorchConnector

### Use When

- The experiment needs a Qiskit-native implementation
- The task is a small classification or regression example
- You want to compare classical SVMs with quantum kernel methods
- You want to build QNN examples within the Qiskit ecosystem

### Avoid When

- Dependency simplicity is the highest priority
- The experiment does not need quantum circuits
- A classical baseline has not been built yet

## PennyLane

### Best For

- Differentiable quantum programming
- Hybrid quantum-classical workflows
- QNodes
- PyTorch/JAX-style integration
- Variational circuits
- Fast educational experiments

### Useful Concepts

- QNode
- Devices
- Differentiable circuits
- Parameterized gates
- Hybrid optimization

### Use When

- You want a compact hybrid circuit example
- You want differentiable quantum layers
- You are exploring variational circuits
- You want an elegant educational example

### Avoid When

- The experiment specifically requires Qiskit Machine Learning
- You need Qiskit-native backend behavior
- You are not ready to manage hybrid optimization details

## TensorFlow Quantum

### Best For

- TensorFlow + Cirq-based QML workflows
- Research environments already using TensorFlow
- Hybrid quantum-classical neural network experiments

### Use Later Because

TensorFlow Quantum can be powerful, but it brings heavier dependency constraints than this repo needs in sprint one.

It is not a default dependency.

### Use When

- A future experiment specifically requires TensorFlow or Cirq
- The development environment can support the required versions
- The team intentionally chooses a TensorFlow-native stack

## Mitiq

### Best For

- Quantum error mitigation
- Zero-noise extrapolation
- Probabilistic error cancellation
- Clifford data regression
- Noisy intermediate-scale quantum experiments

### Use Later Because

Sprint one focuses on agent protocols and minimal examples.

Mitiq is a future extension for experiments involving noise, real hardware, or error mitigation.

### Use When

- The experiment involves noisy circuits
- Error mitigation is part of the research question
- Backend noise affects interpretation

## Classical ML Baselines

### Required For Every Experiment

Use scikit-learn first.

Recommended baseline models:

Classification:

- Logistic regression
- SVM
- Random forest
- k-nearest neighbors

Regression:

- Linear regression
- Ridge regression
- Random forest regressor
- SVR

Clustering:

- K-means
- Gaussian mixture model

## Framework Selection Guide

| Goal | Recommended Tool |
|---|---|
| Simple baseline | scikit-learn |
| Quantum kernel classifier | Qiskit Machine Learning |
| QNN in Qiskit ecosystem | Qiskit Machine Learning |
| Differentiable variational circuit | PennyLane |
| TensorFlow/Cirq research | TensorFlow Quantum |
| Error mitigation | Mitiq |
| Production experiment discipline | MLOps templates + reports |

## Minimum Experiment Standard

Every experiment should record:

- Dataset
- Task
- Classical baseline
- QML method
- Metrics
- Random seed
- Qubits
- Shots
- Backend or simulator
- Circuit depth if available
- Limitations
- Claim strength

## Final Rule

If a classical model solves the problem well, the QML model must still justify its existence through insight, geometry, interpretability, educational value, or experimental comparison.

Do not use QML as decoration.
