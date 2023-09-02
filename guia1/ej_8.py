#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

ingresa_numero = int(0)
primer_numero = int(0)
segundo_numero = int(1)
aux_num = int(0)

ingresa_numero = int(input("Ingrese la cantidad de numeros que desea ver de la Sucesion de Fibonacci: "))

print(primer_numero)
print(segundo_numero)
for i in range (ingresa_numero):
    aux_num = primer_numero+segundo_numero
    primer_numero=segundo_numero
    segundo_numero=aux_num
    print(aux_num)

primer_numero = int (0)
segundo_numero = int (1)
