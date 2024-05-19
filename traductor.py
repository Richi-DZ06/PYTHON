traductor = {"casa":"house","lapiz":"pen"}


while True:
    palabra=input("ingrese una palabra a traducir ")
    if palabra in traductor:
        print(traductor[palabra])
    elif palabra == "0":
        break
    else:
        resp=input("no existe la traduccion. ¿desea agregar (s/n)?")
        if resp == "s":
            traduccion = input(f"ingrese la traduccion de {palabra}: ")
            traductor[palabra] = traduccion