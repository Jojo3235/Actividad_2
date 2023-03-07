"""Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla"""

from helpers import pedir_numero1_9

class NumeroMagico:

    NUMERO_MAGICO = 12345679

    def __init__(self, numero_elegido):
        self.numero_elegido = numero_elegido

    @staticmethod
    def multiplicar_9(numero): 
        return numero * 9

    @classmethod
    def multiplicar_numero_magico(cls, numero_elegido):
        return cls.NUMERO_MAGICO * 9 * numero_elegido

    def __str__(self):
        return "{} * 9 * {} = {}".format(self.numero_elegido, self.NUMERO_MAGICO, NumeroMagico.multiplicar_numero_magico(self.numero_elegido))
    
if __name__ == "__main__":
    numero_usuario = pedir_numero1_9("Introduce un numero entre 1 y 9: ")
    numero_magico = NumeroMagico(numero_usuario)
    print(numero_magico)