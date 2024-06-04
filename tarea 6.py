
lista = []


while True:
    print("Menú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir y terminar el programa")

    opcion = input("Elija una opción: ")

   
    if opcion == '1':
        element = input("Ingrese el elemento a añadir a la lista: ")
        lista.append(element)
        print("Elemento '{}' añadido a la lista.".replace('{}', element))

   
    elif opcion == '2':
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(lista):
            new_element = input("Ingrese el nuevo valor: ")
            lista[indice] = new_element
            print("Elemento en el índice {} ha sido modificado.".replace('{}', str(indice)))
        else:
            print("Índice no válido.")

   
    elif opcion == '3':
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(lista):
            element_remove = lista.pop(indice)
            print("Elemento '{}' en el índice {} ha sido eliminado.".replace('{}', element_remove).replace('{}', str(indice)))
        else:
            print("Índice no válido.")

    elif opcion == '4':
        if lista:
            element_remove = lista.pop()
            print("Último elemento '{}' ha sido eliminado.".replace('{}', element_remove))
        else:
            print("La lista está vacía.")

    elif opcion == '5':
        element = input("Ingrese el elemento a buscar: ")
        if element in lista:
            indice = lista.index(element)
            print("Elemento '{}' encontrado en el índice {}.".replace('{}', element).replace('{}', str(indice)))
        else:
            print("Elemento no encontrado en la lista.")


    elif opcion == '6':
        if lista:
            print("Elementos de la lista:")
            for i, element in enumerate(lista):
                print("[{}] {}".replace('{}', str(i), 1).replace('{}', element, 1))
        else:
            print("La lista está vacía.")

    
    elif opcion == '7':
        print("Saliendo del programa y finalizando.")
        break

    else:
        print("Opción no válida, por favor elija una opción del 1 al 7.")
