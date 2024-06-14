import mysql.connector

class Conexion:

    @staticmethod
    def ConexionMysql():
        conexion = None
        try:
            conexion = mysql.connector.connect(user='root', password='',
                                               host='localhost', port='3306', database='Personas')
            print("Conexión correcta")
            return conexion
        except mysql.connector.Error as err:
            print("Error al conectarte a la base de Datos: {}".format(err))
            return conexion

# Llamada al método estático
Conexion.ConexionMysql()

#Crear metodos crud para la clase personas
