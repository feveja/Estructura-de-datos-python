import random
import numpy as np
# Generar el número de filas y columnas aleatorias (de 2 a 5)
filas = random.randint(2, 5)
columnas = random.randint(2, 5)

# Crear la primera matriz y solicitar al usuario ingresar los elementos
print("Ingrese los elementos de la primera matriz:")
matriz1 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz1.append(fila)

# Crear la segunda matriz y solicitar al usuario ingresar los elementos
print("\nIngrese los elementos de la segunda matriz:")
matriz2 = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = int(input(f"Ingrese el elemento ({i+1}, {j+1}): "))
        fila.append(elemento)
    matriz2.append(fila)

# Restar las matrices y almacenar el resultado en una nueva matriz
resultado = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = matriz1[i][j] - matriz2[i][j]
        fila.append(elemento)
    resultado.append(fila)

# Imprimir las matrices y el resultado
print("\nMatriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nResultado de la resta:")
for fila in resultado:
    print(fila)

# Generar el número de filas y columnas aleatorias para la nueva matriz (de 2 a 5)
filas_nueva = random.randint(2, 5)
columnas_nueva = random.randint(2, 5)

# Crear la nueva matriz y solicitar al usuario ingresar los elementos
print("Ingrese los elementos de la nueva matriz:")
nueva_matriz = []
for i in range(filas_nueva):
    fila = []
    for j in range(columnas_nueva):
        elemento = int(input(f"Ingrese el elemento ({i+1}, {j+1}): "))
        fila.append(elemento)
    nueva_matriz.append(fila)

# Convertir las matrices en arrays de NumPy
matriz_resultado_np = np.array(resultado)
nueva_matriz_np = np.array(nueva_matriz)

# Multiplicar la matriz resultado por la nueva matriz
producto = np.matmul(matriz_resultado_np, nueva_matriz_np)

# Calcular las traspuestas de las matrices
matriz_resultado_traspuesta = matriz_resultado_np.T
nueva_matriz_traspuesta = nueva_matriz_np.T

# Calcular la multiplicación de las traspuestas
producto_traspuestas = np.matmul(nueva_matriz_traspuesta, matriz_resultado_traspuesta)

# Verificar la propiedad de las matrices traspuestas
propiedad_verificada = np.array_equal(producto.T, producto_traspuestas)

# Imprimir las matrices y el resultado de la multiplicación
print("\nMatriz Resultado de la Resta:")
print(matriz_resultado_np)

print("\nNueva Matriz:")
print(nueva_matriz_np)

print("\nProducto de la Matriz Resultado por la Nueva Matriz:")
print(producto)

print("\nTraspuesta de la Matriz Resultado:")
print(matriz_resultado_traspuesta)

print("\nTraspuesta de la Nueva Matriz:")
print(nueva_matriz_traspuesta)

print("\nProducto de las Traspuestas:")
print(producto_traspuestas)

# Imprimir la verificación de la propiedad de las matrices traspuestas
print("\n¿Se cumple la propiedad (A*B)^T = B^T * A^T?")
if propiedad_verificada:
    print("Sí, se cumple la propiedad.")
else:
    print("No, no se cumple la propiedad.")