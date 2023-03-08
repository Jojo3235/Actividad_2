"""Ejercicio 6
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

Por ejemplo:

pares, impares = separar([6,5,2,1,7])

print(pares)

print(impares)

[2, 6]

[1, 5, 7]

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método .sort()."""

# Generar la clase donde se usara un metodo estatico para generar la separacion de la lista segun sean pares o impares, finalmente un metodo str que devuelva ambas listas, a lo mejor 
# iniciarlas al principio de la clase para mayor comodidad

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