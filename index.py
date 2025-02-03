#Ejercicio N°6
"""
Crea una funcion llamada contar ocurrencias que reciba una lista
y un elemento, y devuelva cuantas veces aparece ese elemento en esa lista
ej lista=[1,2,2,3,2,4] 
la funcion deberia devolver 3 si el elemento es 2
"""

lista=[1,2,2,3,3,3,3,3,3,2,4] 
def contarOcurrencias(lista, elemento):
		contador=0;	
		for e in lista:
				if e== elemento:
							contador+=1;
		return f"la cantidad de ocurrencias del elemento {elemento} es de {contador}"


print(contarOcurrencias(lista,3))