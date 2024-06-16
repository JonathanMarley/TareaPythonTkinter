from Controllers.PersonaControllers import *  # Importa todos los contenidos de PersonaControllers

class Persona:  # Define la clase Persona

    @staticmethod
    def registroPersona(nombre, apellido, telefono, genero, direccion):  # Define un método estático para registrar una persona
        try:
            cone = Conexion.ConexionMysql()  # Establece una conexión a la base de datos
            cursor = cone.cursor()  # Crea un cursor para ejecutar comandos SQL
            # Define la consulta SQL para insertar un nuevo registro en la tabla clientes
            sql = "INSERT INTO clientes VALUES (null,%s,%s,%s,%s,%s);"
            # Crea una tupla con los valores que se insertarán en la tabla
            valores = (nombre, apellido, telefono, genero, direccion)
            cursor.execute(sql, valores)  # Ejecuta la consulta SQL con los valores proporcionados
            cone.commit()  # Confirma la transacción
            print(cursor.rowcount, "Registro de persona agregado")  # Imprime el número de registros agregados
            cone.close()  # Cierra la conexión a la base de datos

        except mysql.connector.Error as error:  # Captura cualquier error que ocurra durante la inserción de datos
            print("Error de ingreso de datos de persona {}".format(error))  # Imprime un mensaje de error con el detalle del mismo

    @staticmethod
    def mostrarPersonas():  # Define un método estático para mostrar todas las personas
        try:
            cone = Conexion.ConexionMysql()  # Establece una conexión a la base de datos
            cursor = cone.cursor()  # Crea un cursor para ejecutar comandos SQL
            cursor.execute("Select * from clientes;")  # Ejecuta una consulta SQL para seleccionar todos los registros de la tabla clientes
            resultados = cursor.fetchall()  # Recupera todos los registros obtenidos por la consulta
            cone.commit()  # Confirma la transacción
            cone.close()  # Cierra la conexión a la base de datos
            return resultados  # Devuelve los resultados obtenidos

        except mysql.connector.Error as error:  # Captura cualquier error que ocurra durante la consulta de datos
            print("Error de mostrar los datos de persona {}".format(error))  # Imprime un mensaje de error con el detalle del mismo

    @staticmethod
    def ActualizarDatos(id, nombre, apellido, telefono, genero, direccion):  # Define un método estático para actualizar los datos de una persona
        try:
            cone = Conexion.ConexionMysql()  # Establece una conexión a la base de datos
            cursor = cone.cursor()  # Crea un cursor para ejecutar comandos SQL
            # Define la consulta SQL para actualizar un registro en la tabla clientes
            sql = "UPDATE clientes SET clientes.nombre = %s, clientes.apellido = %s, clientes.telefono = %s, clientes.genero = %s, clientes.direccion = %s WHERE clientes.id = %s;"
            # Crea una tupla con los nuevos valores y el ID del registro que se actualizará
            valores = (nombre, apellido, telefono, genero, direccion, id)
            cursor.execute(sql, valores)  # Ejecuta la consulta SQL con los valores proporcionados
            cone.commit()  # Confirma la transacción
            print(cursor.rowcount, "Registro de persona actualizado")  # Imprime el número de registros actualizados
            cone.close()  # Cierra la conexión a la base de datos

        except mysql.connector.Error as error:  # Captura cualquier error que ocurra durante la actualización de datos
            print("Error al momento de actualizar los datos de persona {}".format(error))  # Imprime un mensaje de error con el detalle del mismo

    @staticmethod
    def EliminacionDatos(id):  # Define un método estático para eliminar los datos de una persona
        try:
            cone = Conexion.ConexionMysql()  # Establece una conexión a la base de datos
            cursor = cone.cursor()  # Crea un cursor para ejecutar comandos SQL
            # Define la consulta SQL para eliminar un registro en la tabla clientes
            sql = "DELETE from clientes WHERE clientes.id = %s;"
            valores = (id,)  # Crea una tupla con el ID del registro que se eliminará
            cursor.execute(sql, valores)  # Ejecuta la consulta SQL con el valor proporcionado
            cone.commit()  # Confirma la transacción
            print(cursor.rowcount, "Registro de persona eliminado")  # Imprime el número de registros eliminados
            cone.close()  # Cierra la conexión a la base de datos

        except mysql.connector.Error as error:  # Captura cualquier error que ocurra durante la eliminación de datos
            print("Error al momento de eliminar los datos de persona {}".format(error))  # Imprime un mensaje de error con el detalle del mismo