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
        return cls.NUMERO_MAGICO * NumeroMagico.multiplicar_9(numero_elegido)

    def __str__(self):
        return "{} * 9 * {} = {}".format(self.numero_elegido, self.NUMERO_MAGICO, NumeroMagico.multiplicar_numero_magico(self.numero_elegido))
    
