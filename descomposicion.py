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