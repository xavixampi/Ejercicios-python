#Pide al usuario el valor del radio. A partir de este dato, calcula el área del círculo y muéstrala al usuario


#SOLUCIÓN EXPLICADA:
from math import pi

#1. Pedimos al usuario el valor del radio con un input de tipo float, para que el usuario pueda introducir únicamente números(enteros o decimales).
radio=float(input('Introduce el valor del radio:'))
#2.Usamos la fórmula para hallar el valor del área. La fórmula es pi*radio**2
area=pi*(radio**2)
#Mostramos por pantalla el valor del área
print('El valor del area es:',area)
