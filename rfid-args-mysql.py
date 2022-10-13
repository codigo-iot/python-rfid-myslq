# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("status")
args = parser.parse_args()

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
    # print("ID: %s\nText: %s" % (id,text))
    strrr = text.split(",")
    # print (strrr)
    # print (strrr[0])
    sleep(1)
    query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + strrr[0] + "','" + args.status + "'," + str (id) + ");"
    print (query_insert)
    
    # Ejecutar cursor
    cursor.execute (query_insert)
    # Asegurarse de realizar la operacion en BD
    cnx.commit()
    print ("Query Ok")
    sleep (1)

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