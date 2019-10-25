#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Cada vez que creamos un objeto de esa clase, la definicion del contructor es la primera en ejecutarse.
#La forma de iniciar el valor de un atributo de clase sin un contructor:
class three:
    val=7

Constuctor __init__ (self)


# In[3]:


#Tambien podemos hacer esto dentro de las cunciones de clase:
class three:
    def func(self,val):
        self.val=val
t=three()
t.func(8)
t.val


# In[4]:


t.func(6) #Tambien nos permite reinicializar atributos
t.val


# In[ ]:


#O podemos pedirle informacion al usuario.

class three:
    def __init__(self):
        self.val=input("what value?")

t=three()


# In[ ]:


t.val


# In[ ]:


#Creacion de objetos
#__new__ es un metodo de clase estatica que nos permite control la creacion de objetos.
#Cada vez que hacemos una llamada al constructor de la clase, realiza una llamada a __new__.
#Si bien esta es la funcion predeterminada para cada clase, definitivamente podemos jugar con ella.

class demo:
    def __new__(self):
        return 'dataflair'
d=demo()
type(d)


# In[ ]:


#str 

#Tambien podemos crear un nuevo atributo exclusivamente para este objeto y leerlo al definir valores.
#No hay muchos que pueda hacer una vez que ya haya definico el objeto.

kumquat.color='orange'


# In[ ]:


get_ipython().set_next_input('Entonces, ?que sucede cuando no proporcionamos explicitamente un contructor para una clase');get_ipython().run_line_magic('pinfo', 'clase')
get_ipython().run_line_magic('pinfo', 'Puede')

