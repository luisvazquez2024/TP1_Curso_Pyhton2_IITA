#Ejercicio N°8
"""
Crea una clase Libro con los atributos titulo, autor , y año_publicacion.  
Luego crea una subclase llamada LibroDigital 
que tenga un atributo adicional   

"""

class Libro:
  def __init__(self, titulo, autor, año_publicacion):
			self.titulo=titulo;
			self.autor=autor;
			self.año_publicacion= año_publicacion;


class LibroDigital(Libro):
	def __init__(self, titulo, autor, año_publicacion, genero):
		super().__init__(titulo, autor, año_publicacion)
		self.genero=genero;
	def mostrar_informacion(self):
			print(f'Este es un libro llamado {self.titulo} y es del autor {self.autor} publicado en el año {self.año_publicacion}. y versa sobre {self.genero}')
  
  
  
LibroDigitalCiencia=LibroDigital("La ciencia","LV",1888,"ciencia ficcion")


LibroDigitalCiencia.mostrar_informacion()