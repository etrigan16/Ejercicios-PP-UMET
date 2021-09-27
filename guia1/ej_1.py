#Programa que pregunta al usuario nombre y luego lo saluda. Luego le pide dos numeros y le muestra el producto de ellos.

#variables
nombre = str("")
num1 = int(0)
num2 = int(0)
prod = int(0)

#Logica
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!!")
print("Le pediremos dos numeros y encontraremos el producto de ellos ")
num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))
prod = num1*num2
print(f" El producto entre {num1} y {num2} es: {prod}")