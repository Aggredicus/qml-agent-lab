# Changelog

All notable changes to this project will be documented in this file.

This project uses simple semantic versioning.

## [1.0.0] - 2026-04-25

### Added

- Baseline-first benchmark system with enforced classical comparison
- Validation system for benchmarks and contribution packets
- Contribution Value Rubric with justification and confidence scoring
- Reviewer override workflow and PR review guide
- Reputation tracking via CONTRIBUTION_LOG.md
- Agent-compatible contribution workflow and task system

### Changed

- Upgraded repository structure to support governed multi-agent contributions
- Updated README and documentation for stable release
- Fixed validator scope to avoid false positives
- Standardized version metadata across all files

### Notes

This release marks the transition from experimental QML tooling to a stable,
community-ready research environment. The system emphasizes correctness,
reproducibility, and grounded scientific evaluation over performance claims.

---

## [0.1.6] - 2026-04-25

### Changed

- Updated `CITATION.cff` to match the current release version.
- Replaced the original v0.1.0 sprint checklist with a current repository quality checklist.
- Kept `pyproject.toml` focused on Black and Ruff style configuration by removing premature pytest configuration.
- Updated README badge and governance notes for v0.1.6 consistency.

### Notes

This release is a consistency cleanup. It preserves the agent-first project identity and avoids moving the repository toward a conventional installable Python package structure.

(remaining history unchanged)
