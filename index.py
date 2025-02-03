#Ejercicio N°5
"""
Crea una funcion llamada factorial que reciba un numero entero positivo
y devuelva su factorial . ejemplo factorial(4) debe devolver 24.
"""


def factorial(n):
  if n<0:
    print("El numero debe ser positivo..!");
  elif n ==0 | n == 1:
    return 1;
  else:
    res =1;
    for i in range(2,n+1):
      res*=i;
    return res;        




print(factorial(0)); 
print(factorial(3)); 
print(factorial(4)); 