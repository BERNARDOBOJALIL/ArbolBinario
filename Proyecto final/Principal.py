import random
from TDAs import Nodo, Arbol, Pila

arbol = Arbol()
pila = Pila()
pila_borrados = Pila() 

print("\033[94mPrograma de Bernardo Bojalil Lorenzini")
print("Estructura de Datos y Algoritmos")
print("Verano 2023\033[0m")

while True:
    print("\n\033[92mMENU:\033[0m")
    print("\033[92m1. Crear y mostrar números aleatorios")
    print("2. Añadir número al árbol")
    print("3. Mostrar recorridos")
    print("4. Borrar número del árbol")
    print("5. Mostrar números borrados")
    print("6. Características")
    print("7. Dibujar árbol")
    print("8. Salir\033[0m")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pila = Pila()
        numeros = random.sample(range(1, 101), 20)
        for numero in numeros:
            pila.apilar(numero)
        print("Números aleatorios generados y almacenados en la pila.")
        print("Números aleatorios:", numeros)

    elif opcion == "2":
        while not pila.esta_vacia():
            numero = pila.desapilar()
            arbol.raiz = arbol.insertar_binario(arbol.raiz, numero)
        print("Números añadidos al árbol.")

    elif opcion == "3":
        print("Recorridos:")
        print("Preorden:", end=" ")
        arbol.imprimir_preorden(arbol.raiz)
        print()
        print("Inorden:", end=" ")
        arbol.imprimir_inorden(arbol.raiz)
        print()
        print("Postorden:", end=" ")
        arbol.imprimir_postorden(arbol.raiz)
        print()

    elif opcion == "4":
        numero = int(input("Ingrese el número a borrar: "))
        if arbol.raiz is None:
            print("El árbol está vacío.")
        else:
            arbol.raiz = arbol.eliminar(arbol.raiz, numero)
            pila_borrados.apilar(numero)
            print("Número borrado del árbol.")

    elif opcion == "5":
        print("Números borrados:")
        while not pila_borrados.esta_vacia():
            numero = pila_borrados.desapilar()
            print(numero, end=" ")
        print()

    elif opcion == "6":
        print("Características:")
        print("¿Es un árbol perfecto?", arbol.es_arbol_perfecto(arbol.raiz))
        print("¿Es un árbol lleno?", arbol.es_arbol_lleno(arbol.raiz))
        print("Altura del árbol:", arbol.obtener_altura(arbol.raiz))
        print("Peso del árbol:", arbol.obtener_peso(arbol.raiz))
        print("Nodos hoja:", end=" ")
        arbol.imprimir_nodos_hoja(arbol.raiz)
        print()
        nodo_raiz = arbol.obtener_nodo_raiz()
        print("Valor del nodo raíz:", nodo_raiz.dato if nodo_raiz else "El árbol está vacío.")

    elif opcion == "7":
        arbol.dibujar_arbol()

    elif opcion == "8":
        print("\033[93m¡Hasta luego! Gracias por usar el programa.\033[0m")
      
        print("\033[93m        ^")
        print("       / \\")
        print("      /   \\")
        print("     /     \\")
        print("    /_______\\")
        print("      |   |")
        print("      |___|")
        print("\033[0m")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
