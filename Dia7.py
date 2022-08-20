#Crea un programa que pida al usuario una frase y que devuelva la frase a la inversa
#Ejemplo: El usuario introduce hola, le devolvemos aloh


#SOLUCIÓN EXPLICADA

#1. Creamos un input de tipo string para que el usuario introduzca la frase
frase = str(input("Introduce una frase: "))
#2. creamos un bucle que de tantas vueltas como caracteres tenga la frase
    #El bucle empezará en el último caracter y acabará en el primero
    #Al valor de i se le resta 1 cada vuelta que da el bucle

for i in range(len(frase)-1,-1,-1):
    #Imprimimos por pantalla los caracteres de la frase
    #El valor i empezará en el último caracter y irá pasando por todos hasta llegar al útlimo
    #Usamos end=''para que los siguientes elementos se impriman en la misma línea
    print(frase[i],end='')
    
