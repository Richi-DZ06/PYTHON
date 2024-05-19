#cargar e imprimir lista con funciones
#definimos una lista vacia
lista = []

#definimos la funcion que permitira cargar  la lista 
def cargar_lista(dato):
    lista.append(dato)


#recibir una cantidad indeterminada de argumentos
def cargar_lista(*args):
    for arg in args:
        lista.append(args)

def imprimir_lista():
    for item in lista:
        print(item,end='|')

  #ejecutamos las funciones 
cargar_lista(25)
cargar_lista(50)
cargar_lista(75)
cargar_lista(100)
#imprimimos la lista 
imprimir_lista()

cargar_lista('a','b','c',[125,852,963])

imprimir_lista()

