# Changelog

All notable changes to this project will be documented in this file.

This project uses simple semantic versioning.

## [0.1.5] - 2026-04-25

### Added

- Added `examples/iris_quantum_kernel_comparison.py` as the second functional classical-vs-QML benchmark.
- Added verified Iris benchmark result report in Markdown.
- Added machine-readable Iris benchmark result record in JSON.
- Updated README benchmark section to summarize both Moons and Iris results.

### Notes

The Iris benchmark uses the harder `versicolor` vs `virginica` binary subset with petal length and petal width as features.

The classical RBF SVM outperformed the initial Qiskit quantum kernel SVM on the single-seed Iris benchmark.

This result is useful for honest benchmark discipline and does not support claims of quantum advantage.

## [0.1.4] - 2026-04-25

### Added

- Added `CONTRIBUTING.md` with contribution standards and experiment checklist.
- Added `SECURITY.md` with local-use, credential, and AI-agent safety guidance.
- Added `CODE_OF_CONDUCT.md` with community and scientific-integrity expectations.
- Added `CITATION.cff` for research-adjacent citation metadata.
- Added `pyproject.toml` with Black, Ruff, and pytest style configuration.
- Added README badges and a project governance/style section.

### Notes

This release improves open-source project hygiene and makes the repository look more professional to contributors, reviewers, and future AI coding agents.

## [0.1.3] - 2026-04-25

### Added

- Added verified Moons benchmark result report in Markdown.
- Added machine-readable Moons benchmark result record in JSON.
- Added README summary of the first measured classical-vs-QML result.

### Notes

The classical RBF SVM outperformed the initial Qiskit quantum kernel SVM on the single-seed Moons benchmark.

This result is useful for honest benchmark discipline and does not support claims of quantum advantage.

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
