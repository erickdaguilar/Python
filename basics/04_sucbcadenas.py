#!/usr/bin/env python
# coding: utf-8

# # Subcadenas

# In[1]:


# -*- coding: utf-8 -*-

# ------------- Cadenas y subcadenas -------------

# Cadena con 22 caracteres
cadena = "parangaricutirimicuaro"


# In[2]:


print (cadena[0])    # Se obtiene el primer carácter
print (cadena[21])   # Se obtiene el último carácter


# In[3]:


# Si se pone un indice negativo, la cuenta
# empieza en el �ltimo elemento de la cadena
print (cadena[-2])   # último carácter


# In[4]:


# Si se quiere acceder a un elemento fuera de rango
# de la cadena, se obtiene el error
# IndexError: string index out of range
#print (cadena[22])   # Carácter fuera de rango

print (cadena[5:13])  # imprime garicuti
print (cadena[5:])    # imprime garicutirimicuaro
print (cadena[:5])    # imprime param
print (cadena[:])     # imprime la cadena completa


# In[ ]:




