# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:50:51 2019

@author: usuario
"""

print("¿Cual es tu nombre?")
nombre= input()
print("¿En que año naciste?")
edad= int(input())
edad= 2019-edad
edad= str(edad)
with open ("datos.txt","w") as file:
    file.write(nombre)
    file.write(edad)