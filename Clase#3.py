import sqlite3
conexion=sqlite3.connect('bd.db')
try:
    #se crea el db
    conexion.execute('''create table articulos(codigo integer primary key AUTOINCREMENT,description text, precio real)''')
    print('se crea la tabla')
except sqlite3.OperationalError:
    print('yo existo')
#se agregan datos en el db    
conexion.execute('insert into articulos(description, precio )values(?,?)',('naranja',20))
conexion.commit()
#seleciona los valores
curso=conexion.execute('select codigo,description,precio from articulos')
for fila in curso:
    print(fila)
conexion.close()    

#SQl es la base de datos nativa de Python
#es nativa porque la comunicacion es simple entre ellos.
#Sqlite3 es la base de datos.
#Conexion en este caso es la variable que debe de estar presente para poder ejecutarse.
#lo que esta como ('bd.do) es el nombre de la base de datos.