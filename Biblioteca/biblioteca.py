from libro import Libro;

class Biblioteca:
	
	def __init__(self, nombAr, modo):
		self.nombreArchivo = nombAr;
		self.estanteria = open(self.nombreArchivo, modo);
		self.libro = Libro("", "", "", "");

	def modEstanteria(self, modo):
		self.estanteria = open(self.nombreArchivo, modo);

	def numLibros(self):
		self.modEstanteria("r");
		n = len(self.estateria.readlines());
		self.estanteria.close();
		return n;

	def yaAgregado(self):
		with open(self.nombreArchivo) as est:
			libros = est.readlines();
			l.lower() for l in libros;
			if(", ISBN: "+self.libro.getISBN()+"\n").lower() in libros:
				return True;
			else:
				return False;

	def listarLibros(self):
		self.modEstanteria("r")
		print(self.estanteria.read());
		self.estanteria.close();

	def agregarLibro(self):
		self.libro.setTitulo(input("Introduzca el título:\n"));
		self.libro.setAutor(input("Introduzca el autor:\n"));
		self.libro.setEditorial(input("Introduzca la editorial:\n"));
		self.libro.setISBN(input("Introduzca el I.S.B.N.:\n"));
		if(self.yaAgregado()):
			print("El libro indicado ya se había agregado anteriormente.");
		else:
			self.modEstanteria("at");
			self.estanteria.write("Título: "+self.libro.getTitulo()+", Autor: "+self.libro.getAutor()+", Editorial: "+self.libro.getEditorial()+", ISBN: "+self.libro.getISBN()+"\n");
			self.estanteria.close();
			print("Libro agregado con éxito.");
		self.libro.setTitulo("");
		self.libro.setAutor("");
		self.libro.setEditorial("");
		self.libro.setISBN("");

	def consultarLibro(self):
		opcion = int(input("¿Buscar por Título o por Autor? [1: Título; 2: Autor] (Introduce el número de la opción):\n"));
		while(opcion<1 or opcion>2):
			opcion = int(input("Fuera de rango.\n¿Buscar por Título o por Autor? [1: Título; 2: Autor] (Introduce el número de la opción):\n"));
		if(opcion==1):
			self.libro.setTitulo(input("Introduzca el título:\n"));
			if(self.yaAgregado()):
				with open(self.nombreArchivo) as est:
					libros = est.readlines();
					l.lower() for l in libros;
					for l in libros:
						if ("Título: "+self.libro.getTitulo()).lower() in l:
							print(l);
			else:
				print("Libro no encontrado.");
		elif(opcion==2):
			self.libro.setAutor(input("Introduzca el autor:\n"));
			if(self.yaAgregado()):
				with open(self.nombreArchivo) as est:
					libros = est.readlines();
					l.lower() for l in libros;
					for l in libros:
						if ("Autor: "+self.libro.getAutor()).lower() in l:
							print(l);
			else:
				print("Libro no encontrado.");
	self.libro.setTitulo("");
	self.libro.setAutor("");