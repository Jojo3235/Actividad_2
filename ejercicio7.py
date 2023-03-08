class ControlDeListas:

    def __init__(self, lista, elemento):
        self.lista = lista
        self.elemento = elemento

    @staticmethod
    def comprobar_no_pertenencia(lista, elemento):
        if elemento in lista:
            return False
        else:
            return True

    @staticmethod
    def append_lista(lista, elemento):
        lista.append(elemento)
        return lista