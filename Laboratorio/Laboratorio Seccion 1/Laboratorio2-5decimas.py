import random
#Creamos una matriz aleatoria 
def matriz_random(filas,columnas):
    aux= []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            e=random.randint(1,5)
            fila.append(e)
        aux.append(fila)
    return aux

def resta_Ma(m,z):
    mf=[]
    for i in range(len(m)):
        fila=[]
        for j in range(len(m[0])):
            resta= m[i][j]-z[i][j]
            fila.append(resta) 
        mf.append(fila)
    return mf 
def suma(m,z):
    mf=[]
    for i in range(len(m)):
        fila=[]
        for j in range(len(m[0])):
            suma= m[i][j]+z[i][j]
            fila.append(suma) 
        mf.append(fila)
    return mf
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
print("Primera Matriz Aleatoria")
m1=matriz_random(filas,columnas)
print(m1,"\n")
print("Segunda Matriz aleatoria")
m2=matriz_random(filas,columnas)
print(m2,"\n")

#Resta
mf=resta_Ma(m1,m2)
print("La resta de las matrices da como resultado: ")
for fila in mf:
    print(fila,)
#Suma
mf=suma(m1,m2)
print("La suma de las matrices da como resultado: ")
for fila in mf:
    print(fila)