# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:23:17 2019

@author: usuario
"""
print("Cuanto sacaste en Algoritmos?")
a=int(input())
print("Cuanto sacaste en Contabilidad?")
b=int(input())
print("Cuanto sacaste en Tecnicas de investigacion?")
c=int(input())
print("Cuanto sacaste en Teoria del conocimiento?")
d=int(input())
print("Cuanto sacaste en Info I?")
e=int(input())
import matplotlib.pyplot as plt
plt.plot(["Algoritmos","Contabilidad","Tecnicas de investigacion","Teoria del conocimiento","Info I"],[a,b,c,d,e]) #Vector en Y
#Grafica por defecto el vecto X = 1, 2, 3, 4
plt.axis([-1,5,0,11])
plt.xticks(range(10), labels, rotation=-30, ha='left')
plt.tight_layout()
plt.title('Promedio')
plt.ylabel('some Y numbers')
plt.xlabel('some X numbers')
plt.show()
