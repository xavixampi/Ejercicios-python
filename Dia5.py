#Crea una función que calcule el cuadrado de un número y la raíz cuadrada de otro
#Los números los tiene que determinar el usuario

#SOLUCIÓN EXPLICADA

#1.Para que el usuario determine los números que quiere, tenemos que hacerlo mediante un input
    #Vamos a pedirle el número del cual quiere saber el cuadrado. A este número le llamaremos n1
    #También tenemos que pedrile en número del cual quiere saber la raíz cuadrada. A este le llamaremos n2
n1=float(input('De que número quieres saber el cuadrado? '))
n2=float(input('De que número quieres saber la raíz cuadrada? '))

#2.Tenemos que crear una función que tome como parámetros n1 y n2
    #almacenaremos en una variable n1 elevado al cuadrado
    #almacenaremos en otra variable la raíz cuadrada de n2
        #La raíz cuadrada es equivalente a elevar un número a 0.5
def calcular(n1,n2):
    cuadrado=n1**2
    raiz=n2**0.5
    print('El cuadrado de',n1,'es',cuadrado)#Imprimimos por pantalla el valor de n1²
    print('La raiz cuadrada de',n2,'es',raiz)#Imprimimos por pantalla el valor de la raíz cuadrada de n2
#3.Llamamos a la función
calcular(n1,n2)