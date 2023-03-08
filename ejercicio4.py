"""Ejercicio 4
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""

from helpers import leer_texto, pedir_numero


class Tareas:

    def __init__(self, **kwargs):
        self.tareas = kwargs

    @staticmethod
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
    
def main():
    diccionario_tareas = Tareas.valores_to_dict()
    lista_valores = Tareas.generar_lista_valores(diccionario_tareas)
    lista_claves = Tareas.devolver_claves(diccionario_tareas, lista_valores)
    print("Estas son las tareas ordenadas por prioridad: ")
    for i in lista_claves:
        print(i)

if __name__ == "__main__":
    main()
