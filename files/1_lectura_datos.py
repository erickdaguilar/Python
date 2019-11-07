# -*- coding: utf-8 -*-

print ("Hola, como te llamas?")
nombre = input(' ')
print ("Buen día " + nombre)


running = True #
while running:
    valor_1 = 0
    valor_2 = 0
    print ("---Calculadora---")
    print ("1- Sumar")
    print ("2-Restar")
    print ("3 Multiplicar")
    print ("4-Division")
    print ("5-Salir")
    op = int(input('Opcion: '))
    if op == 1:
        print ("---Sumar---")
        valor_1 = int(input(''))
        print (" + ")
        valor_2 = int(input(''))
        suma = valor_1 + valor_2
        print ("El resultado es: %d" % suma)
    elif op == 2:
        print ("---Restar---")
        valor_1 = float(input(''))
        print (" - ")
        valor_2 = float(input(''))
        resta = valor_1 - valor_2
        print ("El resultado es: %d" % resta)
    elif op == 3:
        print ("---Multiplicar---")
        valor_1 = float(input(''))
        print (" x ")
        valor_2 = float(input(''))
        multiplicacion = valor_1 * valor_2
        print ("El resultado es: %d" % multiplicacion)
    elif op == 4:
        print ("---Division---")
        valor_1 = float(input(''))
        print (" / ")
        valor_2 = float(input(''))
        if valor_2 == 0:
            print ("No se puede dividir entre cero")
        else:
            division = valor_1 / valor_2
            print ("El resultado es: %d" % division)
    else:
        running = False
