from libro import Libro

class Menu:
    
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

    def menuLibro(self):
        print("\n               ======================================")
        print("                            AGREGAR LIBRO            ")
        print("               ======================================")

    def iniciar(self,opcion):
        while(opcion!=3):
            if  opcion=="1":       
                menu1.menuLibro()
                newLibro=Biblioteca()
                newLibro.agregarLibro()
                print("\n")
                menu1.subMenu()
                op=input("Elija su opcion: ")
                if(op=="1"):
                    continue
                elif(op=="2"):
                    menu1.menu_inicial()
                    opcion=input("Ingrese opción: ")
                elif(op=="3"):        
                    break
                else:
                    print("Opción Incorrecta")
                    menu1.subMenu()
                    op=input("Ingrese opción: ")
            elif opcion=="2":
                newLibro.consultarLibro()
                menu1.menu_inicial()
                opcion=input("Ingrese opción: ")
            elif opcion=="4":
                print()
            elif opcion=="5":
                break
            else:
                print("Opción Incorrecta")
                menu1.menu_inicial()
                opcion=input("Ingrese opción: ")

menu1=Menu()
menu1.menu_inicial()
opcion=input("\nIngrese opción: ")
menu1.iniciar(opcion)


