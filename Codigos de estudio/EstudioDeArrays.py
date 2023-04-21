#Arreglos
edades= [1,2,3,4,5]
print(edades) #Imprime el array
#Posicion (indice)
#0 = 1
#1 = 2
#2 = 3
#3 = 4
#4 = 5
mi_edad = edades[4]
print("mi edad es"+str(mi_edad))
edades[4]= 15 #Cambiamos el elemento de la posicion 1
print(edades)

#Len (Cantidad de elementos que tiene un arreglo)
print(str(len(edades)))

#Metodo 1 append
edades.append(1)

#Metodo 2 count
print(str(edades.count(1)))

#Metodo 3 index
posicion = edades.index(15)
print(posicion)

