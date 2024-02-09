import usuarios.usuario as modelo
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
print(current) 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
print(parent)
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from notas import acciones


class Acciones:

    def registro(self):
        print("Ok!! Vamos a registrarte en el sistema")
        nombre = input("Cual es tu nombre?: ")
        apellido = input("Cual es tu apellido?: ")
        email = input("Cual es tu email?: ")
        password = input("Ingresa tu contraseña?: ")

        usuario = modelo.Usuario(nombre,apellido,email,password)
        validaCorreo = usuario.validaCorreo()
        if not validaCorreo[0]:
            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f"Perfecto {registro[1].nombre} te has registrado con el email: {registro[1].email}")
            else:
                print("No te haz registrado correctamente.")
        else:
            print(f"El registro no se pudo llevar acabo ya que el email ({email}) ya existe, intentalo con otro email.")


    def login(self):
        print("Vale!! Identificate en el sistema")
        email = input("Cual es tu email?: ")
        password = input("Ingresa tu contraseña?: ")
        usuario = modelo.Usuario('','',email,password)
        login = usuario.identificar()
        if not isinstance(login, type(None)):
            if email == login[3]:
                usuario.actualizaLogin(login[0])
                print(f"Bienvenido {login[1]} te haz logueado con el correo {login[3]} con la fecha: {login[5]}")
                self.proximasAcciones(login)
            else:
                print("Datos incorrectos")
        else:
            print("Erro de logueo, intentalo nuevamente.")
        

    def salir(self):
        print("Hasta luego.")


    def proximasAcciones(self,usuario):
        print('''
            Acciones disponibles:
              - Crear nota (crear)
              - Mostrar tus notas (mostrar)
              - Eliminar not (eliminar)
              - Salir (salir)
        ''')
        accion = input(f"¿Que quieres hacer {usuario[1]}?: ")
        hazEL = acciones.Acciones()

        if accion == 'crear':
            #print("vamos a crear")
            hazEL.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'mostrar':
            #print("vamos a mostrar")
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'eliminar':
            #print("vamos a eliminar")
            hazEL.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == 'salir':
            print(f"Hasta pronto {usuario[1]}")
            exit()