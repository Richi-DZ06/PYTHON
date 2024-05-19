from biblioteca import Biblioteca
from libro import Libro


if __name__ == "__main__":
    ejecutar= True

    while ejecutar:
    
        print("----BIENVENIDOS AL SISTEMA BIBLIOTECARIO----")
        opcion = int(
            input(
                "¿Que vas a hacer?:\n1-Crear Biblioteca\n2-Agregar libro\n3-ver catalogo\n4-quitar libro\n5-salir\n:"

                
                )
        
        )
        if opcion == 1:
            nombre = input("Nombre de la biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print(
                "se creo la biblioteca:{}".format(
                    biblioteca.consultar_nombre_biblioteca
                    
                    )
                
                )
            
        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("Autor")
            cantidad_de_paginas = input("Paginas: ")
            genero = input("Genero: ")
            sinopsis = input("Sinopsis: ")
            libro = Libro(titulo,autor,cantidad_de_paginas,genero,sinopsis)
            biblioteca.agregar_libro(libro)
        elif opcion == 3:
            print("Catalogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)

        elif opcion == 4:
            indice = input("Id del libro a eliminar: ")
            biblioteca.quitar_libro(indice)

        elif opcion == 5 :
            print("Gracias por visitar. \n(:>)")
            ejecutar = False

        else:
            print("Opcion incorrecta")
