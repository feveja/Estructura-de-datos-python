import random as rp
#Para las 2 primeras matrices
filas = int(input("Ingrese la cantidad filas: "))
columnas = int(input("Ingrese la cantidad columnas: "))
#llenamos la matriz con elementos aleatorios 
M1= [[rp.randint(0,5) for j in range(columnas) for i in range(filas)]]
M2 = [[rp.randint(0,5) for j in range(columnas) for i in range(filas)]]
#Para la suma de las matrices M1 y M2
for i in range(filas):
    for j in range(columnas):
        [Msuma] = [M1+ M2] #Segun mi logica se crea una Nueva variable con la suma de los terminos
#Pedimos la tercera matriz
filas2 = int(input("Ingrese la cantidad filas: "))
columnas2 = int(input("Ingrese la cantidad columnas: "))
M3 = [[rp.randint(0,5) for j in range(columnas2) for i in range(filas2)]]
#Para la resta de la Msuma con M3
for i in range(filas2):
    for j in range(columnas2):
        M3 = [M3- Msuma]         #Pero aqui esa misma variable nos lanza error
#Para el resultado imprimimos M3 resultante
for i in range(filas2):
    for j in range(columnas2):
        print(Msuma[i][j]) #Error al imprimir 
#Este Tomaria M1 y M2 los sumaria en una nueva matriz y esa matriz se restaria con M3 para luego imprimirse