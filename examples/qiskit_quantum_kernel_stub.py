"""
qiskit_quantum_kernel_stub.py

Educational starter example for comparing a classical SVC baseline
with the intended structure of a Qiskit quantum kernel classifier.

This script is intentionally small.

It is not evidence of quantum advantage.
"""

from __future__ import annotations


def main() -> None:
    try:
        import numpy as np
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVC
        from sklearn.metrics import accuracy_score

        from qiskit.circuit.library import ZZFeatureMap
        from qiskit_machine_learning.kernels import FidelityQuantumKernel
    except ImportError as exc:
        print("Missing dependency:", exc)
        print()
        print("Install dependencies with:")
        print("  pip install -r requirements.txt")
        print()
        print("This example requires:")
        print("  numpy")
        print("  scikit-learn")
        print("  qiskit")
        print("  qiskit-machine-learning")
        return

    random_seed = 42

    # Tiny toy dataset.
    # Keep feature count small because feature dimensions map naturally to qubits.
    X, y = make_classification(
        n_samples=40,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=random_seed,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=random_seed,
        stratify=y,
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Classical baseline.
    classical_model = SVC(kernel="rbf", random_state=random_seed)
    classical_model.fit(X_train, y_train)
    classical_predictions = classical_model.predict(X_test)
    classical_accuracy = accuracy_score(y_test, classical_predictions)

    print("Classical baseline")
    print("------------------")
    print("Model: SVC(kernel='rbf')")
    print(f"Accuracy: {classical_accuracy:.3f}")
    print()

    # Quantum kernel candidate.
    # This is a small educational example using a two-feature map.
    feature_map = ZZFeatureMap(feature_dimension=2, reps=1)

    quantum_kernel = FidelityQuantumKernel(feature_map=feature_map)

    # scikit-learn SVC can consume a callable kernel.
    qsvc = SVC(kernel=quantum_kernel.evaluate)
    qsvc.fit(X_train, y_train)
    quantum_predictions = qsvc.predict(X_test)
    quantum_accuracy = accuracy_score(y_test, quantum_predictions)

    print("QML candidate")
    print("-------------")
    print("Method: FidelityQuantumKernel + SVC")
    print("Feature map: ZZFeatureMap(feature_dimension=2, reps=1)")
    print("Backend: default local simulation behavior from Qiskit primitives")
    print("Qubits: 2")
    print(f"Accuracy: {quantum_accuracy:.3f}")
    print()

    print("Claim review")
    print("------------")
    print("This is an educational toy comparison.")
    print("It is not evidence of quantum advantage.")
    print("Repeat with stronger baselines, more seeds, and real datasets before making claims.")


if __name__ == "__main__":
    main()
