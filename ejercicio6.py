class SepararLista:
    def __init__(self, lista):
        self.lista = lista

    @staticmethod
    def separar(lista):
        pares = []
        impares = []
        for i in lista:
            if i % 2 == 0:
                pares.append(i)
            else:
                impares.append(i)
        return pares, impares

    def __str__(self):
        pares, impares = self.separar(self.lista)
        pares.sort()
        impares.sort()
        return f"Los numeros pares son: {pares} y los impares son: {impares}"
    
def main():
    lista = [6,5,2,1,7]
    separar = SepararLista(lista)
    print(separar)

if __name__ == "__main__":
    main()