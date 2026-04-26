# Source Registry

This registry assigns stable source IDs for documents, papers, documentation, and code references used in QML Agent Lab reasoning.

Use these IDs in pull requests, contribution packets, documentation, and agent reasoning traces.

---

## SRC-001

Title: Qiskit Documentation
Type: documentation
Author: IBM Quantum
Year: 2026
URL: https://docs.quantum.ibm.com/
License: Apache-2.0 for Qiskit code; documentation license may vary
Summary: Official documentation for Qiskit, IBM's open-source SDK for quantum circuits, primitives, operators, transpilation, and quantum workflow development.

---

## SRC-002

Title: Support-vector networks
Type: academic
Author: Cortes, C.; Vapnik, V.
Year: 1995
URL: https://link.springer.com/article/10.1007/BF00994018
License: Publisher controlled
Summary: Foundational support vector machine paper. Useful for justifying classical SVM baselines.

---

## SRC-003

Title: Quantum machine learning
Type: academic
Author: Biamonte, J.; Wittek, P.; Pancotti, N.; Rebentrost, P.; Wiebe, N.; Lloyd, S.
Year: 2017
URL: https://www.nature.com/articles/nature23474
License: Publisher controlled
Summary: Review article on quantum machine learning concepts, opportunities, and limitations.

---

## SRC-004

Title: PennyLane Documentation
Type: documentation
Author: Xanadu
Year: 2026
URL: https://docs.pennylane.ai/
License: Apache-2.0 for PennyLane code; documentation license may vary
Summary: Official documentation for PennyLane, a Python framework for differentiable programming of quantum computers.

---

## SRC-005

Title: scikit-learn User Guide
Type: documentation
Author: scikit-learn developers
Year: 2026
URL: https://scikit-learn.org/stable/user_guide.html
License: BSD-3-Clause for scikit-learn code; documentation license may vary
Summary: Official documentation for classical ML models, preprocessing, validation, datasets, and metrics used as baseline references.

---

## Future Source Format

Use this format for new entries:

```text
## SRC-XXX

Title:
Type: documentation | academic | article | code | dataset | other
Author:
Year:
URL:
License:
Summary:
```

## Rules

- Do not invent source IDs.
- Prefer official documentation for tool behavior.
- Prefer primary literature for scientific claims.
- Use source IDs only when the source directly supports the claim or decision.
