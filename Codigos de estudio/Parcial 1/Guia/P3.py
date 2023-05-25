import numpy as np

# Generar una matriz de 3x3 con elementos aleatorios entre 5 y 10
matriz = np.random.randint(5, 11, size=(3, 3))

# Calcular el determinante
determinante = np.linalg.det(matriz)

# Imprimir la matriz y el determinante
print("Matriz:")
print(matriz)
print("Determinante:", determinante)
