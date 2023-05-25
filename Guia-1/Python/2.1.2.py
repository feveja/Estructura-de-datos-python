#list list -> list
#Funcion que multiplica matrices
#Ej:matriz1 = [[2,1],[3,5]] 
#   matriz2 = [[1,1,2],[0,1,3]]
#   multiplicar_matrices(matriz1,matriz2) -> [[2,3,7],[3,8,21]]
def multiplicar_matrices(a,b):
    filas_a = len(a)
    columnas_a = len(a[0])
    filas_b = len(b)
    columnas_b = len(b[0])
    if columnas_a == filas_b:
        resultado = []
        #Recorro filas de A (i)
        for i in range(filas_a):
            #Por cada fila de a se crea una fila de la matriz resultado
            fila_resultado = []
            #Recorriendo columnas de B (j)
            for j in range(columnas_b):
                #Por cada recorrido de columnas de B se crea un elemento de la fila resultado
                suma = 0
                #Recorro filas de B (k)
                for k in range(filas_b):
                    #Por cada fila de A, avanzare por cada columna de B
                    #avanzando en A las filas de B y en B las filas de B
                    suma+= a[i][k]*b[k][j]
                #Una vez que termino de avanzar por todas las filas de B se creo un elemento de la fila resultado
                #Lo añado a la fila resultado
                fila_resultado.append(suma)
            #Una vez que se recorrieron todas las columnas con la fila i de A se añade esa fila resultado a la matriz resultado
            resultado.append(fila_resultado)
        return resultado
    else:
        return None

matriz = [[1,2,1],[0,1,1],[1,3,1]]
matriz_inversa = [[2,-1,-1],[-1,0,1],[1,1,-1]]

#Al multiplicar la matriz con su matriz inversa llego a la matriz identidad
print(f"Matriz A: \n {matriz}")
print(f"Matriz inversa de A: \n {matriz_inversa}")
print(f"Resultado de multiplicar AxA^-1: \n{multiplicar_matrices(matriz,matriz_inversa)}")
print(f"Es identidad => Se cumple la propiedad")