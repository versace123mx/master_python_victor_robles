import hashlib
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

from conexion import conexiondb

connect = conexiondb.ConexionDB().conectar()

database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = 'insert into usuarios(nombre,apellidos,email,password,active) values(%s,%s,%s,%s,%s)'
        usuario = (self.nombre,self.apellido,self.email,cifrado.hexdigest(),1)
        cursor.execute(sql,usuario)
        database.commit()
        return [cursor.rowcount,self]

    def identificar(self):
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = 'select * from usuarios where email = %s and password = %s;'
        usuario = (self.email,cifrado.hexdigest())
        cursor.execute(sql,usuario)
        myresult = cursor.fetchone()
        return myresult
    
    def validaCorreo(self):
        sql = 'select count(*) from usuarios where email = %s;'
        email = (self.email,)#aqui hay que entender que se le paza una tupla, lista o diccionario y cuando le paso una tupla como en este caso hay que colocarle una coma , al final
        cursor.execute(sql,email)
        myresult = cursor.fetchone()
        return myresult

    def actualizaLogin(self,idUser):
        sql = 'insert into login(id_usuario,active) values(%s,%s)'
        usuario = (idUser,1)
        cursor.execute(sql,usuario)
        database.commit()
        