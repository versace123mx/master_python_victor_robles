def validaTipo(lista):
    for i in lista:
        print(f"Soy un tipo de dato: {type(i)}")

lista = [1,'Hola',False,[1,2,3]]
validaTipo(lista)
