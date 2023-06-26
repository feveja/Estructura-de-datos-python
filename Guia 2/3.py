class Nodo:
    dato = None
    siguiente = None
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

    def mostrar_nodo(self):
        return self.dato

class ListaEnlazada:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self,nodo):
        self.nodos.append(Nodo(nodo))
        if self.esta_vacio == False:
            self.nodos[-2].siguiente = len(self.nodos)-1
        
    def esta_vacio(self):
        if len(self.nodos) == 0:
            return True
        else:
            return False
    def mostrar_lista(self):
        lista = []
        for i in range(len(self.nodos)):
            lista.append(self.nodos[i].mostrar_nodo())
        return lista
    
    def promedio(self):
        if self.esta_vacio() == False:
            suma = 0
            for i in range(len(self.nodos)):
                suma += int(self.nodos[i].mostrar_nodo())
            return suma/len(self.nodos)
        else:
            return f"La lista esta vacia"

    def desviacion_e(self):
        if self.esta_vacio() == False:
            varianza = 0
            for i in range(len(self.nodos)):
                varianza=varianza+((int(self.nodos[i].mostrar_nodo())-self.promedio())**2)
            return (varianza/len(self.nodos))**(0.5)
        else:
            return f"La lista esta vacia"
    
lista = ListaEnlazada()
opcion = ""
while type(opcion) == str:
    print("\nSeleccione la operacion a realizar\n")
    print("A. Agregar datos\nB. Calcular Media\nC. Calcular desviacion estandar\nD. Imprimir lista\nE. Verificar si la lista esta vacia\nF. Cerrar el programa\n")
    opcion = input().lower()
    if opcion == "a":
        dato = input("Dato que desea agregar: ")
        lista.agregar_nodo(dato)
    elif opcion == "b":
        print(lista.promedio())
    elif opcion == "c":
        print(lista.desviacion_e())
    elif opcion == "d":
        print(lista.mostrar_lista())
    elif opcion == "e":
        print(lista.esta_vacio())
    elif opcion == "f":
        opcion = -1
