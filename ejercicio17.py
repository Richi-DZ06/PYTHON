import os
resp = 1
while resp != 0:
    print("Paint (1)")
    print("Calc (2)")
    print("Apagar Pc en 2 hora(3)")
    print("Salir (0)")
    resp = int(input("seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os.system("calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200")
    else:
        print("No entiendo esa orden")
        