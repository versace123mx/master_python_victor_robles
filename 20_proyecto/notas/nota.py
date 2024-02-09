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

class Nota:

    def __init__(self,usuario_id,titulo='',descripcion=''):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = 'insert into notas (id_usuario,titulo,descripcion) values(%s,%s,%s);'
        nota = (self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        return [cursor.rowcount,self]

    def listar(self):
        sql = f"select * from notas where id_usuario = {self.usuario_id} and status = 1;"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def eliminar(self,idNota):

        sql = f"select count(*) from notas where id_usuario = {self.usuario_id} and status = 1 and id={int(idNota)};"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result[0]:
            sql = f'update notas set status = 0, fechaActualizacion = now() where id = {int(idNota)} and id_usuario = {self.usuario_id};'
            cursor.execute(sql)
            database.commit()

            return [cursor.rowcount,self]
        else:
            
            return ['La nota no existe o la nota no te pertenece, comprueba nuevamente el id de la nota:']