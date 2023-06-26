class Nodo:
    def __init__(self,nombre,cargo,padre=None):
        self.nombre = nombre
        self.cargo = cargo
        self.padre = padre
    def get_nombre(self):
        return self.nombre
    def get_cargo(self):
        return self.cargo
    def get_padre(self):
        return self.padre
    def cambiar_padre(self,nuevo_padre):
        self.padre = nuevo_padre
    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}"
    
class Arbol:
    def __init__(self):
        self.niveles = []
        self.raiz =None
    def agregar_nivel(self):
        self.niveles.append([])
    #retorna True si el nodo es agregado correctamente
    #retorna False si el nodo no pudo ser agregado
    def agregar_nodo(self,nodo):
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_nombre() == nodo.get_nombre():
                    return False
                
        if self.raiz == None:
            if nodo.get_padre() == None:
                self.raiz = nodo
                self.agregar_nivel()
                self.niveles[0].append(nodo)#añadir y hacer raiz
                return True
            else:
                return False
        else:
            padre_auxiliar = nodo.get_padre()
            for i in range(len(self.niveles)):
                for j in range(len(self.niveles[i])):
                    if padre_auxiliar == self.niveles[i][j].get_nombre():
                        try:
                            self.niveles[i+1].append(nodo)
                        except:
                            self.agregar_nivel()
                            self.niveles[i+1].append(nodo)
            return True
    def borrar_nodo(self,nombre):
        nombre = nombre.lower()
        nodo = None
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_nombre() == nombre:
                    nodo = self.niveles[i][j]
        if nodo != None:
            for i in range(len(self.niveles)):
                if nodo in self.niveles[i]:
                    try:
                        for j in range(len(self.niveles[i+1])):
                            if self.niveles[i+1][j].get_padre() == nodo.get_nombre():
                                self.niveles[i+1][j].cambiar_padre(nodo.get_padre())
                                aux = self.niveles[i+1][j]
                                self.niveles[i].append(aux)
                                self.niveles[i+1].remove(aux)
                    except:
                        pass
                    self.niveles[i].remove(nodo)
            return True
        else:
            return False
        
    def buscar_nodo(self, nombre):
        nombre = nombre.lower()
        hijos = []
        nodo = None
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_nombre() == nombre:
                    nodo = self.niveles[i][j]
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_padre() == nombre:
                    hijos.append(self.niveles[i][j])
        
        hijos_aux = []
        for i in range(len(hijos)):
            hijos_aux.append(hijos[i].get_nombre())
        if nodo != None:
            return [nodo.get_nombre(),nodo.get_cargo(),hijos_aux]
        else:
            return None
    def buscar_padre(self,nombre):
        nombre = nombre.lower()
        nodo = None
        padre = None
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_nombre() == nombre:
                    nodo = self.niveles[i][j]
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                if self.niveles[i][j].get_nombre() == nodo.get_padre():
                    padre = self.niveles[i][j]
        
        if padre != None:
            return [padre.get_nombre(),padre.get_cargo()]
        else:
            return None
    def mostrar_arbol(self):
        jerarquia = ""
        for i in range(len(self.niveles)):
            for j in range(len(self.niveles[i])):
                jerarquia += str(self.niveles[i][j].get_nombre())
            jerarquia += "\n"
        return jerarquia
    
jerarquia = Arbol()

opcion = ""
while type(opcion) == str:
    print("Seleccione la opcion")
    print("A.Agregar empleado\nB.Eliminar empleado\nC.Mostrar jerarquia\nD.Buscar empleado\nE.Obtener Jefe directo")
    print("F.Salir")
    opcion = input().lower()
    if opcion == "a":
        nombre = input("Nombre del empleado: ").lower()
        cargo = input("Cargo del empleado: ").lower()
        jefe = input("Tiene jefe? Si: Ingresar nombre del jefe / No: Deje en blanco: ").lower()
        if jefe != "":
            resultado = jerarquia.agregar_nodo(Nodo(nombre,cargo,jefe))
        else:
            resultado = jerarquia.agregar_nodo(Nodo(nombre,cargo))
        if resultado == True:
            print("El empleado fue agregado a la jerarquia")
        else:
            print("El empleado no pudo ser agregado")
    elif opcion == "b":
        nombre= input("Nombre del empleado: ").lower()
        jerarquia.borrar_nodo(nombre)
    elif opcion == "c":
        print(jerarquia.mostrar_arbol())
    elif opcion == "d":
        nombre = input("Nombre del empleado: ").lower()
        datos = jerarquia.buscar_nodo(nombre)
        if datos != None:
            print(f"El empleado buscado fue: {datos[0]}")
            print(f"Su cargo es: {datos[1]} y los empleados a su cargo son {datos[2]}")
        else:
            print(f"El empleado no existe")
    elif opcion == "e":
        nombre = input("Nombre del empleado: ").lower()
        datos = jerarquia.buscar_padre(nombre)
        if datos != None:
            print(f"El empleado buscado fue {nombre}")
            print(f"Su cargo es: {cargo}")
            print(f"Su jefe es: {datos[0]}, el cargo de su jefe es {datos[1]}")
        else:
            print(f"El empleado no existe")
    elif opcion == "f":
        opcion = -1