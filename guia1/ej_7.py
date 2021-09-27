#Programa que genera un calculo mediante una formula para el monto final segun intereses, capital inicial y años, todos ingresados por el usuario

#variables
c = float(0.0) #Capital inicial
x = float(0.0) #Tasa de interes
n = float (0.0) #Años a calcular
mf = float (0.0) #Monto final calculado
#Logica

c = float(input("Ingrese el capital inicial para el calculo: "))   
x = float(input("Ingrese la tasa de interes a aplicar: "))
n = float(input("Ingrese la cantidad de años: "))

mf = round(float(c*(1+(x/100)**n)),2)

print(f"El monto final calculado es {mf} pesos")

