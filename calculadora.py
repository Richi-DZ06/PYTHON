#funiones matematicas
def suma(a,b):
    return a+b


def resta(a,b):
    return a-b


def multiplicacion(a,b):
    return a*b


def division(a,b):
    if(b==0):
        return "No se puede dividir por CERO"
    else:
        return a/b
    
def raiz(a,b = 2):
    return a**1/b

print("el resultado es ",suma(7,9))
print("el resultado es ",division(10,2))
print("el resultado es ",resta(5,2))
print("el resultado es ",multiplicacion(2,4))
print("el resultado es ", raiz(10,6))
