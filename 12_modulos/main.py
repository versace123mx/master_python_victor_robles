#import mimodulo
from mimodulo import *
import datetime
import math
print(holamundo('Gustavo Marchena'))

print(calculadora(5,10))


#modulo de fechas
print(datetime.date.today())
fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)
print(fecha_completa.minute)
print(fecha_completa.second)

#modulo de matematicas
print(f"Raiz cuadrada de 10: {math.sqrt(10)}")