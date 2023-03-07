"""Ejercicio 7
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

Sugerencia

Puedes utilizar la sintaxis "elemento in lista"

elementos = [1, 5, -2]
"""
#sencillo, faltaria buscar como hacerlo en una clase, ya mañana

def agregar_una_vez(lista, el):
    #Quiza meter un while true para que no se cierre el programa si se introduce un valor erroneo, cambiar un poco de codigo ***
    if el in lista:
        raise ValueError("Error: Imposible añadir elementos duplicados => [elemento].") #***
    else:
        lista.append(el)
        return lista    #Esto quiza ya meterlo en el __str__
    
#Faltan implementar tests y menu