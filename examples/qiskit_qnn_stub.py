"""
qiskit_qnn_stub.py

Educational starter example showing the intended structure of a simple
Qiskit QNN-style workflow.

This script is intentionally minimal.

It is not a full training loop and not evidence of quantum advantage.
"""

from __future__ import annotations


def main() -> None:
    try:
        import numpy as np
        from qiskit import QuantumCircuit
        from qiskit.circuit import Parameter
        from qiskit_machine_learning.neural_networks import EstimatorQNN
    except ImportError as exc:
        print("Missing dependency:", exc)
        print()
        print("Install dependencies with:")
        print("  pip install -r requirements.txt")
        print()
        print("This example requires:")
        print("  numpy")
        print("  qiskit")
        print("  qiskit-machine-learning")
        return

    # Define a tiny one-qubit parameterized circuit.
    x = Parameter("x")
    theta = Parameter("theta")

    circuit = QuantumCircuit(1)
    circuit.ry(x, 0)
    circuit.rz(theta, 0)

    print("Circuit")
    print("-------")
    print(circuit.draw(output="text"))
    print()

    # EstimatorQNN can map circuit parameters to expectation values.
    # input_params are data inputs.
    # weight_params are trainable parameters.
    qnn = EstimatorQNN(
        circuit=circuit,
        input_params=[x],
        weight_params=[theta],
    )

    # Tiny forward pass.
    input_data = np.array([[0.25]])
    weights = np.array([0.5])

    result = qnn.forward(input_data, weights)

    print("QNN forward pass")
    print("----------------")
    print(f"Input data: {input_data}")
    print(f"Weights: {weights}")
    print(f"Output: {result}")
    print()

    print("Extension notes")
    print("---------------")
    print("To turn this into a real experiment:")
    print("1. Add a classical baseline.")
    print("2. Add a dataset card.")
    print("3. Add a training loop or classifier wrapper.")
    print("4. Record qubits, circuit depth, backend, metrics, and limitations.")
    print()
    print("This is an educational stub, not evidence of quantum advantage.")


if __name__ == "__main__":
    main()
