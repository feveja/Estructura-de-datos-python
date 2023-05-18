def cantidad_de_digitos(numero):
    if numero == 0:
        return 1
    count = 0
    while numero > 0:
        count += 1
        numero //= 10
    return count


def posicion(numero, indice, reversa):
    if reversa:
        numero = str(numero)[::-1]
    else:
        numero = str(numero)
    return int(numero[indice])


def reemplazar(numero, indice, nuevo, reversa):
    if reversa:
        numero = str(numero)[::-1]
        numero = int(str(nuevo) + str(numero)[1:])
        numero = int(str(numero)[::-1])
    else:
        numero = str(numero)
        numero = int(numero[:indice] + str(nuevo) + numero[indice + 1:])
    return numero
print(reemplazar(1810, 0, 2, False))