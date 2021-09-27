#Programa que calcula el ahorro con un 4% de interes anual durante tres años

#Variables
dinero_cta = float(0.0)
ahorro = float(0.0)
cont = int(1)



#logica

dinero_cta = float(input("Ingrese valor a depositar: "))

while cont <= 3:
  intereses = float(dinero_cta*4/100) #calculo de interes
  ahorro = round(float(dinero_cta+intereses),2) #Intereses + dinero en cuenta
  print(f"Sus ahorros el año {cont} seran de un total de {ahorro}") #muestra totales a usuario
  dinero_cta = ahorro
  cont = int(cont+1)
