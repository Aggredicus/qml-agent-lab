# Security Policy

## Supported Versions

QML Agent Lab is an early-stage experimental research toolkit.

The current supported version is listed in `VERSION`.

## Security Scope

This repository contains local educational scripts, documentation, templates, and agent instructions for quantum machine learning experiments.

It does not intentionally include:

- hosted services,
- cloud credentials,
- production APIs,
- authentication systems,
- payment systems,
- private datasets, or
- hardware quantum credentials.

## Responsible Use

When using this repository:

- Do not commit API keys, tokens, secrets, or credentials.
- Do not run generated code from agents without review.
- Do not upload private datasets without permission.
- Do not use toy educational benchmark results for high-stakes decisions.
- Do not claim production readiness unless production controls are added.

## Reporting a Vulnerability

If you discover a security issue, please open a GitHub issue with a concise description unless the issue involves sensitive information.

For sensitive issues, contact the repository owner through the most appropriate private channel available on GitHub.

## AI-Agent Safety Notes

This project is designed for use with AI coding agents.

Agents should:

- avoid executing untrusted code automatically,
- avoid adding network calls unless explicitly requested,
- avoid adding credential handling without review,
- keep experiments local by default,
- document any new external dependency,
- flag potentially unsafe or misleading workflows.

## Scientific Safety Notes

Misleading claims can also be a form of harm.

QML Agent Lab requires:

- classical baselines,
- documented limitations,
- modest claims,
- reproducible results where possible,
- explicit distinction between toy benchmarks and real-world evidence.

Do not describe educational QML results as quantum advantage.
