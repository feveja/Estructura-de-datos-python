#Matriz unidimencional - vertical
for i in range (1,7):
    print(i)
print("\n")
#Matriz unidirecional - Horizontal
for i in range(1,7):
    print(i, end = " ") 

print("\n")

#Matriz bidimencional (6x6)
#For anidado
for i in range(1,7):
    for j in range(1,7):
        print(0, end =" ")
    print(" ")

print("\n")

for i in range(1,7):
    for j in range(1,7):
        print(f'({i},{j})', end =" ")
    print(" ")

print("\n")

#Ejercicio: Colocar 1 en la diagonal
for i in range(1,7):
    for j in range(1,7):
        if(i==j):
            print(1, end =" ")
        else:
            print(0, end = ' ')
    print(" ")

###########################################################
#En formato Matriz con corchetes
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(row)
###############################################################
#En formato columna 
for row in matrix:
    for element in row:
        print(element)
#Acceder de elemento a elemento sin corchetes
for row in matrix: #Filas
    for elemen in row: #Columnas
        print(element, end=" ")
    print(" ")
