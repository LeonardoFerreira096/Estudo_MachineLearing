import numpy as np

entradas = np.array([
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 1]
])


pesos = np.array([0.2, 0.3])

def soma(e, p):
    return e.dot(p)

def stepFunction(s):
    return (s >= 0.5).astype(int)

s = soma(entradas, pesos)
r = stepFunction(s)

print(f"somas:    {s}")
print(f"saidas:   {r}")
print(f"esperado: {np.array([0, 0, 1, 1])}")