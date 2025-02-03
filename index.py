#Ejercicio N°7
"""
Crea una funcion funcion recursiva llamada suma_recursiva que reciba un numero n
y devuelva la suma de los primeros n numeros naturales, ej suma_recursica(5)
 debe devolver 15(1+2+3+4+5)

"""


def suma_recursiva(n):
		suma=0;	
		i =1;	
		while(i <= n):
				#print(i)
				suma+=i;
				i+=1;
		return suma;
print(suma_recursiva(5))


