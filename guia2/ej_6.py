# Dadas dos fechas informar cual es la más reciente. Determine cuales serían los datos de entrada  y las leyendas a informar de acuerdo al proceso solicitado.  

#Importar modulo
import datetime

#ingreso de fechas para comprar
fecha1 = datetime.datetime(2021, 1, 1)
fecha2 = datetime.datetime(2019, 1, 1)


#Logica
if fecha1 > fecha2:
  print (f"La fecha {fecha1} es mas reciente que la fecha {fecha2}")
else:
  print (f"La fecha {fecha2} es mas reciente que la fecha {fecha1}") 