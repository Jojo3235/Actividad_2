import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

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
            numero = int(input("Introduzca un numero: "))
            return numero
        except ValueError:
            pass
            print("El numero debe ser un entero")

def pedir_varias_cadenas():
    lista = []
    while True:
        cadena = leer_texto("Introduzca un elemento: ")
        lista.append(cadena)
        if leer_texto("¿Quieres añadir otra cadena? (s/n): ") == "n":
            return lista

def leer_texto(mensaje):
    return input(mensaje)

def valores_to_dict():
    valores = {}
    while True:
        try:
            clave = leer_texto("Introduzca una clave: ")
            valor = pedir_numero()
            valores[clave] = valor
            if leer_texto("¿Quieres añadir otro valor? (s/n): ") == "n":
                return valores
        except ValueError:
            pass
            print("Error")

def pedir_varios_numeros():
    lista = []
    while True:
        try:
            numero = pedir_numero()
            lista.append(numero)
            if leer_texto("¿Quieres añadir otro valor? (s/n): ") == "n":
                return lista
        except ValueError:
            pass
            print("Error")