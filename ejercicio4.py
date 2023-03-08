from helpers import leer_texto, pedir_numero


class Tareas:

    def __init__(self, **kwargs):
        self.tareas = kwargs

    @staticmethod
    def valores_to_dict():
        valores = {}
        while True:
            try:
                clave = leer_texto("Introduzca una tarea: ")
                valor = pedir_numero()
                valores[clave] = valor
                if leer_texto("¿Quieres añadir otro valor? (s/n): ") == "n":
                    return valores
            except ValueError:
                pass
                print("Error")

    @staticmethod
    def generar_lista_valores(diccionario):
        lista = []
        for key, value in diccionario.items():
            lista.append(value)
        lista.sort()
        return lista
    
    @staticmethod
    def devolver_claves(diccionario, lista):
        lista_claves = []
        for value in lista:
            clave = list(diccionario.keys())[list(diccionario.values()).index(value)]
            lista_claves.append(clave)
        return lista_claves