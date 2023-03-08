"""Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']"""

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']


class ListasComparar:

    def __init__(self, lista_1, lista_2):
        self.lista_1 = lista_1
        self.lista_2 = lista_2

    @staticmethod
    def generar_lista(*args):
        lista = []
        for arguments in args:
            lista.append(arguments)
        return lista
    
    @staticmethod
    def comparar_listas(lista1, lista2):
        return list(set(lista1)&set(lista2))
    
    def __str__(self):
        return "Los elementos en común entre ambas listas son: {}".format(self.comparar_listas(self.lista_1, self.lista_2))
    

def main():
    lista_compartida = ListasComparar(lista_1, lista_2)
    print(lista_compartida)

if __name__ == "__main__":
    main()