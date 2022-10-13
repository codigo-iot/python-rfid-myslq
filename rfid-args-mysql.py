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
    # Lectura unica
    id, text = reader.read()
    print("ID: %s\nText: %s" % (id,text))
    strrr = text.split(",")
    print (strrr)
    print (strrr[0])
    sleep(1)

    # Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    
except KeyboardInterrupt:
    # Cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise