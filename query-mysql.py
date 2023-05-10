# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='hugohugo', password='1234', host='127.0.0.1', database='codigoIoT')
# cursor = cnx.cursor()

# Query
query = ("SELECT id,fecha,nombre,texto,ifid_id FROM rfid WHERE id=1;")

# Ejecucion
# cursor.execute(query)
res = cnx.cmd_query(query)

#Imprimir resultado
print ("Respuesta")
print (res)

# Cerrar
# cursor.close()
cnx.close()
