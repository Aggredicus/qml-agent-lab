# Citation and Reasoning System

## Purpose

This system ensures that all reasoning in QML Agent Lab is:

- traceable
- evidence-based
- reviewable by humans and agents

---

## Citation Format

Use source IDs from `docs/SOURCE_REGISTRY.md`:

Example:

```
Quantum kernels can be simulated classically [SRC-001].
```

---

## Reasoning Trace Format

Every non-trivial decision should include:

```
Decision:

Evidence:
- [SRC-XXX]

Conclusion:
```

---

## Good Example

```
Decision: Use RBF SVM baseline

Evidence:
- [SRC-002] shows SVMs are strong general-purpose classifiers

Conclusion:
RBF SVM is a reasonable classical comparator
```

---

## Bad Example

```
Decision: Use RBF SVM

Reason: It works well
```

---

## Rules

- Only cite sources that directly support your claim
- Do not invent sources
- Do not cite without using the source in reasoning
- Prefer primary sources and official documentation

---

## Goal

Make all reasoning transparent, auditable, and reproducible.
