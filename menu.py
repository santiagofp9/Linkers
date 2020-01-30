from classLibro import Libro

def menu():
    print("\n               ======================================")
    print("                               MENÚ                  ")
    print("               ======================================")

    print("\n1.-Ingrese libro.")
    print("2.-Consulte libros.")
    print("3.-Salir.")

def subMenu():
    print("\nDesea ingresar otro libro")
    print("\n1.-Ingresar otro libro.")
    print("2.-Regresar al menú")
    print("3.-Salir")

menu()

opcion=input("\nIngrese opción: ")

def crear():
    titulo=input("\nIngrese titulo: ")
    autor=input("Ingrese autor: ")
    editorial=input("Ingrese editorial: ")
    isbn=input("Ingrese isbn: ")
    newLibro=Libro(titulo,autor,editorial,isbn)

def consultar(file):
    print(file.read())
    file.close()


while(opcion!=3):
    print(opcion)
    if  opcion=="1":
        print("\n               ======================================")
        print("                            AGREGAR LIBRO            ")
        print("               ======================================")

        crear()
        newLibro.agregarLibro()
        print("\n")
        subMenu()
        op=input("Elija su opcion: ")
        if(op=="1"):
            x=1
        elif(op=="2"):
            menu()
        elif(op=="3"):        
            break
        else:
            print("Opción Incorrecta")
            subMenu()
            op=input("Ingrese opción: ")
    elif opcion=="2":
        newLibro.consultar()
        opcion=3
    else:
        print("Opción Incorrecta")
        menu()
        opcion=input("Ingrese opción: ")
