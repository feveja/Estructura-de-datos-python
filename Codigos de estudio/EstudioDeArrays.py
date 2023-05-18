def cantidad_de_digitos(numero):
    return len(str(numero))

def en_posicion(numero, indice, reversa):
    numero_str = str(numero)
    if reversa:
        numero_str = numero_str[::-1]
    return int(numero_str[indice])

def reemplazar(numero, indice, nuevo, reversa):
    numero_str = str(numero)
    if reversa:
        numero_str = numero_str[::-1]
    numero_str = numero_str[:indice] + str(nuevo) + numero_str[indice+1:]
    if reversa:
        numero_str = numero_str[::-1]
    return int(numero_str)

print(reemplazar(1810, 0, 2, False))