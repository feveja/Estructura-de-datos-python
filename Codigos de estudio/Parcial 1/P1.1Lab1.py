import numpy as np

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    np_matriz1 = np.array(matriz1)
    np_matriz2 = np.array(matriz2)
    matriz_suma = np_matriz1 + np_matriz2
    return matriz_suma

def restar_matrices(matriz1, matriz2):
    np_matriz1 = np.array(matriz1)
    np_matriz2 = np.array(matriz2)
    matriz_resta = np_matriz1 - np_matriz2
    return matriz_resta

# Ingreso de filas y columnas para la matriz 1
filas1 = int(input("Ingrese el número de filas para la matriz 1: "))
columnas1 = int(input("Ingrese el número de columnas para la matriz 1: "))

# Creación de la matriz 1
print("Ingrese los elementos de la matriz 1:")
matriz1 = crear_matriz(filas1, columnas1)

# Ingreso de filas y columnas para la matriz 2
filas2 = int(input("Ingrese el número de filas para la matriz 2: "))
columnas2 = int(input("Ingrese el número de columnas para la matriz 2: "))

# Creación de la matriz 2
print("Ingrese los elementos de la matriz 2:")
matriz2 = crear_matriz(filas2, columnas2)

# Suma de las matrices
matriz_suma = sumar_matrices(matriz1, matriz2)

# Resta de las matrices
matriz_resta = restar_matrices(matriz1, matriz2)

# Imprimir las matrices resultantes
print("\nMatriz 1:")
print(np.array(matriz1))

print("\nMatriz 2:")
print(np.array(matriz2))

print("\nMatriz suma:")
print(matriz_suma)

print("\nMatriz resta:")
print(matriz_resta)
