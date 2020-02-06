from classLibro import Libro


def procesar_opcion(opcion): 
    if opcion == 1:
        agregar()
    elif opcion == 2:
        editar()  
    elif opcion == 3:
        listar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        buscar()


def buscar():
    f = open("biblioteca.txt", "r")
    
    buscar = input("Ingrese la palabra por la que quiera buscar -> ")  
    if buscar != "":
        exists = False
        for i in f.readlines():
            if str.lower(buscar) in str.lower(i):
                exists = True
                print(i)
        if not exists: 
            print("No hay registros con esos datos")
    else:
        print("Consulta vacía")
    f.close()


def agregar():
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


def listar():
    f = open("biblioteca.txt", "r")
    contenido = f.readlines()
    for i in contenido:
        print(i) 
    f.close()
    

def eliminar():
    f = open('biblioteca.txt','r+')
    contenido = f.readlines()
    for i in enumerate(contenido):
        print(i[0], " - " ,i[1][:-1])
    seleccion = int(input("Elija el libro que desea eliminar o escribe '666' para cancelar ->  "))
    f.close()

    if seleccion <= (len(contenido) - 1):
        f = open('biblioteca.txt', 'w+')
        for i in contenido:
            if i != contenido[seleccion]:   
                f.write(i)   
        print("Eliminado con éxito")
    elif seleccion == 666:
        f.close()
        return
    else:
        print("Indice no válido")
    f.close()
    

def editar():
    f = open('biblioteca.txt','r+')
    contenido = f.readlines()
    for i in enumerate(contenido):
        print(i[0], " - " ,i[1][:-1])
    seleccion = int(input("Elija el libro que desea editar o escribe '666' para cancelar ->  "))
    f.close()

    if seleccion <= (len(contenido) - 1):
        f = open('biblioteca.txt', 'w+')
        for i in contenido:
            if i != contenido[seleccion]:   
                f.write(i)   
            else:
                f.close()
                agregar()
        print("Editado con éxito")
    elif seleccion == 666:
        f.close()
        return
    else:
        print("Indice no válido")
    f.close()


while True:
 
    print("========================")
    print("======    MENÚ    ======")
    print("========================")
    print("Elija una opción")
    print("1.- Agregar")
    print("2.- Editar")
    print("3.- Listado")
    print("4.- Eliminar")
    print("5.- Buscar")
    print("6.- Salir")

    try:
        opcion = int(input("->: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion in range(1, 6):
        procesar_opcion(opcion)
    elif opcion == 6:
        break
    else:
        print("Opción no válida")


