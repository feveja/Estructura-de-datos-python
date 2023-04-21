import random as rp
#Para las 2 primeras matrices
filas = int(input("Ingrese la cantidad filas: "))
columnas = int(input("Ingrese la cantidad columnas: "))
escalar = int(input("Ingrese escalar a multiplicar"))
#llenamos la matriz con elementos aleatorios 
M1= [[rp.randint(0,10) for j in range(columnas) for i in range(filas)]]
#Para la multiplicacion por el escalar 
for i in range(filas):
    for j in range(columnas):
        M1 = escalar*M1
#Para imprimir la matriz resultante 