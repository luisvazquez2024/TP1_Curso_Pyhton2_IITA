#Ejercicio N°1
listaNumeros=[10,2,5,1,4,9];
desordenados=[100,5,101,500,2,65,1000,6,8,3,1]

def funcionOrdenadora(lista):
	n=len(lista);
	temporario=0;
	for i in range(n):  
		for j in range(n-i-1):
				if lista[j]>lista[j+1]:
					temporario=lista[j];				
					lista[j]=lista[j+1];
					lista[j+1] = temporario;  
	return lista;
  
print(funcionOrdenadora(listaNumeros))
print(funcionOrdenadora(desordenados))


