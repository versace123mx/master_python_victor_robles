import mysql.connector

#conexion
database = mysql.connector.connect(
    host = 'localhost',
    user = 'victorrobles',
    passwd = 'Prueba12#',
    database = 'masterPython'
)

cursor = database.cursor()


#crear base de datos
sql = 'Create database IF not exists python_prueba;'
cursor.execute(sql)

#crear tablas
sql = '''
    Create table if not exists vehiculos(
        id int auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        constraint pk_vehiculo Primary key(id)
);
'''
cursor.execute(sql)



sql='show databases;'
cursor.execute(sql)

