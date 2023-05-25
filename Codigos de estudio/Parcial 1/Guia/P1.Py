# Crear la matriz
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Inicializar las variables para almacenar los resultados
suma_mas_alta = 0
suma_mas_baja = float('inf')

# Calcular la suma de cada columna
for columna in range(5):
    suma_columna = 0
    for fila in range(5):
        suma_columna += matriz[fila][columna]
    # Actualizar la suma más alta si corresponde
    if suma_columna > suma_mas_alta:
        suma_mas_alta = suma_columna

# Calcular la suma de cada fila y la suma más baja
for fila in range(5):
    suma_fila = sum(matriz[fila])
    # Actualizar la suma más baja si corresponde
    if suma_fila < suma_mas_baja:
        suma_mas_baja = suma_fila

# Imprimir los resultados
print("La suma más alta entre las columnas es:", suma_mas_alta)
print("La suma más baja entre las filas es:", suma_mas_baja)
