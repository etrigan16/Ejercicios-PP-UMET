#Programa que le pide una palabra a un usuario y luego la repite 1000 veces de forma seguida y dejando un espacio. Para esto se utiliza parametro "end" de la funcion "print"


#Variables
palabra = str("")

#Logica

palabra= input("Ingrese palabra: ")

for i in range (1001):
  print(f"{palabra}", end=" ")
