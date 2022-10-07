# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='hugohugo', password='1234', host='127.0.0.1', database='codigoIoT')

# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Hugo Vargas','Test Python 8',865485648652);"

# Ejecutar cursor
cursor.execute (query_insert)

# Asegurarse de realizar la operacion en BD
cnx.commit()
print ("Query Ok")

# Cerrar
cursor.close()
cnx.close()