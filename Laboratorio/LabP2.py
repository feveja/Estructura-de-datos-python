import random as rp
#Para las 2 primeras matrices
filas = int(input("Ingrese la cantidad filas: "))
columnas = int(input("Ingrese la cantidad columnas: "))
escalar = int(input("Ingrese escalar a multiplicar"))
#llenamos la matriz con elementos aleatorios 
M5= [[rp.randint(0,10) for j in range(columnas) for i in range(filas)]]
#Para la multiplicacion por el escalar 
for i in range(filas):
    for j in range(columnas):
        M5 = M5*escalar #Segun mi logica M4 seria el resultado de la multiplicacion del escalar con la matriz dando M4 
#Para imprimir la matriz resultante 
for i in range(filas):
    for j in range(columnas):
        print(M5[i][j]) #Me lanza error al imprimir la matriz resultante
#Segun mi pensamiento poco logico este codigo tomaria la matriz generada y tomaria el escalar y lo multiplicaria y el resultado seria la misma matriz 