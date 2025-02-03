#Ejercicio N°4
"""
Escriba un programa en python para eliminar todos los duplicados
de una lista de cadenas dada y devolver una lista de cadena unica
"""

lista=['a', 'b','b','c','d','d', 'e'];
lista1=['a','a', 'a','b','b','c','c','d','d', 'e'];

cadena=["Perro", "Gato", "Perro", "Oso","oso","Elefante"]


def listaCadenaUnica(lista):
	listminus=[i.lower() for i in lista]
	nuevaLista=[];
	for i in listminus:
		if i not in nuevaLista:
			nuevaLista.append(i);	
	return nuevaLista		
  

print(listaCadenaUnica(cadena))
print(listaCadenaUnica(lista))
print(listaCadenaUnica(lista1))
   
 