
import sqlite3

conexion = sqlite3.connect('db/Reservas_de_Clientes.db')

cursor = conexion.cursor()

sentenciaSQL = 'CREATE TABLE clientes'
sentenciaSQL = sentenciaSQL + '(nombre_completo integer,'
sentenciaSQL = sentenciaSQL + 'edad integer'
sentenciaSQL = sentenciaSQL + 'dni integer)'

cursor.execute(sentenciaSQL)

"""
except Exception as e:
    print('Hubo una Exception: ', e)
"""

conexion = sqlite3.connect("db/Reservas_de_Clientes.db")
conexion.close()

#insertando registros
conexion = sqlite3.connect("db/Reservas_de_Clientes.db")

cursor = conexion.cursor()

sentenciaSQL = "INSERT INTO reservas"
sentenciaSQL = sentenciaSQL + "VALUES ('Agustina Ramos', '21', '43567894')"
cursor.execute(sentenciaSQL)

sentenciaSQL = "INSERT INTO reservas"
sentenciaSQL = sentenciaSQL + "VALUES ('Martin Pereira', '43', '23456743')"
cursor.execute(sentenciaSQL)

sentenciaSQL = "INSERT INTO reservas"
sentenciaSQL = sentenciaSQL + "VALUES ('Laura Gomez', '67', '13435671)"
cursor.execute(sentenciaSQL)

sentenciaSQL = "INSERT INTO reservas"
sentenciaSQL = sentenciaSQL + "VALUES ('Juan Res', '19', '44789194)"
cursor.execute(sentenciaSQL)

cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()

#select

conexion = sqlite3.connect("db/Reservas_de_Clientes.db")
cursor = conexion.cursor()

sentenciaSQL = "SELECT * FROM reservas"
cursor.execute(sentenciaSQL)

conexion.close()





