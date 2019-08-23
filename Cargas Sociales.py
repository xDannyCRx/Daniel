#Cree un sofware que calcule las cargas sociales. (30% el patrono y el 10% el epmleador)y que de el total)

while True:
    try:
        salario=float(input('Salario mensual a calcular \n ='))
        break
    except:
        print('Digite un Numero') 
patrono=salario*0.30
trabajador=salario*0.10
total=salario+patrono+trabajador
print('Salario con cargas sociales =',total)