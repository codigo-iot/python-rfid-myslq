import mysql.connector

cnx = mysql.connector.connect(user='hugohugo', password='1234', host='192.168.1.85', database='codigoIoT')
cnx.close()