import random

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(0, 10) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def multiplicar_matriz(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_resultante = []
    for i in range(filas):
        fila_resultante = []
        for j in range(columnas):
            producto = matriz[i][j] * escalar
            fila_resultante.append(producto)
        matriz_resultante.append(fila_resultante)
    return matriz_resultante

# Ingreso de filas y columnas para la matriz
filas = int(input("Ingrese el número de filas para la matriz: "))
columnas = int(input("Ingrese el número de columnas para la matriz: "))

# Ingreso del escalar
escalar = int(input("Ingrese un valor escalar: "))

# Creación de la matriz aleatoria
matriz = crear_matriz(filas, columnas)

# Multiplicación de la matriz por el escalar
matriz_resultante = multiplicar_matriz(matriz, escalar)

# Imprimir la matriz resultante
print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz resultante:")
for fila in matriz_resultante:
    print(fila)
