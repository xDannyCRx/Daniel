#!/usr/bin/env python
# coding: utf-8

# In[1]:


class itspower:
    def __init__(self,x):
       self.x=x
    def __pow__(self,other):
        return self.x**other.x
a=itspower(2)
b=itspower(10)
a**b


# In[11]:


def factorial(n):
    f=1
    while n>0:
        f*=n
        n-=1
    print(f)
factorial(4)


# In[12]:


def factorial(numero):
    print ("Valor inicial ->",numero)
    if numero > 1:
        numero = numero * factorial(numero -1)
    print ("valor final ->",numero)
    return numero
print (factorial(4))


# In[ ]:




