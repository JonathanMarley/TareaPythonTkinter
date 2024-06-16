import mysql.connector  # Importa el módulo mysql.connector para trabajar con bases de datos MySQL

class Conexion:  # Define la clase Conexion

    @staticmethod
    def ConexionMysql(): # Define un método estático llamado ConexionMysql
        conexion = None   # Inicializa la variable conexion a None
        try:
            # Intenta establecer una conexión con la base de datos MySQL usando los parámetros proporcionados
            conexion = mysql.connector.connect(user='root', password='',
                                               host='localhost', port='3306', database='Personas')
            print("Conexión correcta")  # Si la conexión es exitosa, imprime "Conexión correcta"
            return conexion              # Devuelve el objeto de conexión
        except mysql.connector.Error as err:  # Captura cualquier error que ocurra durante la conexión
            # Imprime un mensaje de error con el detalle del mismo
            print("Error al conectarte a la base de Datos: {}".format(err))
            return conexion  # Devuelve el objeto de conexión, aunque en este caso será None

# Llamada al método estático para establecer la conexión con la base de datos
Conexion.ConexionMysql()

#Crear metodos crud para la clase personas
