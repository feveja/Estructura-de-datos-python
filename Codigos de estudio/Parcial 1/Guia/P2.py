import numpy as np
def comprobar_propiedad(matriz_A):
    # Calcula la matriz inversa de A
    matriz_inversa = np.linalg.inv(matriz_A)
    # Realiza la multiplicación de A por su inversa
    resultado = np.matmul(matriz_A, matriz_inversa)
    # Comprueba si el resultado es igual a la matriz identidad
    matriz_identidad = np.eye(matriz_A.shape[0])
    if np.allclose(resultado, matriz_identidad):
        print("La propiedad A × A−1 = I se cumple.")
    else:
        print("La propiedad A × A−1 = I no se cumple.")
# Ejemplo de uso
matriz_A = np.array([[2, 1], [4, 3]])
comprobar_propiedad(matriz_A)
