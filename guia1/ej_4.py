#Algoritmo que permite calcular factorial de un numero n

#Variables
num = int(0)
fact = int(1)
cont = int(1)


#Logica
num = int(input("Ingrese el numero para calculo factorial: "))
while(cont<=num):
    fact = cont*fact
    cont=cont+1
print(f"El numero factorial de {num} es {fact} ")