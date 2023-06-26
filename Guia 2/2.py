class Cliente:
    def __init__(self, ticket, caja):
        self.ticket = ticket
        self.caja = caja
        self.siguiente = None


class ColaAtencion:
    def __init__(self):
        self.caja1 = None
        self.caja2 = None
        self.caja3 = None

    def agregar_cliente(self, ticket, caja):
        cliente = Cliente(ticket, caja)
        if caja == 1:
            if self.caja1 is None:
                self.caja1 = cliente
                self.caja1.siguiente = self.caja1
            else:
                temp = self.caja1
                while temp.siguiente != self.caja1:
                    temp = temp.siguiente
                temp.siguiente = cliente
                cliente.siguiente = self.caja1
        elif caja == 2:
            if self.caja2 is None:
                self.caja2 = cliente
                self.caja2.siguiente = self.caja2
            else:
                temp = self.caja2
                while temp.siguiente != self.caja2:
                    temp = temp.siguiente
                temp.siguiente = cliente
                cliente.siguiente = self.caja2
        elif caja == 3:
            if self.caja3 is None:
                self.caja3 = cliente
                self.caja3.siguiente = self.caja3
            else:
                temp = self.caja3
                while temp.siguiente != self.caja3:
                    temp = temp.siguiente
                temp.siguiente = cliente
                cliente.siguiente = self.caja3

    def atender_cliente(self, caja):
        if caja == 1 and self.caja1 is not None:
            atendido = self.caja1
            if self.caja1.siguiente == self.caja1:
                self.caja1 = None
            else:
                temp = self.caja1
                while temp.siguiente != self.caja1:
                    temp = temp.siguiente
                temp.siguiente = self.caja1.siguiente
                self.caja1 = self.caja1.siguiente
            return atendido
        elif caja == 2 and self.caja2 is not None:
            atendido = self.caja2
            if self.caja2.siguiente == self.caja2:
                self.caja2 = None
            else:
                temp = self.caja2
                while temp.siguiente != self.caja2:
                    temp = temp.siguiente
                temp.siguiente = self.caja2.siguiente
                self.caja2 = self.caja2.siguiente
            return atendido
        elif caja == 3 and self.caja3 is not None:
            atendido = self.caja3
            if self.caja3.siguiente == self.caja3:
                self.caja3 = None
            else:
                temp = self.caja3
                while temp.siguiente != self.caja3:
                    temp = temp.siguiente
                temp.siguiente = self.caja3.siguiente
                self.caja3 = self.caja3.siguiente
            return atendido

    def imprimir_cola(self, caja):
        if caja == 1:
            if self.caja1 is None:
                print("Caja 1: No hay clientes en espera")
            else:
                temp = self.caja1
                while True:
                    print(f"Caja 1: Cliente {temp.ticket}")
                    temp = temp.siguiente
                    if temp == self.caja1:
                        break
        elif caja == 2:
            if self.caja2 is None:
                print("Caja 2: No hay clientes en espera")
            else:
                temp = self.caja2
                while True:
                    print(f"Caja 2: Cliente {temp.ticket}")
                    temp = temp.siguiente
                    if temp == self.caja2:
                        break
        elif caja == 3:
            if self.caja3 is None:
                print("Caja 3: No hay clientes en espera")
            else:
                temp = self.caja3
                while True:
                    print(f"Caja 3: Cliente {temp.ticket}")
                    temp = temp.siguiente
                    if temp == self.caja3:
                        break

# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("----- Menú -----")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar cola de una caja")
    print("4. Salir")
    opcion = int(input("Ingrese la opción deseada: "))
    return opcion

# Crear una instancia de ColaAtencion
cola = ColaAtencion()

while True:
    opcion = mostrar_menu()

    if opcion == 1:
        ticket = int(input("Ingrese el número de ticket: "))
        caja = int(input("Ingrese el número de caja (1, 2 o 3): "))
        cola.agregar_cliente(ticket, caja)
        print("Cliente agregado a la cola.")

    elif opcion == 2:
        caja = int(input("Ingrese el número de caja (1, 2 o 3): "))
        cliente_atendido = cola.atender_cliente(caja)
        if cliente_atendido is not None:
            print(f"Cliente {cliente_atendido.ticket} atendido en la caja {caja}.")
        else:
            print("No hay clientes en la cola de esa caja.")

    elif opcion == 3:
        caja = int(input("Ingrese el número de caja (1, 2 o 3): "))
        cola.imprimir_cola(caja)

    elif opcion == 4:
        print("Adios.")
        break

    else:
        print("Opción inválida. Por favor, intente nuevamente.")