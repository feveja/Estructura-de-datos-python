import numpy as np

filas = int(input("ingrese cantidad de filas:"))
columnas = int(input("ingrese cantidad de columnas:"))

matriz1 = np.zeros((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = int(input(f"elementos de la matriz [{i}][{j}]:"))


matriz2 = np.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        matriz2[i][j] = int(input(f"elementos de la matriz [{i}][{j}]:"))

def suma_matrices(matriz1,matriz2):
    suma = np.add(matriz1,matriz2)
    return suma


def resta_matrices(matriz1, matriz2):
    resta = np.subtract(matriz1,matriz2)
    return resta

suma= suma_matrices(matriz1,matriz2)
print("La suma de las matrices es:")
print (suma)

resta= resta_matrices(matriz1,matriz2)
print("la resta de las matrices es:")
print(resta)