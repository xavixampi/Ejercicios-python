#Crea un diccionario con varias divisas y sus correspondientes símbolos
#Cuando el usuario escriba el nombre de una divisa, el programa tiene que devolver el símbolo que le corresponda
#En caso de que la divisa introducida por el usuario no esté disponible, muestra un mensaje en pantalla que informe de esto

#SOLUCIÓN EXPLICADA:
#1.Creamos un diccionario con las divisas que vamos a utilizar
divisas={'Yen':'¥','Euro':'€','Libra':'£','Dollar':'$'}
#2.Creamos una variable con un input para que el usuario introduzca el nombre de la moneda
divisa_seleccionada = input("Introduce una divisa: ")

#3.Usamos un condicional. Si la divisa seleccionada está en nuestro diccionario, mostrara por pantalla su símbolo
if divisa_seleccionada.title() in divisas:
    print(divisas[divisa_seleccionada.title()])
#4.En caso de que la divisa no esté en nuestro diccionario, nos mostrara un mensaje por pantalla
else:
    print("Esa divisa no está disponible")