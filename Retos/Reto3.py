aux = input("Ingrese la palabra: \n")
vocales= {"a":0,"e":0,"i":0,"o":0,"u":0}
for letra in aux:
    if letra.lower() in vocales:
        vocales[letra.lower()]+=1
print("La palabra ",aux,"contiene:")
for vocal, cantidad in vocales.items():
    print(cantidad,"ocurrencias de vocal",vocal)
