def pedir_numero1_9(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if 1 <= numero <= 9:
                return numero
        except ValueError:
            pass
            print("El numero debe estar entre 1 y 9")

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un numero: "))
            return numero
        except ValueError:
            pass
            print("El numero debe ser un entero")