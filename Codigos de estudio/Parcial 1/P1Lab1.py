import random

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(0, 5) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_suma = []
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        matriz_suma.append(fila_suma)
    return matriz_suma

def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resta = []
    for i in range(filas):
        fila_resta = []
        for j in range(columnas):
            resta = matriz1[i][j] - matriz2[i][j]
            fila_resta.append(resta)
        matriz_resta.append(fila_resta)
    return matriz_resta

# Ingreso de filas y columnas para las matrices
filas1 = int(input("Ingrese el número de filas para la primera matriz: "))
columnas1 = int(input("Ingrese el número de columnas para la primera matriz: "))

filas2 = int(input("Ingrese el número de filas para la segunda matriz: "))
columnas2 = int(input("Ingrese el número de columnas para la segunda matriz: "))

filas3 = int(input("Ingrese el número de filas para la tercera matriz: "))
columnas3 = int(input("Ingrese el número de columnas para la tercera matriz: "))

# Creación de las matrices aleatorias
matriz1 = crear_matriz(filas1, columnas1)
matriz2 = crear_matriz(filas2, columnas2)
matriz3 = crear_matriz(filas3, columnas3)

# Suma de las dos primeras matrices
matriz_suma = sumar_matrices(matriz1, matriz2)

# Resta de la tercera matriz con la matriz suma
matriz_resta = restar_matrices(matriz_suma, matriz3)

# Imprimir las matrices resultantes
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nMatriz 3:")
for fila in matriz3:
    print(fila)

print("\nMatriz suma:")
for fila in matriz_suma:
    print(fila)

print("\nMatriz resta:")
for fila in matriz_resta:
    print(fila)
