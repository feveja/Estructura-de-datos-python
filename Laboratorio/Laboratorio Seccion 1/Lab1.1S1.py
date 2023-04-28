import numpy
#Anais Caro
#Felipe Vera
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m = numpy.zeros((filas, columnas)) #Creamos una array con 0 para llenarlos
for i in range(filas):
    filas = []
    for j in range(columnas):
        m[i][j] = int(input(f"Elemento ({i + 1}, {j + 1}): "))

filas2 = int(input("Ingrese la cantidad de filas: "))
columnas2 = int(input("Ingrese la cantidad de columnas: "))
aux = numpy.zeros((filas2, columnas2))
for i in range(filas2):
    filas2 = []
    for j in range(columnas2):
        aux[i][j] = int(input(f"Elemento ({i + 1}, {j + 1}): "))

if filas == filas2 and columnas == columnas2: #Si esto no se cumple estariamos con una matriz que no se puede sumar
    print(f"Suma matrices:\n{m+aux}'")
    print(f"Resta matrices:\n{m-aux}'")
else: print("Las matrices no son iguales en medida")