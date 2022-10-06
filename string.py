nombre = "Hugo Vargas"
texto = "Texto del RFID"
rfid = 8462519551

# "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Hugo Vargas','Test Python 4',88843565);"
query = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + nombre + "','" + texto + "'," + str(rfid) + ")"

print (query)