#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# ------------- Búsquedas en cadenas -------------


# In[2]:


# Cadena original
cadena = "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama. (Don Quijote)"


# In[3]:



# Busca la cadena "ama"
print (cadena.find("ama"))


# In[6]:


#Imprimie  la subcadena
print (cadena[cadena.find("ama"):])


# In[7]:


# Busca la siguiente coincidencia de "ama"
print (cadena[cadena.find("ama") + 1:].find("ama"))


# In[10]:


# Imprime la cadena a partir de la segunda coincidencia
print (cadena[61 + 1 + 40:])


# In[11]:


# Busca "corazon" en la cadena
print (cadena.find("corazon"))


# In[12]:


# Busca a partir de un indice
print (cadena.find("todo", 62))

# Imprime a partir de un �ndi


# In[13]:


print (cadena[78:])


# In[ ]:




