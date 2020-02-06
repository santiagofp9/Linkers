class Libro:
	def __init__(self, titulo, autor, editorial, isbn):
		self.titulo = titulo;
		self.autor = autor;
		self.editorial = editorial;
		self.isbn = isbn;

	def setTitulo(self, titulo):
		self.titulo = titulo

	def getTitulo(self):
		return self.titulo

	def setAutor(self, autor):
		self.autor = autor

	def getAutor(self):
		return self.autor

	def setEditorial(self, editorial):
		self.editorial = editorial

	def getEditorial(self):
		return self.editorial

	def setISBN(self, isbn):
		self.isbn = isbn

	def getISBN(self):
		return self.isbn

#libro1 = Libro("La Sombra del Viento", "Carlos Ruíz Zafón", "Planeta", "9788408043645");