#Cree un asofware cond dos bases de datos. la primera con el nombre 'Empleados' y 
# la segunda 'Transacciones'
#En la base de datos empleados, cree tablas con los nombres:
#1)Empleados y 2)Horarios en la tabla empleados cree 3 casillas:
#1)nombre,2)cedula y 3) puesto.
#en la base de datos, cree 3 tablas:1)Inventario,2)efectivo y 3)Activos
#con las casillas en inventario: 1)entrada,2)salida y 3) saldo
#$olicite al usuario ingresar los datos de un nuevo empleado o ver los empleados que hay.

import sqlite3
conexion1=sqlite3.connect('empleados.db')
conexion2=sqlite3.connect('transacciones.db')
try:
    conexion1.execute('''create table empleados(cedulas integer primary key AUTOINCREMENT, nombre test, cedula text, puesto text)''')
    conexion1.execute('''create table Horarios''')
    conexion2.execute('''create table transacciones(inventario integer primary key AUTOINCREMENT, entrada test, salida text, saldo text)''')
    conexion2.execute('''create table efectivo''')
    conexion2.execute('''create table activos''')
    print('se crea la tabla')
except sqlite3.OperationalError:
    print('Ya existo')

nombre=(input('Digite el nombre del empleado = \n')) 
cedula=(input('Digite la cedula = \n')) 
puesto=(input('Digite el puesto = \n')) 
conexion1.execute('insert into empleados(nombre, cedula, puesto )values(?,?,?)',(nombre,cedula,puesto))
conexion1.commit()
curso=conexion1.execute('select cedulas,nombre,puesto from empleados')

entrada=(input('Digite el Articulo de ingresar = \n')) 
salida=(input('Digite la cantidad de Articulos de salida= \n')) 
saldo=(input('Digite el Saldo a pagar = \n')) 
conexion2.execute('insert into transacciones(entrada, salida, saldo )values(?,?,?)',(entrada,salida,saldo))
conexion2.commit()
curso=conexion2.execute('select inventario,entrada,salida from transacciones')

for fila in curso:
    print(fila)
conexion1.close() 
conexion2.close() 