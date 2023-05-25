import numpy as np
#Multiplicacion de matrices con numpy
# Generar la primera matriz de 3x3 con elementos aleatorios entre -10 y -5
matriz1 = np.random.randint(-10, -4, size=(3, 3))
# Generar la segunda matriz de 3x3 con elementos aleatorios entre -10 y -5
matriz2 = np.random.randint(-10, -4, size=(3, 3))
# Verificar que las dimensiones sean adecuadas para la multiplicación
if matriz1.shape[1] != matriz2.shape[0]:
    print("No se pueden multiplicar las matrices debido a dimensiones incompatibles.")
else:
    # Realizar la multiplicación de matrices
    matriz_resultante = np.dot(matriz1, matriz2)
    # Imprimir la matriz resultante
    print("Matriz resultante de la multiplicación:")
    print(matriz_resultante)
    # Multiplicar la matriz resultante por una matriz identidad
    matriz_final = np.dot(matriz_resultante, np.eye(3)) #np.eye es para la identidad #dot para multiplicar
    # Imprimir la matriz final
    print("Matriz final:")
    print(matriz_final)
#################################################################################################################
#Determinantes con numpy
# Generar una matriz de 3x3 con elementos aleatorios entre 5 y 10
matriz = np.random.randint(5, 11, size=(3, 3)) #Size para el tamaño de nuestra matriz 
# Calcular el determinante
determinante = np.linalg.det(matriz)
# Imprimir la matriz y el determinante
print("Matriz:")
print(matriz)
print("Determinante:", determinante)
####################################################################################################################
#Para concadenar
# En una dimension
x = np.array([1, 2, 3]) # Vector de valores
y = np.array([3, 2, 1]) # Vector de valores
np.concatenate([x, y]) # Concatenacion
########################################################################################################################
#creacion de una matriz de ejemplo
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#Para su transpuesta
arr_2d.T