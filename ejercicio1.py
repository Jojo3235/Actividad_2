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
        print(cadena)
    
    def __str__(self):
        cadena = self.cadena.split(',')
        return f"{cadena[1]} ha sacado un {cadena[0]}"

def main():
    cadena = Cadena('zerauJ epeP,7')
    cadena.mostrar(cadena.recuperar_cadena(cadena.cadena))          ## hacer que formatee la corrupta
    print(cadena.__str__())

if __name__ == '__main__':
    main()