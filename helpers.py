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

def leer_texto(mensaje):
    return input(mensaje)

def valores_to_dict():
    valores = {}
    while True:
        try:
            clave = leer_texto("Introduce una clave: ")
            valor = pedir_numero()
            valores[clave] = valor
            if leer_texto("¿Quieres añadir otro valor? (s/n): ") == "n":
                return valores
        except ValueError:
            pass
            print("Error")

