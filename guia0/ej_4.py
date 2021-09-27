#Pide al usuario que introduzca su nombre. Luego lo muentra en pantalla en mayuscula y cuenta la cantidad de letras

nombre = input("¿Cual es su nombre? Escribalo por favor: ")
contar_nombre = len(nombre)
nombre_may = nombre.upper()
print (f"{nombre_may} tiene {contar_nombre} letras")
