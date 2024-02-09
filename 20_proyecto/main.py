from usuarios import acciones

print('''
    Acciones disponibles:
      - registro
      - login
      - salir
''')

accion = input("¿Que quieres hacer?: ")

while accion != 'registro' and accion != 'login' and accion != 'salir':
    print("Opccion Invalida :) ")
    accion = input("¿Que quieres hacer?: ")
    

if accion == 'registro':
    acciones.Acciones().registro()
    
elif accion == 'login':
   acciones.Acciones().login()
else:
    acciones.Acciones().salir()
