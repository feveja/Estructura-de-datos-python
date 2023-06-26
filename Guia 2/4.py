class Cola:
    def __init__(self):
        self.elementos = []
        self.primero = None
        self.ultimo = None
    #Coloca el elemento dado al final de la cola
    def encolar_elemento(self,elemento):
        self.ultimo = elemento
        if self.esta_vacia() == True:
            self.primero = elemento
        self.elementos.append(elemento)
    #Quita el ultimo elemento de la cola
    def desencolar_elemento(self):
        self.elementos.pop(0)
        self.primero = self.elementos[0]
    #Entrega si la cola esta vacia
    def esta_vacia(self):
        if len(self.elementos) == 0:
            return True
        else:
            return False
    def mostrar_cola(self):
        return self.elementos
    def primer_elemento(self):
        return self.primero
    def ultimo_elmento(self):
        return self.ultimo
    
class Pila:
    def __init__(self):
        self.elementos = []
        self.ultimo = None
    def agregar_elemento(self,elemento):
        self.ultimo = elemento
        self.elementos.append(elemento)
    def quitar_elemento(self):
        self.elementos.pop(-1)
        self.ultimo = self.elementos[-1]
    def esta_vacia(self):
        if len(self.elementos) == 0:
            return True 
        else:
            return False
    def ultimo_elemento(self):
        return self.ultimo
    def mostrar_pila(self):
        return self.elementos
    


cola = Cola()
pila = Pila()

opcion = ""

while type(opcion) == str:
    print("\nSeleccione la opcion que desea\n")
    print("A. Agregar producto\nB. Enviar producto a despacho\nC. Despachar producto")
    print("D. Verificar si la pila de productos recibidos esta vacia\nE. Verificar si la cola de productos para despachar esta vacia")
    print("F. Imprimir lista de productos recibidos\nG. Imprimir lista de productos para despachar\nH. Mostrar cantidad total de productos en el almacen")
    print("I. Salir\n")
    opcion = input().lower()
    if opcion == "a":
        producto = input("Ingrese el producto por agregar: ")
        pila.agregar_elemento(producto)
    elif opcion == "b":
        if pila.esta_vacia() == False:
            cola.encolar_elemento(pila.ultimo_elemento())
            pila.quitar_elemento()
        else:
            print("La pila de productos recibidos esta vacia")
    elif opcion == "c":
        if cola.esta_vacia() == False:
            cola.desencolar_elemento()
        else:
            print("La cola de productos para despacho esta vacia")
    elif opcion == "d":
        if pila.esta_vacia() == True:
            print("La pila de productos recibidos esta vacia")
        else:
            print("La pila de productos recibidos no esta vacia")
    elif opcion == "e":
        if cola.esta_vacia() == True:
            print("La cola de productos por despachar esta vacia")
        else:
            print("La cola de productos por despachar no esta vacia")
    elif opcion == "f":
        print(f"La pila de productos recibidos es: {pila.mostrar_pila()}")
    elif opcion == "g":
        print(f"La cola de productos por despachar es: {cola.mostrar_cola()}")
    elif opcion == "h":
        print(f"La cantidad total de productos es: {(len(pila.mostrar_pila())+len(cola.mostrar_cola()))}")
    elif opcion == "i":
        opcion = -1