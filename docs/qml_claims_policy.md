# QML Claims Policy

This repository is baseline-first and evidence-first.

## Allowed Claims

Contributors may say:

- A result is educational.
- A model underperforms, matches, or outperforms a recorded baseline on a specific benchmark fixture.
- A result suggests a direction for further testing.
- A benchmark is inconclusive.

## Disallowed Claims

Contributors may not claim:

- Quantum advantage without repeated, controlled evidence.
- General QML superiority from a small dataset.
- Production readiness from a toy benchmark.
- Scientific significance without documented limitations.

## Required Context

Every benchmark result must include:

- Classical baseline
- Quantum result if available
- Delta vs classical baseline
- Claim status
- Limitations

## Claim Status Values

| Status | Meaning |
|---|---|
| `quantum_underperforms` | Quantum model performed worse than classical baseline. |
| `quantum_matches_classical` | Quantum model matched classical baseline within reported precision. |
| `quantum_outperforms_classical` | Quantum model exceeded classical baseline on this benchmark only. |
| `quantum_not_run` | Only the classical baseline was run. |
| `inconclusive` | Result is not strong enough to classify. |

## Review Rule

If a claim sounds stronger than the data, weaken the claim.
