# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector

# Inicar el sensor
reader = SimpleMFRC522()

# Conexión
cnx = mysql.connector.connect(user='hugolan', password='1234', host='192.168.1.85', database='codigoIoT')
# Cursor
cursor = cnx.cursor()

# Cuerpo del programa
try:
    # Leer el tag
    while True:
        print("Acercar el tag al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Hugo Vargas','" + text + "',"+ str (id) + ");"
        
        # Ejecutar cursor
        cursor.execute (query_insert)
        # Asegurarse de realizar la operacion en BD
        cnx.commit()
        print ("Query Ok")

        sleep(5)
except KeyboardInterrupt:
    # Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise