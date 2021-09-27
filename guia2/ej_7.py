# Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir una leyenda según sea: equilátero, isósceles o escálenos.

#Variables
l1 = 0 #Lado 1
l2 = 0 #Lado2
l3 = 0 #Lado3

#Ingreso de datos
l1 = int(input("Ingrese la medida del primer lado del triangulo: "))
l2 = int(input("Ingrese la medida del segundo lado del triangulo: "))
l3 = int(input("Ingrese la medida del tercer lado del triangulo: "))

#Logica

if l1 == l2 and l1 == l3 and l2 == l3:
  print("Por los lados ingresados el triangulo es Equilatero")

elif l1 == l2 or l1 == l3 or l2 == l3:
  print("Por los lados ingresados el triangulo es Isosceles")

else:
  print("Por los lados ingresados el triangulo es Escaleno")