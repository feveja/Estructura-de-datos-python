import random

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(1, 5) for _ in range(columnas)]
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
filas = int(input("Ingrese el número de filas para las matrices: "))
columnas = int(input("Ingrese el número de columnas para las matrices: "))

# Creación de las matrices aleatorias
matriz1 = crear_matriz(filas, columnas)
matriz2 = crear_matriz(filas, columnas)

# Suma de las matrices
matriz_suma = sumar_matrices(matriz1, matriz2)

# Resta de las matrices
matriz_resta = restar_matrices(matriz1, matriz2)

# Imprimir las matrices resultantes
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nMatriz suma:")
for fila in matriz_suma:
    print(fila)

print("\nMatriz resta:")
for fila in matriz_resta:
    print(fila)
 