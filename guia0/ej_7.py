#Pide a usuario intriducir dos numeros enteros, luego realiza la division de ambos y muentra en pantalla el cociente y el resto 

#variables
num1 = int()
num2 = int()
res = int()
coc = int()


#logica
num1 = int(input("Ingrese el primer numero a dividir: "))
num2 = int(input("Ingrese el segundo numero a dividir: "))
res = round(num1%num2,2)
coc = round(num1//num2,2)
print(f"el resto de la division entre {num1} y {num2} es {res}")
print(f"el cociente de la division entre {num1} y {num2} es {coc}")