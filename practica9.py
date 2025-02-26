#!/usr/bin/env python
# coding: utf-8

# In[3]:


edad = float(input("ingresa la edad que deseas saber si es posible votar"))
if edad >= 18:
    print("es posible votar")
else:
    print("eres menor de edad, no puedes votar")


# In[5]:


numero1=input("ingresa el primer numero")
numero2=input("ingresa el segundo numero")
if numero1>numero2:
    print(numero1," es mayor que ",numero2)
elif numero2>numero1:
    print(numero2," es mayor que ",numero1)


# In[11]:


edades=[]
edad1=int(input("ingresa tu edad"))
edades.append(edad1)
edad2=int(input("ingresa tu edad"))
edades.append(edad2)
edad3=int(input("ingresa tu edad"))
edades.append(edad3)
edad4=int(input("ingresa tu edad"))
edades.append(edad4)
print("la edad menor es ",min(edades))


# In[21]:


minus="qwertyuiopasdfghjklñzxcvbnm"
mayus="QWERTYUIOPASDFGHJKLÑZXCVBNM"
palabra=input("ingresa una palabra")
letras=list(palabra)
for letra in letras:
    if letra in minus:
        print("letra minuscula ",letra)
    elif letra in mayus:
        print("letra mayuscula ",letra)
    else:
        print("es un simbolo o numero ",letra)


# In[ ]:





# In[ ]:




