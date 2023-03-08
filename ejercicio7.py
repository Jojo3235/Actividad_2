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
        if ControlDeListas.comprobar_no_pertenencia(lista,elemento) == True:
            lista.append(elemento)
            return lista
        else:
            return "Error: Imposible añadir elementos duplicados => {}.".format(elemento)
        
    
def main():
    lista = [1,2,3,4,5]
    elemento = 5
    lista = ControlDeListas.append_lista(lista, elemento)
    print(lista)

if __name__ == "__main__":
    main()