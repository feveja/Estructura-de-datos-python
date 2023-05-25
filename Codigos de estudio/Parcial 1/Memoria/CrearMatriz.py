import random
def matrizaleatoria(filas,columnas):
    M = []
    for _ in range(filas):
        Mp=[]
        for _ in range(columnas):
            elemento = random.randint(1,10)
            Mp.append(elemento)
        M.append(Mp)
    return M        
def crearmatriz(filas,columnas):
    matriz = []
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            elemento = int(input(f"ingrese el elemento:[{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(filas)
    return matriz            
def suma(matriza,matrizb):
    filas = len(matriza)
    columnas= len(matriza[0])
    Total=[]
    for i in range(filas):
        filas_suma=[]
        for j in range(columnas):
            aux = matriza[i][j]+matrizb[i][j]
            filas_suma.append(aux)
        Total.append(filas_suma)
    return Total
def resta(matriza,matrizb):
    filas = len(matriza)
    columnas= len(matriza[0])
    Total=[]
    for i in range(filas):
        filas_resta=[]
        for j in range(columnas):
            aux = matriza[i][j]-matrizb[i][j]
            filas_resta.append(aux)
        Total.append(filas_resta)
    return Total
def multiplicacionEscalar(matriz,escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    Resultado = []
    for i in range(filas):
        filas_resultado = []
        for j in range(columnas):
            pepito = matriz[i][j] * escalar
            filas_resultado.append(pepito)
        Resultado.append(filas_resultado)
    return Resultado
def multiplicar(matrizd,matrizc):
    filas1 = len(matrizd)
    columnas1= len(matrizd[0])
    filas2 = len(matrizc)
    columnas2= len(matrizc[0])
    if columnas1 != filas2:
        print("No se pueden multiplicar las matrices. Las dimensiones no coinciden.")
        return None
    resultado = [[0] * columnas2 for _ in range(filas1)]
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                resultado[i][j] += matrizd[i][k] * matrizc[k][j]
    return resultado 
def crear_matriz_identidad(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = 1
    return matriz 
##################################################
M1 = matrizaleatoria(3,3) 
M2 = matrizaleatoria(3,3)
Mr = multiplicar(M1,M2)
Mi = crear_matriz_identidad(3)
Mrf= multiplicar(Mr,Mi)
print(Mrf)