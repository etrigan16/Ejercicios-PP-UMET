""" Programa que tendra las siguientes opciones de calculos:
a) Calcular perimetro de rectangulo
b) Calcular area de rectangulo
c) Calcular area de rectangulo alineado ejes X e Y
d) perimetro de circulo dado su radio
e) calcular area de un circulo dado su radio
f) volumen de una esfera dado su radio
g) calcular hipotenusa  """

#variables
opcion=int(0)
salir=int(0)
lado1=float(0.0)
lado2=float(0.0)
lado3=float(0.0)
result=float(0.0)

#Logica

while not salir:
    #Opciones mostradas en pantalla para usuario
    print ("1. Calcular perimetro de rectangulo")
    print ("2. Calcular area de rectangulo")
    print ("3. Calcular area de rectangulo (alineado ejes X e Y) dadas sus coordenadas x1, x2, y1, y2.")
    print ("4. Calcular perimetro de circulo dado su radio")
    print ("5. Calcular area de un circulo dado su radio")
    print ("6. Calcular volumen de una esfera dado su radio")
    print ("7. Calcular hipotenusa")
    print ("8. Salir")
     
    opcion = int(input ("Elige una opcion: "))
 
 
    if opcion == 1:
        #Calculo de perimetro de rectangulo
        lado1=float(input("Ingrese la altura del rectangulo: "))
        lado2=float(input("Ingrese la base del rectangulo: "))
        result= round(float((lado1*2)+(lado2*2)),2)
        print(f"El perimetro del rectangulo es: {result}")
        salir = True
    elif opcion == 2:
        #Calculo de area de rectangulo
        lado1=float(input("Ingrese la altura del rectangulo: "))
        lado2=float(input("Ingrese la base del rectangulo: "))
        result=round(float((lado1)*(lado2)),2)
        print(f"El perimetro del rectangulo es: {result}")
        salir = True
    elif opcion == 3:
      #NO PUDE ENCONTRAR COMO REALIZARLO, POR AHORA.
        #Calcular area de rectangulo (alineado ejes X e Y) dadas sus coordenadas x1, x2, y1, y2.
        print("Opcion 3")
        salir = True
    elif opcion == 4:
        #Calcular perimetro de un circulo
        lado1=float(input("Ingrese el radio del circulo: "))
        result=round(float(2*3.14*lado1),2)
        print(f"El perimetro del circulo es: {result}")
        salir = True
    elif opcion == 5:
        #Calcular area de un circulo
        lado1=float(input("Ingrese el radio del circulo: "))
        result=round(float(3.14*(lado1**2)),2)
        print(f"El area del circulo es: {result}")
        salir = True
    elif opcion == 6:
        #Calcular el volumen de una esfera
        lado1=float(input("Ingrese el radio de la esfera: "))
        result=round(float(3.14*1.33*(lado1**3)),2)
        print(f"El volumen de la esfera es: {result}")
        salir = True
    elif opcion == 7:
        #Calcular la hipotenusa de un triangulo rectangulo
        lado1=float(input("Ingrese largo del primer cateto: "))
        lado2=float(input("Ingrese largo del segundo cateto: "))
        result=round(float((lado2**2)+(lado1**2)),2)
        print(f"La hipotenusa de un triangulo rectangulo es: {result}")
        print("Opcion 7") 
        salir = True               
    elif opcion == 8:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 8")
 
print ("Fin")