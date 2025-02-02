#Ejercicio N°3
"""
Dados dos conjuntos de numeros, escribe un programa para encontrar los
numeros que faltan en el segundo conjunto en comparacion con 
el primero y viceversa.

"""
conjunt1= {1,2,3,4,5,6}
conjunt2= {5,6,7,8,9,10}

def encontrarNumeroFaltantes(conj1, conj2):
  elementosFaltantes2 = conj1 - conj2;
  elementosFaltantes1 = conj2 - conj1;
  
  return (f"Los numeros que faltan el conjunto 1 son {elementosFaltantes1} y los numeros faltantes en el conjunto 2 son {elementosFaltantes2}");

print(encontrarNumeroFaltantes(conjunt1,conjunt2))