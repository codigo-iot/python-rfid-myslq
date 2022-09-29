# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

# Inicar el sensor
reader = SimpleMFRC522()

# Cuerpo del programa
try:
    # Leer el tag
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise