# -*- coding: utf-8 -*-

cont = 0


def incrementar():
    global cont
    print(cont)
    cont += 5


incrementar()
incrementar()
print (cont)
