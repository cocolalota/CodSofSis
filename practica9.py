#victor jovany palacios noguez
#2-J
#practica 9

#!/usr/bin/env python
# coding: utf-8

# In[15]:


for i in range (10):
    print(i)
for i in range (1,20,2):
    print(i)

lista1=[1,2,3,4,5,6,7,8,9,0]
lista1.sort(reverse=true)
print(lista1)


# In[9]:


numero=int(input("ingresa el numero que deseas multiplicar"))
for i in range (1,11): 
    print(i,"x",numero,"=",i*numero)
    


# In[13]:


numero1="1234567890"
contador=1
numero=input("ingresa el numero")
numero2=list(numero)
for numero3 in numero2:
    contador= int (numero3)*contador
    print("producto",contador)

