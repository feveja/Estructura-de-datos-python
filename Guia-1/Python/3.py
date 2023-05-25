import random

# Definir la matriz de 3x3 con elementos aleatorios
matriz = [[random.randint(1, 10) for i in range(3)] for j in range(3)]

# Imprimir la matriz
for fila in matriz:
    print(fila)

# Como el ejercicio especifica que la matriz es 3x3.Calcular la determinante por el metodo de sarrus
determinante = 0 #Determinate Total ya que lo vamos a hacer por el metodo de sarrus para 3x3

for i in range(3):
    det_parcial = 1 #Como estamos trabajando multiplicacion este valor tiene que ser 1 o siempre sera 0
    for j in range(3):
        det_parcial *= matriz[j][(i+j)%3] #Para encontrar el indice correcto al calcular el producto de da cada diagonal
    determinante += det_parcial #Sumamos la parte de la suma del metodo de sarrus a nuestra determinante total

for i in range(3):
    det_parcial = 1
    for j in range(3):
        det_parcial *= matriz[2-j][(i+j)%3] 
    determinante -= det_parcial

# Imprimir la determinante
print("Determinante:", determinante)
