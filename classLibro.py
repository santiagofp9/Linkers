class Libro:

    def __init__(self,titulo,autor,editorial,isbn):
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

    def getDatos(self):
        datos=("Título: "+self.get_titulo()+", Autor: "+self.get_autor()+", Editorial: "+self.get_editorial()+", ISBN: "+self.get_isbn()+"\n")
        return datos

