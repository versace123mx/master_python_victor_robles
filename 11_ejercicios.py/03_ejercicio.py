'''
comprobar si una variable esta vacia y si esta vacia que la rellene con un texto en minusculas y la muestre en mayusculas
'''

def validaDAto(valor):
    if not len(valor.strip()):
        valor = 'Hola mundo desde Python'
    
    return valor.upper()

print(validaDAto(''))