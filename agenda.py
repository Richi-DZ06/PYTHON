agenda = {}

def cargar_agenda(nombre,telefono):
    agenda[nombre] = telefono

def ver_agenda():
    print(agenda)

def ver_agenda_detalle():
    print("lista de contactos")
    for nombre,tel in agenda.items():
        print(f"{nombre} : {tel}")


if __name__== "__main__":
    cargar_agenda("moises","096167552")
    cargar_agenda("camila","0983883170")
    ver_agenda()
    ver_agenda_detalle()
