def matriz_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):
        fila_transpuesta = []
        for i in range(filas):
            fila_transpuesta.append(matriz[i][j])
        transpuesta.append(fila_transpuesta)
    return transpuesta
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
AT = matriz_transpuesta(A)
ATT = matriz_transpuesta(AT)
print("la matriz transpuesta es:")
for fila in AT:
    for elemento in fila:
        print(elemento, end=" ")
    print( end="\n")
if A == ATT:
    print("las matrices ATT = A por lo tanto se cumple la propiedad")