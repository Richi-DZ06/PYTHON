#ejecutar python -m pip install mysql-connector-python
#documentacion de consulta: https://www.w3school.com/python/python_mysql_getstarted.asp
"""perfeccionar el ejercicio detraductor implementando una base de datos mysql crear una tabla llamada
 traductorcon los campos ID,español,ingles"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_spotify_richi"
)

cursor = mydb.cursor()

palabra = input("ingrese la palabra a traducir: ")
sentencia = f"select INGLES from traductor where ESPANOL like'{palabra}'"
cursor.execute(sentencia)

resultado = cursor.fetchall()

#si existe imprimir, sino solicitar para agregar una nueva palabra
for x in resultado:
    print(x) 