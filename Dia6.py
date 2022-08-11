#A partir de la siguiente lista, 
# crea un programa que encuentre el segundo número más grande

numeros=[7,91,13,32,93,101,45,0,3]

#SOLUCIÓN EXPLICADA
#1. Primero de todo vamos a ordenar la lista de mayor a menor
    #Para ordenada de mayor a menor usamos el metodo .sort

    #El método sort por defecto orena de menos a mayor
    #Para que sea de mayor a menor, usaremos el argumento reverse y le daremos el valor True
numeros.sort(reverse=True)

#2. Ahora que ya tenemos la lista ordenada, tendremos que encontrar el segundo elemento de la l 
segundo_mayor=(numeros[1])
print('El segundo número mayor es',segundo_mayor)
