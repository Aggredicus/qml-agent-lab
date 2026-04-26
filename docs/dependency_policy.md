# Dependency Policy

Keep the repository lightweight and reproducible.

## Rules

- Prefer standard Python libraries.
- Avoid adding heavy frameworks unless justified.
- Document all dependencies in the file that uses them.
- Provide graceful failure if dependency is missing.

## QML-Specific

- Qiskit and PennyLane are allowed but optional.
- Do not require cloud access.
- Avoid GPU-only dependencies.

## Review Criteria

A dependency may be rejected if:

- It significantly increases install complexity
- It is not necessary for the task
- It introduces hidden execution behavior

## Principle

Every dependency must justify its existence.
