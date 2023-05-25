import random
#Creamos Las dos Matrices de manera aleatoria sus columnas y filas
m1=[]
filas = random.randint(2,5)
columnas= random.randint(2,5)
m2=[]
filas2 = random.randint(2,5)
columnas2= random.randint(2,5)
#Creamos Listas Vacias para Almacenar los resultados de la resta y la multiplicacion y la tercera matriz
m3=[]
filas3 = None #Cambiamos al Valor que de en la resta
columnas3 = None #Cambiamos al Valor que de en la resta
mr=[]
mt=[]
#Solicitamos Al usuario los elementos de cada matriz 
for i in range(filas):
    for j in range(columnas):
        m1= int(input(f"ElementoM1({i+1},{j+1}): "))
for i in range(filas2):
    for j in range(columnas2):
        m2= int(input(f"ElementoM2({i+1},{j+1}): "))
for i in range(filas3):
    for j in range(columnas3):
        m3= int(input(f"ElementoM3({i+1},{j+1}): ")) 
#Realizamos la resta de las dos matrices (Segun mi logica) pero cabe destacar que este es erroneo ya que seria de otra forma
for i in range(filas):
    for j in range(columnas):
        m3=m1[i][j] - m2[i][j]       
#Mostramos las matrices obtenidas en pantalla        
print("Matriz 1 ", m1)
print("Matriz 2", m2)
print("Matriz 3", m3)
#Para la matriz multiplicacion tenemos que recordar que 2x2 * 2x3 si se simplifica nos debe quedar como resultado una matriz de 2*3 si no nos lanza error
if columnas == filas3:
    for i in range(filas):
        for j in range(columnas):
        mr = m1[i][j] * m2[i][j]
    "Las matrices no se pueden multiplicar"
#Pasamos esta matriz resultado a una matriz transpuesta para comparar 
mrmt=[] 
for i in range(filas):
    for j in range(columnas):
        mrmt = mr[j][i]
#Para la funcion transpuesta tenemos que recordar que Aij Pasa a ser Aji por lo tanto tenemos que invertir la variable del ciclo for
m1t=[]
for i in range(filas):
    for j in range(columnas):
        m1t = m1[j][i]
m2t=[]
for i in range(filas2):
    for j in range(columnas2):
        m2t = m2[j][i]
#Creamos nuestra matriz resultado de la multiplicacion para compararla con la otra matriz                
mtm=[]
#Realizamos la multiplicacion (Segun mi logica)
for i range(filas):
    for j in range(columnas):
        mtm= m2t[i][j] * m1t[i][j] #El tema aqui es que la multiplicacion no seria la correcta ya que como bien sabemos las matrices se multiplican de una forma distinta y creo que eran con 3 bucles 
if mrmt == mtm:
    print("Se cumple la propiedad")
else:
    print("Las matrices no tienen la misma cantidad de filas ni columnas")
#Spoiler codigo no funcional
#juro que para el parcial no se me van a olvidar