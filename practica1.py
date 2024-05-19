""""
calculo de promedio
"""

notas =[]
#leer datos
for x in range(1,4):
    nota = int(input(f"ingrese la nota {x} "))
    notas.append(nota)

    #calcular el promedio y si esta aprobado o reprobado
suma= 0
for x in range (3):
     suma += notas[x]

promedio = suma / 3
print("promedio de notas: ",promedio)
#verificar estado: aprobado o reprobado
print("estado:")
if (promedio > 1,7):
    print("aprobado")
else:
    print("reprobado")

6