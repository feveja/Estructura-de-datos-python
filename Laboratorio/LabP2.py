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
        M1 = escalar*M1[i][j] #Segun mi logica M4 seria el resultado de la multiplicacion del escalar con la matriz dando M4 
#Para imprimir la matriz resultante 
for i in range(filas):
    for j in range(columnas):
        print(M1[filas][columnas]) #Me lanza error al imprimir la matriz resultante