import random

# Generar una matriz aleatoria de tamaño entre 3 y 5
n = random.randint(3, 5)
matriz = []
for _ in range(n):
    fila = [random.randint(1, 10) for _ in range(n)]
    matriz.append(fila)
    
print("Matriz original:")
for fila in matriz:
    print(fila)

# Crear una matriz identidad del mismo tamaño que la matriz original
I = [[int(i == j) for i in range(n)] for j in range(n)]

# Ampliar la matriz adosando la matriz identidad
for i in range(n):
    matriz[i] += I[i]

# Aplicar eliminación gaussiana
for i in range(n):
    # Si el elemento diagonal es cero, intercambiar filas
    if matriz[i][i] == 0:
        for j in range(i + 1, n):
            if matriz[j][i] != 0:
                matriz[i], matriz[j] = matriz[j], matriz[i]
                break

    # Hacer ceros debajo del elemento diagonal
    for j in range(i + 1, n):
        factor = matriz[j][i] / matriz[i][i]
        for k in range(n * 2):
            matriz[j][k] -= factor * matriz[i][k]

# Realizar sustitución hacia atrás para obtener una matriz diagonal
for i in range(n - 1, -1, -1):
    factor = matriz[i][i]
    for j in range(i, n * 2):
        matriz[i][j] /= factor

    for j in range(i - 1, -1, -1):
        factor = matriz[j][i]
        for k in range(i, n * 2):
            matriz[j][k] -= factor * matriz[i][k]

# Extraer la matriz inversa de la parte derecha de la matriz ampliada
matriz_inversa = [fila[n:] for fila in matriz]
print("Matriz inversa:")
for fila in matriz_inversa:
    print(fila)
