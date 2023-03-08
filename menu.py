import helpers
from descomposicion import Descomposicion
from ejercicio1 import Cadena
from ejercicio2 import NumeroMagico
from ejercicio3 import ListasComparar
from ejercicio4 import Tareas
from ejercicio6 import SepararLista
from ejercicio7 import ControlDeListas

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("================================")
        print("Bienvenido al menu de ejercicios")
        print("================================")
        print("1. Restuarador de cadenas       ")
        print("2. Número mágico                ")
        print("3. Comparador de listas         ")
        print("4. Ordenar tareas               ")
        print("5. Descomposicion               ")
        print("6. Pares e impares              ")
        print("7. Control de listas            ")
        print("8. Salir                        ")
        print("================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == "1":
            print("Restaurador de cadenas...")
            cadena = helpers.leer_texto("Introduce la cadena corrupta: ")
            cadena_c = Cadena(cadena)
            print(cadena_c.mostrar(cadena_c.recuperar_cadena(cadena_c.cadena)))
            print(cadena_c.__str__())

        elif opcion == "2":
            print("Número mágico...")
            numero_usuario = helpers.pedir_numero1_9("Introduce un numero entre 1 y 9: ")
            numero_magico = NumeroMagico(numero_usuario)
            print(numero_magico)

        elif opcion == "3":
            print("Comparador de listas...")
            args_1 = helpers.pedir_varias_cadenas()
            helpers.limpiar_pantalla()
            args_2 = helpers.pedir_varias_cadenas()
            comparar = ListasComparar(args_1, args_2)
            print(comparar)

        elif opcion == "4":
            print("Ordenar tareas...")
            diccionario_tareas = Tareas.valores_to_dict()
            lista_valores = Tareas.generar_lista_valores(diccionario_tareas)
            lista_claves = Tareas.devolver_claves(diccionario_tareas, lista_valores)
            print("Estas son las tareas ordenadas por prioridad: ")
            for i in lista_claves:
                print(i)

        elif opcion == "5":
            print("Descomposicion...")
            numero = helpers.pedir_numero()
            descomposicion = Descomposicion.descomponer_a_lista(numero)
            formateado = Descomposicion.formatear(descomposicion)
            helpers.limpiar_pantalla()
            print("Numero formateado: ")
            Descomposicion.imprimir(formateado)

        elif opcion == "6":
            print("Pares e impares...")
            lista = helpers.pedir_varios_numeros()
            separar = SepararLista(lista)
            print(separar)
            
        elif opcion == "7":
            lista = []
            while True:
                if helpers.leer_texto("¿Quieres añadir un valor? (s/n): ") == "s":
                    insertar = helpers.leer_texto("Introduzca el elemento de la lista: ")
                    if ControlDeListas.comprobar_no_pertenencia(lista, insertar) == True: 
                        lista = ControlDeListas.append_lista(lista, insertar)
                        print(lista)
                    else:
                        print("Error: Imposible añadir elementos duplicados => {}.".format(insertar))
                else:
                    print("Saliendo...")
                    break

        elif opcion == "8":
            print("¡Hasta la proxima!")
            break

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    iniciar()