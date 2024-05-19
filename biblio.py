import os
#menu principal
respuesta = -1
while(respuesta != 0):
    print("elija una opcion")
    print("1. calculadora")
    print("2. ver mi IP")
    print("3. administrador de tareas")
    print("4. apagar equipo en 5 minutos")
    print("5. cancelar apagado")
    print("0. salir")
    respuesta = int(input(" |"))
    if(respuesta == 1):
        os.system('calc')

    elif(respuesta == 2):
      os.system('ipconfig')

    elif(respuesta == 3):
      os.system('taskmgr')

    elif(respuesta == 4):
       os.system('shutdown -s -t 300')

    elif(respuesta == 5):
       #ver como cancelar el apagado
       os.system('')
    else:
       "No se ha seleccionado nada"


