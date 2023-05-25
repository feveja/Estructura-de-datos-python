#2.1.1
import random

matriz = []
for i in range(5):
    aux=[]
    for j in range(5):
        num = random.randint(1,5)
        aux.append(num)
    matriz.append(aux)

print(f"la matriz 5x5 es: {matriz}")

sumas_j=[]
for j in range(5):
    aux=0
    for i in range(5):
        aux = aux + matriz[i][j]
    sumas_j.append(aux)

print(f"el conjunto de las sumas de columnas es: {sumas_j}")

sumas_i=[]
for i in range(5):
    aux=0
    for j in range(5):
        aux = aux + matriz[i][j]
    sumas_i.append(aux)

print(f"el conjunto de las sumas de filas es: {sumas_i}")

for j in range(5):
    if j ==0:
        mayor=sumas_j[j]
    elif mayor < sumas_j[j]:
        mayor=sumas_j[j]

print(f"la suma mas alta de las columnas es: {mayor}")

for i in range(5):
    if i ==0:
        menor=sumas_i[i]
    elif sumas_i[i] < menor:
        menor=sumas_i[i]

print(f"la suma mas baja de las filas es: {menor}")