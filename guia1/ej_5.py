#Programa que, como primera opcion, dado dos numeros ingresados por el usuario realiza todas las operaciones matematicas y como segunda opcion dado un numero entero imprime su tabla de multiplicar

#Variables
opcion = int(0)
salir = int(0)
num1 = int(0)
num2 = int(0)


#Logica
while not salir:
    #Opciones mostradas en pantalla para usuario
    print ("1. Realizar operaciones matematicas de dos numeros")
    print ("2. Imprimir tabla de multiplicar de un numero")
    print ("3. Salir")
    

    opcion = int(input ("Elige una opcion: "))
  

    if opcion == 1:
        #Realizar opetaciones matematicas de dos numeros
        num1=int(input("Ingrese el primer numero: "))
        num2=int(input("Ingrese el segundo numero: "))
        operacion = num1+num2
        print(f"La suma de {num1} y {num2} es: {operacion}")
        operacion = num1-num2
        print(f"La resta de {num1} y {num2} es: {operacion}")
        operacion = num1*num2
        print(f"La multiplicacion de {num1} y {num2} es: {operacion}")
        operacion = num1/num2
        print(f"La division de {num1} y {num2} es: {operacion}")
        salir = True
    elif opcion == 2:
        #Imprimir tabla de multiplicar de un numero n
        num1=int(input("Ingrese un numero: "))
        for i in range (11):
          operacion = num1*i
          print(f"{num1} X {i}= {operacion}")
        salir = True
    elif opcion == 3:
        salir = True
    else:
      print("Elige una opcion del 1 al 3")
    

  