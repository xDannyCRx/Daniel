#Cree un asofware cond dos bases de datos. la primera con el nombre 'Empleados' y 
# la segunda 'Transacciones'
#En la base de datos empleados, cree tablas con los nombres:
#1)Empleados y 2)Horarios en la tabla empleados cree 3 casillas:
#1)nombre,2)cedula y 3) puesto.
#en la base de datos, cree 3 tablas:1)Inventario,2)efectivo y 3)Activos
#con las casillas en inventario: 1)entrada,2)salida y 3) saldo
#$olicite al usuario ingresar los datos de un nuevo empleado o ver los empleados que hay.

import sqlite3
conexion1=sqlite3.connect('bd.empleados')
conexion2=sqlite3.connect('db.transacciones')
try:
    conexion1.execute('''create table empleados(cedulas integer primary key, nombre test, cedula text, puesto text)''')
    conexion1.execute('''create table Horarios''')
    conexion2.execute('''create table inventario(codigo integer primary key AUTOINCREMENT, entrada test, salida text, saldo real)''')
    conexion2.execute('''create table efectivo''')
    conexion2.execute('''create table activos''')
    print('se crea la tabla')
except sqlite3.OperationalError:
    print('Ya existo')