import random

def depolarizing_channel(circuit, qubit, decoherence_percent):
    if(random.random() <= decoherence_percent):
        gate = random.randint(0,2)
        if gate == 0:
            circuit.x(qubit)
        if gate == 1:
            circuit.y(qubit)
        if gate == 2:
            circuit.z(qubit)
    return