import random

while True:
    aleatorio = random.randrange(0,3)
    elijePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. tijera")
    opcion = int(input("elije tu opcion"))

    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "Piedra"
    elif aleatorio == 1:
        elijePc = "Papel"
    elif aleatorio == 2:
        elijePc = "Tijera"
    print("La maquina elijio: ", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, papel envuelve piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta Papel")
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste, Papel envuelve Piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("perdiste, Tijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("perdiste, piedra machaca tijera")
    elif elijePc == elijeUsuario:
        print("empate")
        