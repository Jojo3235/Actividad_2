import sys
sys.path.insert(0, '')

import unittest
from ejercicio1 import Cadena
from ejercicio2 import NumeroMagico
from ejercicio3 import ListasComparar
from ejercicio4 import Tareas
from descomposicion import Descomposicion
from ejercicio6 import SepararLista
from ejercicio7 import ControlDeListas

class TestEjercicios(unittest.TestCase):
    
    def test_ejercicio1(self):
        cadena = "zerauJ epeP,01"
        self.assertEqual(Cadena.recuperar_cadena(cadena), "10,Pepe Juarez")

    def test_ejercicio2(self):
        numero_magico = NumeroMagico(1)
        self.assertEqual(numero_magico.multiplicar_9(1), 9)
        self.assertEqual(numero_magico.multiplicar_numero_magico(1), 111111111)
 
    def test_ejercicio3(self):
        comparar = ListasComparar.comparar_listas(["a", "b", "c"], ["c", "d", "e"])
        self.assertEqual(comparar, ["c"])
 
    def test_ejercicio4(self):
        dic = {'limpiar': 1, 'comer': 2, 'dormir': 3}
        lista = Tareas.generar_lista_valores(dic)
        self.assertEqual(Tareas.devolver_claves(dic,lista), ['limpiar', 'comer', 'dormir'])
 
    def test_ejercicio5(self):
        num = 214
        self.assertEqual(Descomposicion.descomponer_a_lista(num), [4,1,2])

    def test_ejercicio6(self):
        lista = [1, 2, 3, 4, 5, 6]
        self.assertEqual(SepararLista.separar(lista), ([2, 4, 6],[1, 3, 5]))

    def test_ejercicio7(self):
        lista = [1, 2, 3, 4, 5]
        elemento = 6
        self.assertTrue(ControlDeListas.comprobar_no_pertenencia(lista, elemento))