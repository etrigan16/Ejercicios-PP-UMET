#Programa que informara la suma, la diferencia y el producto de dos valores enteros

#variables
num1=int(0)
num2=int(0)
sum=int(0)
rest=int(0)
prod=int(0)


#Logica

print("Se calculara la suma, la resta y la multiplicacion de dos valores que debera ingresar")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
sum=num1+num2 #Suma de numeros
print(f"La suma de {num1} y {num2} es: {sum}") #Mensaje de suma
rest=num1-num2 #resta de numeros
print(f"La resta de {num1} y {num2} es: {rest}") #Mensaje de resta
prod=num1*num2 #Producto de numeros
print(f"El producto de {num1} y {num2} es: {prod}") #Mensaje de producto
