# Iris Quantum Kernel Comparison

## Summary

This benchmark compares a classical RBF-kernel SVM against a Qiskit quantum kernel SVM on a binary subset of the built-in scikit-learn Iris dataset.

The benchmark uses the harder `versicolor` vs `virginica` class pair rather than the easier `setosa` comparisons.

This is an educational benchmark and is not evidence of quantum advantage.

## Environment

- Python: 3.13.5
- numpy: 2.3.5
- scikit-learn: 1.8.0
- qiskit: 2.4.1
- qiskit-machine-learning: 0.9.0

## Dataset

- Dataset: `sklearn.datasets.load_iris`
- Classes: `versicolor` vs `virginica`
- Features: `petal length (cm)`, `petal width (cm)`
- Samples: 100
- Random seed: 42
- Train/test split: 75/25 stratified
- Train samples: 75
- Test samples: 25

## Models Compared

| Model | Configuration |
|---|---|
| Classical baseline | `StandardScaler + SVC(kernel="rbf")` |
| QML candidate | `ZZFeatureMap + FidelityQuantumKernel + SVC(kernel="precomputed")` |

## Results

| Model | Accuracy | Correct | Incorrect |
|---|---:|---:|---:|
| Classical RBF SVM | 0.880 | 22 / 25 | 3 / 25 |
| Qiskit quantum kernel SVM | 0.600 | 15 / 25 | 10 / 25 |

## Classical Confusion Matrix

Rows are true labels and columns are predicted labels.

Label order: `versicolor`, `virginica`

```text
[[12  1]
 [ 2 10]]
```

## Classical Classification Report

```text
              precision    recall  f1-score   support

  versicolor       0.86      0.92      0.89        13
   virginica       0.91      0.83      0.87        12

    accuracy                           0.88        25
   macro avg       0.88      0.88      0.88        25
weighted avg       0.88      0.88      0.88        25
```

## QML Confusion Matrix

Rows are true labels and columns are predicted labels.

Label order: `versicolor`, `virginica`

```text
[[8 5]
 [5 7]]
```

## QML Classification Report

```text
              precision    recall  f1-score   support

  versicolor       0.62      0.62      0.62        13
   virginica       0.58      0.58      0.58        12

    accuracy                           0.60        25
   macro avg       0.60      0.60      0.60        25
weighted avg       0.60      0.60      0.60        25
```

## QML Configuration

- Feature map: `ZZFeatureMap(feature_dimension=2, reps=2, entanglement="linear")`
- Input scaling: `MinMaxScaler(feature_range=(0, pi))`
- Classifier: `SVC(kernel="precomputed")`
- Qubits: 2
- Train kernel matrix shape: `(75, 75)`
- Test kernel matrix shape: `(25, 75)`
- Backend: default local simulation behavior from Qiskit primitives

## Interpretation

The classical RBF SVM outperformed the QML candidate on this first Iris benchmark.

```text
Classical accuracy: 0.880
QML accuracy:       0.600
Delta:             -0.280
```

This is a useful result because it confirms that the benchmark process is not biased toward flattering the QML method. The QML candidate must justify itself against a strong classical baseline.

## Claim Review

This result supports the claim that the repository can run a small classical-vs-QML comparison workflow on a built-in real dataset.

This result does not support claims of quantum advantage, QML superiority, or production readiness.

## Known Limitations

- Small dataset
- Binary subset only
- Two selected features only
- Single random seed
- No hyperparameter sweep
- No repeated cross-validation
- No runtime comparison
- Uses `ZZFeatureMap`, which is deprecated as a class in recent Qiskit versions
- Tested in one Python environment only

## Recommended Next Steps

- Repeat across multiple random seeds
- Add a seed-sweep summary
- Compare additional Iris class pairs
- Compare additional feature pairs
- Tune `reps`, `C`, and feature scaling
- Replace deprecated `ZZFeatureMap` class with newer Qiskit feature-map API
- Add visualization of the decision boundary
