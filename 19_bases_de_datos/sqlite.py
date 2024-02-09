#Importar modulo de base de datos
import sqlite3

#conexion
conexion = sqlite3.connect('pruebas.db')

#crear curso
cursor = conexion.cursor()

sql = """
        Create table if not exists productos(
            id INT PRIMARY KEY AUTOINCREMENT, 
            titulo varchar(255),
            descripcion text,
            precio int
            );
    """
#crear tabla
cursor.execute(sql)
conexion.commit()

#insertar datos
#cursor.execute("Insert into productos values(null,'Primer producto','descripcion de mi producto',149)")
#conexion.commit()


sql = '''
    Select * from productos;
'''
#lectura
cursor.execute(sql)
productos = cursor.fetchall()
#print(productos) aqui ya tengo los datos
for producto in productos:
    print(producto)


#borrar por id
#sql = 'delete from productos where id = 1;'
#cursor.execute(sql)
#conexion.commit()

#borrar toda la tabla
sql = 'drop table productos;'
cursor.execute(sql)
conexion.commit()


#cerrar conexion
conexion.close()