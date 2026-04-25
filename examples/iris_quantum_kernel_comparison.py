"""
iris_quantum_kernel_comparison.py

Functional QML Agent Lab example comparing:

1. A classical RBF-kernel SVC baseline
2. A Qiskit FidelityQuantumKernel + precomputed-kernel SVC candidate

Dataset: scikit-learn Iris
Task: binary classification using versicolor vs virginica
Features: petal length and petal width

This is an educational benchmark. It is not evidence of quantum advantage.
"""

from __future__ import annotations


def main() -> None:
    try:
        import numpy as np
        from sklearn.datasets import load_iris
        from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import MinMaxScaler, StandardScaler
        from sklearn.svm import SVC

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

    iris = load_iris()

    # Use a nontrivial binary Iris subset.
    # Class IDs: 1 = versicolor, 2 = virginica.
    # Feature IDs: 2 = petal length, 3 = petal width.
    class_ids = (1, 2)
    feature_ids = (2, 3)
    class_mask = np.isin(iris.target, class_ids)

    X = iris.data[class_mask][:, feature_ids]
    y_raw = iris.target[class_mask]
    y = (y_raw == class_ids[1]).astype(int)

    class_names = [str(iris.target_names[class_ids[0]]), str(iris.target_names[class_ids[1]])]
    feature_names = [str(iris.feature_names[i]) for i in feature_ids]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=random_seed,
        stratify=y,
    )

    # Classical baseline: strong, simple, and appropriate for small nonlinear data.
    classical_model = make_pipeline(
        StandardScaler(),
        SVC(kernel="rbf", C=1.0, gamma="scale", random_state=random_seed),
    )
    classical_model.fit(X_train, y_train)
    classical_predictions = classical_model.predict(X_test)
    classical_accuracy = accuracy_score(y_test, classical_predictions)

    print("Classical baseline")
    print("------------------")
    print("Dataset: Iris binary subset")
    print(f"Classes: {class_names[0]} vs {class_names[1]}")
    print(f"Features: {feature_names}")
    print("Model: StandardScaler + SVC(kernel='rbf')")
    print(f"Accuracy: {classical_accuracy:.3f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, classical_predictions))
    print()

    # Quantum feature maps usually expect bounded feature values.
    # Scaling to [0, pi] keeps the toy inputs in a gate-angle-friendly range.
    angle_scaler = MinMaxScaler(feature_range=(0.0, np.pi))
    X_train_angles = angle_scaler.fit_transform(X_train)
    X_test_angles = angle_scaler.transform(X_test)

    feature_map = ZZFeatureMap(
        feature_dimension=2,
        reps=2,
        entanglement="linear",
    )

    quantum_kernel = FidelityQuantumKernel(feature_map=feature_map)

    # Use explicit precomputed kernel matrices for robust sklearn integration.
    train_kernel_matrix = quantum_kernel.evaluate(x_vec=X_train_angles)
    test_kernel_matrix = quantum_kernel.evaluate(
        x_vec=X_test_angles,
        y_vec=X_train_angles,
    )

    quantum_model = SVC(kernel="precomputed", C=1.0)
    quantum_model.fit(train_kernel_matrix, y_train)
    quantum_predictions = quantum_model.predict(test_kernel_matrix)
    quantum_accuracy = accuracy_score(y_test, quantum_predictions)

    print("QML candidate")
    print("-------------")
    print("Method: FidelityQuantumKernel + SVC(kernel='precomputed')")
    print("Feature map: ZZFeatureMap(feature_dimension=2, reps=2, entanglement='linear')")
    print("Input scaling: MinMaxScaler(feature_range=(0, pi))")
    print("Backend: default local simulation behavior from Qiskit primitives")
    print("Qubits: 2")
    print(f"Train kernel matrix shape: {train_kernel_matrix.shape}")
    print(f"Test kernel matrix shape: {test_kernel_matrix.shape}")
    print(f"Accuracy: {quantum_accuracy:.3f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, quantum_predictions))
    print()

    print("Comparison")
    print("----------")
    print(f"Classical accuracy: {classical_accuracy:.3f}")
    print(f"QML accuracy:       {quantum_accuracy:.3f}")
    print(f"Delta:              {quantum_accuracy - classical_accuracy:+.3f}")
    print()

    print("Classical classification report")
    print("--------------------------------")
    print(classification_report(y_test, classical_predictions, target_names=class_names))

    print("QML classification report")
    print("-------------------------")
    print(classification_report(y_test, quantum_predictions, target_names=class_names))

    print("Claim review")
    print("------------")
    print("This is a small educational benchmark on a built-in Iris subset.")
    print("It is useful for testing workflow, feature selection, and comparison discipline.")
    print("It is not evidence of quantum advantage.")
    print("Before making stronger claims, repeat with more seeds, stronger baselines,")
    print("additional feature pairs, ablations, runtime comparisons, and documented limitations.")


if __name__ == "__main__":
    main()
