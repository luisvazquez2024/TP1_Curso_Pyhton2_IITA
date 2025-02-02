#Ejercicio N°2
"""
Crear un programa que permita crear un conjunto desde cero y 
despues me permita eliminar un elemento de un conjunto si esta presente en 
el conjunto
"""

def crearConjunto(*args):
	conjunto = set(args);
	return conjunto;

conjunto1 =crearConjunto(1,5,5,6,8,10,5,3,5,9)
conjunto2 =crearConjunto(10,50,500,6,8,1000,50,30,50,90)
 
#print(conjunto1)

def eliminarElementoConjunto(elemento,conjunto):
		if elemento in conjunto:
				conjunto.discard(elemento);
				return f'El elemento {elemento} a sido eliminado, el conjunto resultante es {conjunto}'
		else: 
				return(f"elemento {elemento} no fue encontrado el conjunto queda {conjunto}")

resultado1 = eliminarElementoConjunto(1,conjunto1);
resultado2 = eliminarElementoConjunto(1,conjunto2);

print(resultado2)
print(resultado1)


