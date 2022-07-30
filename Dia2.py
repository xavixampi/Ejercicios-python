#Resuelve la siguiente ecuación de segundo grado y muéstrale al usuario el resultado
#-x²-2x=-3


#SOLUCIÓN EXPLICADA:
#1.El primer paso para solucionar la ecuación colocar los términos para que ax²⁺+bx+c=0
    #-x²-2x+3=0
    #A partir de esta ecuación debemos asignar un valor a,b,c para cada término.
a=-1
b=-2
c=3

#2.El segundo paso es aplicar la fórmula para resolver las ecuaciones de segundo grado
    #Una ecuación de segundo grado tiene dos soluciones.

    #Al no poder usar ninguna librería, no podemos usar el símbolo ±
    #Por eso tenemos que hacer una variable para cada solución, una tendrá el símbolo + y la otra el símbolo -

    #Al no poder usar ninguna libería, tampoco podremos utilizar la operación de raíz cuadra
    #Por eso tendremos que buscar una operación equivalente. Una raíz cuadrada es equivalente a elevar un número a 0.5
    
x_1=(-b+((b**2-(4*a*c))**0.5))/(2*a)
x_2=(-b-((b**2-(4*a*c))**0.5))/(2*a)

#3.Mostramos al usuario el resultado de las ecuaciones
print('Las souciones para esta ecuación són:\n',x_1,'\n',x_2)
