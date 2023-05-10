# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='hugolan', 
                              password='hugohugo', 
                              host='127.0.0.1',
                              database='codigoIoT')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT * FROM rfid WHERE id=3;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()