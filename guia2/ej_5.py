#Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos.

#Variables

num1 = int(0)
num2 = int(0)

#Pedido de numeros a usuarios

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero distinto al primero: "))

#Logica

if num1 > num2:
  print(f"{num1} es mayor que {num2}")

elif num2 > num1:
  print(f"{num2} es mayor que {num1}")