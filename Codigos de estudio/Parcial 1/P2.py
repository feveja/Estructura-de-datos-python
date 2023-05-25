import numpy as np

# Generar la primera matriz de 3x3 con elementos aleatorios entre -10 y -5
matriz1 = np.random.randint(-10, -4, size=(3, 3))

# Generar la segunda matriz de 3x3 con elementos aleatorios entre -10 y -5
matriz2 = np.random.randint(-10, -4, size=(3, 3))

# Verificar que las dimensiones sean adecuadas para la multiplicación
if matriz1.shape[1] != matriz2.shape[0]:
    print("No se pueden multiplicar las matrices debido a dimensiones incompatibles.")
else:
    # Realizar la multiplicación de matrices
    matriz_resultante = np.dot(matriz1, matriz2)

    # Imprimir la matriz resultante
    print("Matriz resultante de la multiplicación:")
    print(matriz_resultante)

    # Multiplicar la matriz resultante por una matriz identidad
    matriz_final = np.dot(matriz_resultante, np.eye(3))

    # Imprimir la matriz final
    print("Matriz final:")
    print(matriz_final)
