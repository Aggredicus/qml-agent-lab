"""
Example: Compare classical SVM vs Qiskit quantum kernel SVM on a small dataset.

Gracefully handles missing Qiskit.
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Classical baseline
clf = SVC(kernel="rbf")
clf.fit(X_train, y_train)
classical_acc = clf.score(X_test, y_test)

print(f"Classical RBF SVM accuracy: {classical_acc:.3f}")

# Try Qiskit kernel
try:
    from qiskit.circuit.library import ZZFeatureMap
    from qiskit_machine_learning.kernels import QuantumKernel

    feature_map = ZZFeatureMap(feature_dimension=X.shape[1], reps=2)
    qkernel = QuantumKernel(feature_map=feature_map)

    qsvc = SVC(kernel=qkernel.evaluate)
    qsvc.fit(X_train, y_train)
    quantum_acc = qsvc.score(X_test, y_test)

    print(f"Quantum kernel SVM accuracy: {quantum_acc:.3f}")

except ImportError:
    print("Qiskit not installed. Skipping quantum kernel example.")
