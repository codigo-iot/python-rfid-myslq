# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='hugolan', 
                              password='1234', 
                              host='192.168.1.185',
                              database='codigoIoT')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT id,nombre,temperatura,fecha FROM clima WHERE id=555;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()