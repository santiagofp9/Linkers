class Libro:
    titulo=''
    autor=''
    editorial=''
    isbn=''
    
    def __init__(self):
        self.titulo=titulo
        self.autor=autor     
        self.editorial=editorial
        self.isbn=isbn
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo
    
    def set_autor(self,autor):
        self.autor=autor

    def get_autor(self):
        return self.autor
    
    def set_editorial(self,editorial):
        self.editorial=editorial

    def get_editorial(self):
        return self.editorial
    
    def set_isbn(self,isbn):
        self.isbn=isbn

    def get_isbn(self):
        return self.isbn

    def agregarLibro(self):
        self.biblioteca = open("biblioteca.txt", "at")
        self.biblioteca.write(self.get_titulo()+", "+self.get_autor()+", "+self.get_editorial()+", "+self.get_isbn()+"\n")
        self.biblioteca.close()

