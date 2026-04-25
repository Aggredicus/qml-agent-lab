# Moons Quantum Kernel Comparison

## Summary

This benchmark compares a classical RBF-kernel SVM against a Qiskit quantum kernel SVM on `sklearn.datasets.make_moons`.

This is an educational benchmark and is not evidence of quantum advantage.

## Environment

- Python: 3.13.5
- qiskit: installed
- qiskit-machine-learning: installed
- sklearn: installed
- numpy: installed

## Dataset

- Dataset: `make_moons`
- Samples: 80
- Noise: 0.18
- Random seed: 42
- Train/test split: 75/25 stratified
- Train samples: 60
- Test samples: 20

## Models Compared

| Model | Configuration |
|---|---|
| Classical baseline | `StandardScaler + SVC(kernel="rbf")` |
| QML candidate | `ZZFeatureMap + FidelityQuantumKernel + SVC(kernel="precomputed")` |

## Results

| Model | Accuracy | Correct | Incorrect |
|---|---:|---:|---:|
| Classical RBF SVM | 0.900 | 18 / 20 | 2 / 20 |
| Qiskit quantum kernel SVM | 0.700 | 14 / 20 | 6 / 20 |

## Classical Confusion Matrix

```text
[[9 1]
 [1 9]]
```

## Classical Classification Report

```text
              precision    recall  f1-score   support

           0       0.90      0.90      0.90        10
           1       0.90      0.90      0.90        10

    accuracy                           0.90        20
   macro avg       0.90      0.90      0.90        20
weighted avg       0.90      0.90      0.90        20
```

## QML Confusion Matrix

```text
[[6 4]
 [2 8]]
```

## QML Classification Report

```text
              precision    recall  f1-score   support

           0       0.75      0.60      0.67        10
           1       0.67      0.80      0.73        10

    accuracy                           0.70        20
   macro avg       0.71      0.70      0.70        20
weighted avg       0.71      0.70      0.70        20
```

## Interpretation

The classical RBF SVM outperformed the QML candidate on this first Moons benchmark.

```text
Classical accuracy: 0.900
QML accuracy:       0.700
Delta:             -0.200
```

This is a useful result because it shows the benchmark is not biased toward flattering the QML method. The QML candidate must justify itself against a strong classical baseline.

## Claim Review

This result supports the claim that the repository can run a small classical-vs-QML comparison workflow.

This result does not support claims of quantum advantage, QML superiority, or production readiness.

## Known Limitations

- Small toy dataset
- Single random seed
- No hyperparameter sweep
- No repeated cross-validation
- No runtime comparison
- Uses `ZZFeatureMap`, which is deprecated as a class in recent Qiskit versions
- Tested in one Python environment only

## Recommended Next Steps

- Repeat across multiple random seeds
- Add a seed-sweep summary
- Compare additional feature maps
- Tune `reps`, `C`, and feature scaling
- Replace deprecated `ZZFeatureMap` class with newer Qiskit feature-map API
- Add visualization of the Moons decision boundary
