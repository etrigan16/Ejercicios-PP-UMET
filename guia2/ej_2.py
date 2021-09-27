#Programa que dara las formas de pago y sus intereses de una compra

#Variables
compra = float(0.0) #Importe de compra
inter2 = float(0.0) #Interes en dos cuotas
inter6 = float (0.0) #Interes en seis coutas
cuot2 = float(0.0) #Cuota a pagar en dos pagos
cuot6 = float(0.0) #Cuota a pagar en seis pagos
tot2 = float (0.0) #Total en dos cuotas
tot6 = float (0.0) #Total en seis cuotas

#Pedido al usuario de ingreso
compra = float(input("Ingrese el importe de su compra: "))

#logica

print(f"1 cuota de ${compra}") #mensaje 1 cuota

inter2 = round(float(compra*5/100),2) #calculo interes
tot2 = round(float(compra+inter2),2) #total en dos cuotas
cuot2 = round (float(tot2/2),2) #Calculo cuota
print(f"2 cuotas de ${cuot2}. Total ${tot2} (5% de recargo)")


inter6 = round(float(compra*40/100),2) #calculo interes
tot6 = round(float(compra+inter6),2) #total en seis cuotas
cuot6 = round (float(tot6/6),2) #Calculo cuota
print(f"6 cuotas de ${cuot6}. Total ${tot6} (40% de recargo)")