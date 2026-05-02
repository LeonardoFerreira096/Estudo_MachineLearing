import numpy as np


# Dados de entrada: nota do filme, compatibilidade de gênero
entradas = np.array([
    [1, 1],  # Filme A
    [2, 1],  # Filme B
    [3, 2],  # Filme C       
    [4, 1]   # Filme D    
])

# w1 = peso da nota  w2 = peso da compatibilidade de genero
pesos = np.array([0.1, 0.4])


def soma(e, p):
    return e.dot(p)

def stepFunction(s):
    return (s > 0.5).astype(int)

s = soma(entradas, pesos)
r = stepFunction(s)


print(f"somas:    {s}")
print(f"saidas:   {r}")
print(f"esperado: {np.array([0, 0, 1, 1])}")