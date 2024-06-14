
from Controllers.PersonaControllers import *


class Persona:

    @staticmethod
    def registroPersona(nombre, apellido, telefono, genero, direccion):

        try:
            cone = Conexion.ConexionMysql()
            cursor = cone.cursor()
            sql = "INSERT INTO clientes VALUES (null,%s,%s,%s,%s,%s);"
            valores = (nombre, apellido, telefono, genero, direccion)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount, "Registro de persona agregado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos de persona {}".format(error))

    @staticmethod
    def mostrarPersonas():
        try:
            cone = Conexion.ConexionMysql()
            cursor = cone.cursor()
            cursor.execute("Select * from clientes;")
            resultados = cursor.fetchall()
            cone.commit()
            cone.close()
            return resultados

        except mysql.connector.Error as error:
            print("Error de mostrar los datos de persona {}".format(error))

#Actualizar datos de personas
    @staticmethod
    def ActualizarDatos(id, nombre, apellido, telefono, genero, direccion):
        try:
            cone = Conexion.ConexionMysql()
            cursor = cone.cursor()
            sql = "UPDATE clientes SET clientes.nombre = %s,clientes.apellido = %s,clientes.telefono = %s,clientes.genero = %s,clientes.direccion = %s WHERE clientes.id = %s;"
            valores = (nombre, apellido, telefono, genero, direccion, id)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro de persona actualizado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al momento de actualizar los datos de persona {}".format(error))

#Eliminar datos de personas
    @staticmethod
    def EliminacionDatos(id):
        try:
            cone = Conexion.ConexionMysql()
            cursor = cone.cursor()
            sql = "DELETE from clientes  WHERE clientes.id = %s;"
            valores = (id,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount,"Registro de persona eliminado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al momento de eliminar los datos de persona {}".format(error))




