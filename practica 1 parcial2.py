#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Artista:
    genero = 'rap'
    escuela = 'teatro'

    def __init__(self, nombre, pais):
        print(f"creado artista {nombre}, {pais}")
        self.nombre = nombre
        self.pais = pais

artista=Artista("tyron jose", "venezuela")

