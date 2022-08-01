#Pregunta al usuario su edad y muestra en pantalla todos los años que ha cumplido desde 1 hasta la edad actual


#SOLUCIÓN EXPLICADA:

#1.Pedimos al usuario su edad usando un input de tipo int(entero), para que el valor de la edad solo se pueda introducir con números enteros
edad=int(input('Introduce tu edad:'))

#2.Creamos un bucle que se ejecutara (edad) veces, es decir, el bucle se ejecuta tantas veces como años tenga el usuario
for i in range(edad):
#3.Por cada vuelta que dé el bucle, se sumará 1 al valor de i y se mostrará por pantalla este nuevo valor
    #De esta forma empezará imprimiendo 1 y llegará hasta la edad introducida por el usuario
    i+=1
    print(i)


