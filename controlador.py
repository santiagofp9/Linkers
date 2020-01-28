from classLibro import Libro
from classLibreria import Libreria
 
 
class Controlador:
    def __init__(self):
        self.controlador = Libreria()
    
    def menu(self):
 
        while True:
 
            print("========================")
            print("Elija una opción")
            print("1.- Agregar")
            print("2.- Editar")
            print("3.- Listado")
            print("4.- Eliminar")
            print("5.- Salir")
            print("========================")

            try:
                opcion = int(input("?: "))
            except ValueError as ve:
                print("Opción no válida")
                continue

            if opcion in range(1, 5):
                self.procesar_opcion(opcion)
            elif opcion == 5:
                break
            else:
                print("Opción no válida")
 
    def procesar_opcion(self, opcion):
 
        if opcion == 1:
            self.agregar()
        elif opcion == 2:
            self.editar()
        elif opcion == 4:
            self.eliminar()
        elif opcion == 3:
            self.listar()

    def agregar(self):
        
        autor = input("Autor: ")
        titulo = input("Titulo: ")
        editorial = input("Editorial: ")
        isbn = input("ISBN: ")

        l = Libro(titulo, autor, editorial, isbn)
        self.controlador.agregar(l)

    def eliminar(self):
 
        self.listar()
        try:
            indice = int(input("Indice del libro: "))
            self.controlador.eliminar(indice)
 
        except ValueError as ve:
            print("Indice no válido")

    def listar(self):
 
        print("")
 
        for i, l in enumerate(self.controlador.libros):
            print("Id: {0}, Titulo: {1}, Autor: {2}, Editorial: {3}, ISBN: {4}".format(i, l.titulo, l.autor, l.editorial, l.isbn))


    def editar(self):
 
        self.listar()
 
        try:
 
            indice = int(input("\nIndice del libro: "))
 
            titulo = input("\nNuevo titulo: ")
            autor = input("Nuevo autor: ")
            editorial = input("Nueva editorial: ")
            isbn = input("ISBN: ")
 
            l = Libro(titulo, autor, editorial, isbn)
 
            self.controlador.editar(indice, l)
            self.listar()
 
        except ValueError as ve:
            print("Indice no válido")
    
if __name__ == "__main__":
    controlador = Controlador()
    controlador.menu()
