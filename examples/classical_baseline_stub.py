"""
classical_baseline_stub.py

Minimal scikit-learn baseline example for QML Agent Lab.

Run this before building a QML candidate.

This script demonstrates the repository rule:
Every QML experiment must include a classical baseline.
"""

from __future__ import annotations


def main() -> None:
    try:
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVC
        from sklearn.metrics import accuracy_score, classification_report
    except ImportError as exc:
        print("Missing dependency:", exc)
        print()
        print("Install dependencies with:")
        print("  pip install -r requirements.txt")
        print()
        print("This example requires:")
        print("  scikit-learn")
        return

    random_seed = 42

    X, y = make_classification(
        n_samples=80,
        n_features=4,
        n_informative=3,
        n_redundant=1,
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

    model = make_pipeline(
        StandardScaler(),
        SVC(kernel="rbf", random_state=random_seed),
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Classical baseline example")
    print("--------------------------")
    print("Task: binary classification")
    print("Dataset: synthetic make_classification toy data")
    print("Model: StandardScaler + SVC(kernel='rbf')")
    print(f"Random seed: {random_seed}")
    print(f"Accuracy: {accuracy:.3f}")
    print()
    print("Classification report")
    print("---------------------")
    print(classification_report(y_test, predictions))
    print()
    print("Next steps")
    print("----------")
    print("1. Record this result in a comparison report.")
    print("2. Build a QML candidate on the same task and split.")
    print("3. Compare honestly and document limitations.")


if __name__ == "__main__":
    main()
