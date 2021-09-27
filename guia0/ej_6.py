#Programa que calcula el indice de masa corporal

#Variables
kg = float(0.0)
alt = float(0.0)
imc = float(0.0)

#Logica
print ("Se calculara tu indice de masa corporal")

kg = input("Ingrese su peso: ")
while not (kg.isdigit()):
  print("El valor no es correcto.Ingreso numeros")
  kg = input ("Ingrese su peso: ")
kg2 = float(kg)

alt = input("Ingrese su altura en centimetros: ")
while not (alt.isdigit()):
  print("El valor no es correcto.Ingreso numeros")
  alt = input("Ingrese su altura en metros: ")
alt2 = float(alt)  
print(f"Su peso es {kg} y su altura es {alt}")
imc =kg2/(alt2*2)
print (f"Su indice de masa corporal es {imc}")