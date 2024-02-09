'''
lista con 8 numeros enteros
1)recorrerla y mostrarla
2)ordenarla y mostrarla
3)mostrar su longitud
4)buscar un elemento deacuerdo a su busqueda del usuario
'''
def lista():
    lista = [1,2,5,8,7,4,6,3,25,4,5]
    return lista


for i in lista():
    print(i)

print(f'Lista desordenada: {lista()}')
newLista = lista()
newLista.sort()
print(f'Lista ordenada {newLista}')

print(f"Longitud de la lista: {len(lista())}")
numeroBuscar = int(input("Ingresa un numero a buscar en la lista y te digo si se encuentra: "))
if numeroBuscar in lista():
    print(f"El numero {numeroBuscar} si esta en la lista.")
else:
    print(f"El numero {numeroBuscar} no esta en la lista.")