#Dada una terna de números naturales que representan al día, al mes y al año de una determinada fecha informarla como un solo número natural de 8 dígitos (AAAAMMDD).

#variables
d = int(0) #Dia
m = int(0) #Mes
a = int(0) #Año

#Logica

d = int(input("Ingrese los dos digitos del dia: "))
m = int(input("Ingrese los dos digitos del mes: "))
a = int(input("Ingrese los cuatro digitos del año: "))

print(f"{a}{m}{d}")