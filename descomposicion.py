"""Ejercicio 5
Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:

python descomposicion.py 3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

0007

0040

0600

3000

Pista

Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa"""

# Crear un metodo de separacion de digitos, un metodo para formatearlos y un metodo para imprimirlos
from helpers import pedir_numero

class Descomposicion:
    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def descomponer_a_lista(numero):
        descomposicion = []
        while numero > 0:
            descomposicion.append(numero % 10)
            numero = numero // 10
        return descomposicion

    @staticmethod
    def formatear(descomposicion):
        for i in range(len(descomposicion)):
            descomposicion[i] = str(descomposicion[i]*10**i).zfill(len(descomposicion))
        return descomposicion[::-1]
    
    @staticmethod 
    def imprimir(descomposicion):
        for i in descomposicion:
            print(i)

def main():
    numero = pedir_numero()
    descomposicion = Descomposicion.descomponer_a_lista(numero)
    descomposicion = Descomposicion.formatear(descomposicion)
    Descomposicion.imprimir(descomposicion)


if __name__ == "__main__":
    main()