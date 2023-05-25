import random as ran

n = ran.randint(3,5)

matriz = []
for i in range(n):
    aux = []
    for j in range(n):
        aux.append(ran.randint(1,3))
    matriz.append(aux)

def matrizastr(m:list):
    aux_str = ""
    for i in range(len(m)):
        aux_str += str(m[i]) + "\n"
    return aux_str

def escalarxfila(escalar:float,fila:int,matriz:list):
    for i in range(len(matriz[fila])):
        matriz[fila][i] = matriz[fila][i]*escalar
    return None

def restarfilas(fila1:list,fila2:list):
    for i in range(len(fila1)):
        fila1[i] = fila1[i]-fila2[i]
    return None

def crear_identidad(a:list):
    filas = len(a)
    columnas = len(a[0])
    if filas == columnas:
        identidad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            identidad.append(fila)
        return identidad
    else:
        return None

def aumentar_matriz(a:list,b:list):
    if len(a)==len(b):
        for i in range(len(a)):
            a[i] += b[i]
        return a
    else:
        return None

matriz_identidad = crear_identidad(matriz)

#Aumentar
print(f"La matriz original es \n{matrizastr(matriz)}")
matriz_a = aumentar_matriz(matriz,matriz_identidad)
print(f"La matriz aumentada con su identidad es: \n{matrizastr(matriz_a)}")

#Triangular la matriz

for j in range(n):
    for i in range(n):
        if i>=j:
            escalarxfila(1/matriz_a[i][j],i,matriz_a)
    for i in range(n-1):
        if i>=j:
            restarfilas(matriz_a[i+1],matriz_a[j])

print(f"{matrizastr(matriz_a)}")