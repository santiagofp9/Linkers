class Libreria:


    # Métodos
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)
 
    def eliminar(self, indice):
        if indice in range(0, len(self.libros)):
            del self.libros[indice]
 
    def editar(self, indice, libro):
        if indice in range(0, len(self.libros)):
            self.libros[indice].titulo = libro.titulo
            self.libros[indice].autor = libro.autor
            self.libros[indice].editorial = libro.editorial
            self.libros[indice].isbn = libro.isbn
