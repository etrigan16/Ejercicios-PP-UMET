# A partir de un valor entero ingresado por teclado, se pide informar:
# a)	La quinta parte de dicho valor
# b)	El resto de la división por 5
# c)	La séptima parte del resultado del punto a) 


#Variables
num1 = float(0.0) #Numero ingreso por teclado
part5 = float(0.0) #Quinta parte del numero
res = float(0.0) #Resto de divicion por 5
part7 = float (0.0) #Septima parte del punto a)


#pedido de ingreso de numero
num1 = float (input("Ingrese un numero: "))

#Logica
part5 = round(float(num1/5),2) #quinta parte del numero
print (f"La quinta parte de {num1} es {part5}")
res = round(num1%5,2) #Calculo de resto dividido 5
print (f"El resto de {num1} dividido 5 es {res}")
part7 = round(float(part5/7),2) #calculo de dividir por 7 resultado punto a)
print (f"La septima parte de {part5} es {part7}")