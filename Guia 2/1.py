#El nodo en este caso representa una cancion de la lista de reproduccion y cada cancion tiene titulo y artista 
class Nodo:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def esta_vacia(self):
        return self.primero is None
    def agregar_cancion(self, titulo, artista):
        nueva_cancion = Nodo(titulo, artista)
        if self.primero is None:
            self.primero = nueva_cancion
            self.ultimo = nueva_cancion
        else:
            nueva_cancion.anterior = self.ultimo
            self.ultimo.siguiente = nueva_cancion
            self.ultimo = nueva_cancion
    def cancion_sonando(self):
        if self.esta_vacia():
            print("No hay nada sonando")
        else:
            actual = self.primero
            print(f"Título: {actual.titulo}, Artista: {actual.artista}")
    def pasar_anteriorcancion(self):
        if self.esta_vacia() or self.primero.anterior is None:
            print("No hay canción anterior")
        else:
            actual = self.primero
            while actual is not None:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                actual = actual.siguiente
    def pasar_siguientecancion(self):
        if self.esta_vacia() or self.ultimo.siguiente is None:
            print("No hay canción siguiente")
        else:
            actual = self.primero
            while actual is not None:
                actual.siguiente.anterior = actual.anterior
                actual.anterior.siguiente = actual.siguiente
                actual = actual.siguiente
    def terminar_cancion(self):
        if self.esta_vacia():
            print("No hay canciones para terminar")
        else:
            self.primero = None
            self.ultimo = None
    def eliminar_cancion(self, titulo):
        actual = self.primero
        while actual is not None:
            if actual.titulo == titulo:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                break
            actual = actual.siguiente
    def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacía")
        else:
            actual = self.primero
            while actual is not None:
                print(f"Título: {actual.titulo}, Artista: {actual.artista}")
                actual = actual.siguiente
def mostrar_menu():
    print("---- Menú ----")
    print("1. Agregar canción")
    print("2. Mostrar canción sonando")
    print("3. Pasar a la canción anterior")
    print("4. Pasar a la siguiente canción")
    print("5. Terminar canción")
    print("6. Eliminar canción")
    print("7. Mostrar lista de reproducción")
    print("8. Salir")
# Crear una instancia de la lista de reproducción
lista_reproduccion = ListaReproduccion()
while True:
    mostrar_menu()
    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == "1":
        titulo = input("Ingrese el título de la canción: ")
        artista = input("Ingrese el nombre del artista: ")
        lista_reproduccion.agregar_cancion(titulo, artista)
        print("Canción agregada exitosamente.")

    elif opcion == "2":
        lista_reproduccion.cancion_sonando()

    elif opcion == "3":
        lista_reproduccion.pasar_anteriorcancion()

    elif opcion == "4":
        lista_reproduccion.pasar_siguientecancion()

    elif opcion == "5":
        lista_reproduccion.terminar_cancion()

    elif opcion == "6":
        titulo = input("Ingrese el título de la canción a eliminar: ")
        lista_reproduccion.eliminar_cancion(titulo)

    elif opcion == "7":
        lista_reproduccion.mostrar_lista()

    elif opcion == "8":
        print("Adios.")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 8 para seleccionar una opción.")