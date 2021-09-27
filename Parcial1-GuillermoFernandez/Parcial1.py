
#Variables
dia = 0 #dia de nacimiento
mes = 0 # mes de nacimiento
año = 0 #año de nacimiento
sexo = "F" #sexo de la persona
cont1 = 0 #nacimientos en meses de enero
cont2 = 0 #nacimientos antes del 07/01/1980
cont3 = 0 #nacimientos en primavera de 1942
joven_año = 0
joven_sexo = ""
opcion = 0
salir = True

#Logica

while dia == 0:
  
    print ("Elija la opcion")
    print ("1. ingresar nacimiento")
    print ("2. Ver estadisticas")
    print ("3. Salir")
    
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
      dia = int (input("Ingrese el DIA de nacimiento - DOS DIGITOS: "))
      mes = int (input("Ingrese el MES de nacimiento - DOS DIGITOS: "))
      año = int (input("Ingrese el AÑO de nacimiento - DOS DIGITOS: "))
      sexo = str (input("Ingrese el sexo. M o F: "))
      #validar nacimientos en enero
      if dia > 0 and mes == 1: 
        cont1 = cont1 + 1
      #validar nacimientos antes 07/01/1980
      if año <= 80:
        if dia <= 7 and mes == 1 and año == 80: 
          cont2 = cont2 + 1
        else:
          cont2 = cont2 + 1  
      #Validar nacimientos varones en primavera de 1942    
      if dia >= 22 and mes >= 9 and año == 42 and sexo == "M":
        cont3 = cont3 + 1
      #Validar sexo de persona mas joven  
      if año > joven_año:
        joven_sexo = sexo
      dia = 0

    elif opcion == 2:
      while dia == 0:
        print ("Elija la opcion del dato que desee conocer")
        print ("1. Cantidad de nacimientos en el mes de enero")
        print ("2. Cantidad de nacimientos antes del 07/01/1980")
        print ("3. Cantidad de nacimientos en primavera de 1942")
        print ("4. Sexo de la persona mas joven: ")
        print ("5. Salir")

        opcion = int(input("Ingrese opcion"))

        if opcion == 1:
          print (f"La cantidad de nacimientos en el mes de enero de todos los años es {cont1}")
        elif opcion == 2:
          print (f"La cantidad de nacimientos antes del dia 7 de enero de 1980 es {cont2}")
        elif opcion == 3:
          print (f"La cantidad de nacimientos de varones en 1942 es {cont3}")
        elif opcion == 4:
          if joven_sexo == "M":
            print("El sexo de la persona mas joven es masculino")
          else:
            print("El sexo de la persona mas joven es femenimo")
        elif opcion == 5:
          dia = 1
        else: 
          print ("Elija una opcion del 1 al 5, por favor")      
    elif opcion == 3:
     dia = 0
    else:
      print("Elija una opcion del 1 al 3")  
   
