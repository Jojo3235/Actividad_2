class Cadena:

    def __init__(self, cadena):
        self.cadena = Cadena.recuperar_cadena(cadena)

    @staticmethod
    def leer_texto(mensaje):
        return input(mensaje)

    @staticmethod
    def recuperar_cadena(cadena):
        return cadena[::-1]

    @staticmethod
    def mostrar(cadena):
        return cadena
    
    def __str__(self):
        cadena = self.cadena.split(',')
        return f"{cadena[1]} ha sacado un {cadena[0]}"