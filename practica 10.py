#nombre:victor jovany palacios noguez
#grado y grupo:2-J



#!/usr/bin/env python
# coding: utf-8

# In[39]:


def factorial (n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n -1)
num =int(input("introduce un numero paracalcular su factorial:"))
if num< 0:
    print("el factorial no esta difinido para numeros negativos.:")
else:
    result =factorial(num)
    print(f"el factorial de {num} es {result}.")


# In[ ]:


def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero \\= 10:
    return suma
num =int(input("introduce un numero para calcular la suma de sus digitos:"))
resultado =suma_digitos(num)


# In[35]:


def es_primo(n):
    if n <= 1:
        return 
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return
num1=int(input("introduce el primer numero: "))
num2=int(input("introduce el segundo numero: "))
if num1 > num2:
    num1, num2, num2, num1
print(f"los numeros primos entre {num1} y {num2} son:")
for num in range(num1, num2 +1):
    if es_primo(num):
        print(num)


# In[1]:


n = int(input("intruce un numero:"))
for i in range (1, n + 1):
    linea =''.join(str(x) for x in range (1, i +1))
    print(f"#{linea}")

