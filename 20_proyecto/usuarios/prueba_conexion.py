'''
import sys

sys.path.insert(0, "../conexion")
import conexiondb as conexion

connect = conexion.conectar
database = connect[0]
cursos = connect[1]
print(database)

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'victorrobles',
    passwd = 'Prueba12#',
    database = 'masterPython'
)

mycursor = mydb.cursor()

sql = "select count(*) from usuarios where email = %s;"
adr = ["www"]

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
'''