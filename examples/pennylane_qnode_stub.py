"""
pennylane_qnode_stub.py

Educational starter example for a tiny PennyLane QNode.

This script demonstrates how data and parameters can enter a quantum circuit.

It is not evidence of quantum advantage.
"""

from __future__ import annotations


def main() -> None:
    try:
        import pennylane as qml
        import numpy as np
    except ImportError as exc:
        print("Missing dependency:", exc)
        print()
        print("Install dependencies with:")
        print("  pip install -r requirements.txt")
        print()
        print("This example requires:")
        print("  pennylane")
        print("  numpy")
        return

    dev = qml.device("default.qubit", wires=2)

    @qml.qnode(dev)
    def circuit(x, weights):
        """
        Tiny hybrid-style circuit.

        x:
            Input features.

        weights:
            Trainable circuit parameters.
        """
        qml.RY(x[0], wires=0)
        qml.RY(x[1], wires=1)

        qml.CNOT(wires=[0, 1])

        qml.RZ(weights[0], wires=0)
        qml.RZ(weights[1], wires=1)

        return qml.expval(qml.PauliZ(0)), qml.expval(qml.PauliZ(1))

    x = np.array([0.25, -0.15])
    weights = np.array([0.5, -0.25])

    result = circuit(x, weights)

    print("PennyLane QNode example")
    print("----------------------")
    print(f"Input x: {x}")
    print(f"Weights: {weights}")
    print(f"Output expectation values: {result}")
    print()

    print("Circuit")
    print("-------")
    print(qml.draw(circuit)(x, weights))
    print()

    print("Extension notes")
    print("---------------")
    print("To turn this into a real experiment:")
    print("1. Add a classical baseline.")
    print("2. Add a dataset card.")
    print("3. Define a loss function.")
    print("4. Add a small optimizer loop.")
    print("5. Compare metrics fairly.")
    print()
    print("This is an educational stub, not evidence of quantum advantage.")


if __name__ == "__main__":
    main()
