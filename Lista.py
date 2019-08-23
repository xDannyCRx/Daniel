#lista=[]
#lista.append('Juan')
#print(lista)
#->Crear un software que le permita al profesor agregar o eliminar nombres de estudiantes (solo nombres)de estudiantes

lista=[]
while True:
    selecionar=input('1 = Desea agregar estudiante \n2 = Desea eliminar estudiante \n3 = Salir \n')
    if selecionar=='1':
        estudiante=input('Digite el Nombre: \n')
        lista.append(estudiante)
    elif selecionar=='2':
        print(lista)
        estudiante=(input('Digite el Nombre a eliminar: \n'))
        lista.remove(estudiante)
    elif selecionar=='3':
        break
print(lista)