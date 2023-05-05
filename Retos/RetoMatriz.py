# Definir las matrices
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

# Inicializar la matriz de resultado con ceros
resultado = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# Sumar las correspondientes entradas de ambas matrices y colocar el resultado en la matriz de resultado
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

# Imprimir la matriz de resultado
for fila in resultado:
    print(fila)

# Inicializar la matriz transpuesta con ceros
transpuesta = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

# Intercambiar las filas y columnas de la matriz resultado y colocar el resultado en la matriz transpuesta
for i in range(len(resultado)):
    for j in range(len(resultado[0])):
        transpuesta[j][i] = resultado[i][j]

# Imprimir la matriz transpuesta
for fila in transpuesta:
    print(fila)