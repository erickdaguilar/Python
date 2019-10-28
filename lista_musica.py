# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:38:04 2019

@author: usuario
"""
lista_musica = [["Metal","Epica","The Phantom Agony"],
                ["Rock","Muse","Black Holes and Revelations"],
                ["Electronica", "Deadmau5","Profesional Griefers"],
                ["Horrorpunk","Misfits","Famous Monsters"],
                ["Metal","Metallica","The Four Horseman"]]

print(lista_musica[0][2])
print(len(lista_musica))
lista_musica.append(["Punk","Ramones","Rocket to Rusia"])
elem_borrado = lista_musica[2]
print(elem_borrado)
lista_musica.pop(2)
lista_musica.insert(4,["K-Pop","SuperJunior","Mr. Simple"])
print(lista_musica)
lista_musica.insert(2,elem_borrado)
print(lista_musica)