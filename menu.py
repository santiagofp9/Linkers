from classLibro import Libro

def menu():
    print("\n               ======================================")
    print("                               MENÚ                  ")
    print("               ======================================")

    print("\n1.-Ingrese libro.")
    print("2.-Consulte libros.")
    print("3.-Salir.")

def subMenu():
    print("\n¿Desea ingresar otro libro?")
    print("\n1.-Ingresar otro libro.")
    print("2.-Regresar al menú")
    print("3.-Salir")

def menuLibro()
    print("\n               ======================================")
    print("                            AGREGAR LIBRO            ")
    print("               ======================================")

menu()

opcion=input("\nIngrese opción: ")

def consultar():
    file=open("biblioteca.txt","r")
    print(file.read())
    file.close()


while(opcion!=3):
    if  opcion=="1":       
        menuLibro()
        newLibro=Libro()
        newLibro.agregarLibro()
        print("\n")
        subMenu()
        op=input("Elija su opcion: ")
        if(op=="1"):
            continue
        elif(op=="2"):
            menu()
            opcion=input("Ingrese opción: ")
        elif(op=="3"):        
            break
        else:
            print("Opción Incorrecta")
            subMenu()
            op=input("Ingrese opción: ")
    elif opcion=="2":
        consultar()
        menu()
        opcion=input("Ingrese opción: ")
    elif opcion=="3":
        break
    else:
        print("Opción Incorrecta")
        menu()
        opcion=input("Ingrese opción: ")
