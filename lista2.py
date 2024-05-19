lista=[]
def cargar_lista(dato):
    lista.append(dato)


#recibir una cantidad indeterminada de argumentos
def cargar_lista(*args):
    for arg in args:
        lista.append(args)

def imprimir_lista():
    for item in lista:
        print(item,end='|')

cargar_lista(input("cargar nombre. "))
cargar_lista(input("cargar nombre. "))
cargar_lista(input("cargar nombre. "))
cargar_lista(input("cargar nombre. "))

imprimir_lista()

cargar_lista('a','b','c')

imprimir_lista()
