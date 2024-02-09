'''
añadir valores a una lista mientras la longitud sea menor a  120
y luego mostrarlo por pantall
'''


condicion = 1
lista = []
while condicion <= 10:
    valor = int(input(f'Ingresa un valor {condicion}: '))
    lista.append(valor)
    condicion+=1

print(lista)