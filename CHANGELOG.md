# Changelog

All notable changes to this project will be documented in this file.

This project uses simple semantic versioning.

## [0.1.2] - 2026-04-25

### Added

- Added `examples/moons_quantum_kernel_comparison.py` as the first functional classical-vs-QML benchmark.
- Documented the Moons benchmark in the README.

### Notes

The Moons benchmark compares a classical RBF SVM against a Qiskit `FidelityQuantumKernel` with an explicit precomputed-kernel SVC workflow.

This remains an educational benchmark and is not evidence of quantum advantage.

## [0.1.1] - 2026-04-25

### Added

- Added `VERSION` file.
- Added `CHANGELOG.md`.
- Added `examples/classical_baseline_stub.py` as a minimal scikit-learn baseline example.
- Added Python version guidance to the README.

### Changed

- Updated README quickstart to include the real GitHub clone URL.
- Expanded quickstart guidance to recommend running the classical baseline before QML examples.

### Notes

This release keeps the repo intentionally lightweight. It does not add CI, package metadata, Docker, notebooks, or cloud integrations.

## [0.1.0] - 2026-04-25

### Added

- Initial `README.md`.
- Initial `AGENT.md` for Cursor/Codex-style QML development.
- Agent role documents for research, architecture, baselines, engineering, evaluation, claims review, and documentation.
- Reusable templates for experiment plans, dataset cards, QML model cards, and comparison reports.
- QML tooling map.
- Sprint checklist.
- Starter examples for PennyLane, Qiskit QNNs, and Qiskit quantum kernels.
- MIT License.
