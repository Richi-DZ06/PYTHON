#numeros primos
numero = 100000000
while True:
    bandera = 0
    for x in range(2,numero//2):
        if(numero % x == 0):
            bandera = 1
            #si la bandera es 1 ya no es primo
            break
    if (bandera == 0):
        print(numero)


    bandera = 0
    numero += 1