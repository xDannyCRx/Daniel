#Que le pide al usuario ingresar la descripcion y el precio a la base de datos.
import sqlite3
conexion=sqlite3.connect('bd2.db')
try:
    #se crea el db
    conexion.execute('''create table articulos(codigo integer primary key AUTOINCREMENT,description text, precio real)''')
    print('se crea la tabla')
except sqlite3.OperationalError:
    print('yo existo')
#se agregan datos en el db   
descrip=(input('Digite la descripcion del articulo = \n')) 
precios=(input('Digite el precio del articulo = \n')) 
conexion.execute('insert into articulos(description, precio )values(?,?)',(descrip,precios))
conexion.commit()
#seleciona los valores
curso=conexion.execute('select codigo,description,precio from articulos')
for fila in curso:
    print(fila)
conexion.close()  