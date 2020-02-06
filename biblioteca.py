from classLibro import Libro

class Biblioteca:
    
    def __init__(self):
        self.nombre="Biblioteca Tomillo"
        
    def menu_inicial(self):
        print("\n               ======================================")
        print("                               MENÚ                  ")
        print("               ======================================")

        print("\n1.-Ingrese libro.")
        print("2.-Mostrar Biblioteca")
        print("3.-Consultar libros.")
        print("4.-Eliminar libros.")
        print("5.-Salir.")

    def subMenu(self):
        print("\n¿Desea ingresar otro libro?")
        print("\n1.-Ingresar otro libro.")
        print("2.-Regresar al menú")
        print("3.-Salir")

    def agregar(self):    
        titulo = str(input("TITULO: "))
        autor = str(input("AUTOR: "))
        editorial = str(input("EDITORIAL: "))
        isbn = str(input("ISBN: "))

        libro = Libro(titulo, autor, editorial, isbn)
        f = open("biblioteca.txt", "a")
        f.close()

        f = open("biblioteca.txt", "r")

        
        if str.lower(titulo) in str.lower(f.read()):
            print("Ese libro ya existe")
        else:
            f.close()
            f = open("biblioteca.txt", "at")
            f.write(libro.getDatos()) 
            f.close()
            print("Agregado con éxito")

    def listar(self):
        f = open("biblioteca.txt", "r")
        contenido = f.readlines()
        for i in contenido:
            print(i) 
        f.close()

    def consultar(self):
        f = open("biblioteca.txt", "r")
        
        buscar = input("Ingrese la palabra por la que quiera buscar: ")  
        if buscar != "":
            exists = False
            for i in f.readlines():
                if str.lower(buscar) in str.lower(i):
                    exists = True
                    print("\n"+i)
            if not exists: 
                print("No hay registros con esos datos")
        else:
            print("Consulta vacía")
        f.close()

    def eliminar(self):
        try:
            f = open('biblioteca.txt','r+')
            contenido = f.readlines()
            for i in enumerate(contenido):
                print(i[0], " - " ,i[1][:-1])        
            
            seleccion = int(input("\nElija el libro que desea eliminar o escribe '666' para cancelar ->  "))
            f.close()

            if seleccion <= (len(contenido) - 1):
                f = open('biblioteca.txt', 'w+')
                for i in contenido:
                    if i != contenido[seleccion]:   
                        f.write(i)   
                print("\n            =============== Eliminado con éxito =================")
            elif seleccion == 666:
                f.close()
                return
            else:
                print("Indice no válido")
            f.close()
        except ValueError:
            print("\nNo se permiten letras ni caracteres especiales")

    def iniciar(self,opcion):
        while(opcion!=3):
            if  opcion=="1":       
                print("\n                       =============== Agregar ==============\n")
                self.agregar()
                print("\n")
                self.subMenu()
                op=input("Elija su opcion: ")
                if(op=="1"):
                    continue
                elif(op=="2"):
                    self.menu_inicial()                    
                    opcion=input("\nIngrese opción: ")
                elif(op=="3"):        
                    break
                else:
                    print("Opción Incorrecta")
                    self.subMenu()
                    op=input("\nIngrese opción: ")
            elif opcion=="2":
                print("\n                       =============== BIBLIOTECA ==============\n")
                self.listar()
                self.menu_inicial()
                opcion=input("\nIngrese opción: ")
            elif opcion=="3":
                print("\n                       =============== Busqueda ==============\n")
                self.consultar()
                self.menu_inicial()
                opcion=input("\nIngrese opción: ")
            elif opcion=="4":
                print("\n                       =============== Eliminar ==============\n")
                self.eliminar()
                self.menu_inicial()
                opcion=input("\nIngrese opción: ")
            elif opcion=="5":
                print("\n                =================== Hasta Pronto ==================")
                break
            else:
                print("Opción Incorrecta")
                self.menu_inicial()
                opcion=input("\nIngrese opción: ")


