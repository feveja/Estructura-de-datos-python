import random
import numpy as np
# Obtener la cantidad de filas y columnas por teclado
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Crear la primera matriz con números aleatorios del 1 al 5
matriz1 = [[random.randint(1, 5) for i in range(columnas)] for i in range(filas)]

# Crear la segunda matriz con números aleatorios del 1 al 5
matriz2 = [[random.randint(1, 5) for i in range(columnas)] for i in range(filas)]

# Inicializar la matriz resultante con ceros
matriz_resultante = [[0 for i in range(columnas)] for i in range(filas)]

# Sumar las matrices elemento por elemento
for i in range(filas):
    for j in range(columnas):
        matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]

# Imprimir la matriz resultante
print("Matriz resultante:")
for fila in matriz_resultante:
    print(fila)
# Obtener el escalar por teclado
escalar = int(input("Ingrese un escalar del 1 al 10: "))

# Multiplicar la matriz resultante por el escalar
matriz_resultante *= escalar

# Imprimir la matriz resultante
print("Matriz resultante:")
for fila in matriz_resultante:
    print(fila)
# Crear la nueva matriz ingresada por teclado con sus elementos
filas_nueva_matriz = int(input("Ingrese la cantidad de filas de la nueva matriz: "))
columnas_nueva_matriz = int(input("Ingrese la cantidad de columnas de la nueva matriz: "))
nueva_matriz = []
for i in range(filas_nueva_matriz):
    fila = []
    for j in range(columnas_nueva_matriz):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(elemento)
    nueva_matriz.append(fila)

# Obtener la matriz resultante de la suma anterior
matriz_resultante = np.array(matriz_resultante)

# Realizar la multiplicación entre la matriz resultante y la nueva matriz
matriz_final = np.dot(matriz_resultante, nueva_matriz)
#Imprimir la Matriz final de la multiplicacion
print("Matriz final:")
for fila in matriz_final:
    print(fila)