import tkinter as tk  # Importa el módulo tkinter para la creación de interfaces gráficas
from tkinter import *  # Importa todos los contenidos del módulo tkinter
from tkinter import ttk  # Importa el módulo ttk para widgets más avanzados
from tkinter import messagebox  # Importa el módulo messagebox para cuadros de mensajes

from Models.Personas import Persona  # Importa la clase Persona del módulo Models.Personas

class ListaPersonas:  # Define la clase ListaPersonas
    global tree  # Declara tree como una variable global
    tree = None  # Inicializa tree a None

    global textBoxId  # Declara textBoxId como una variable global
    textBoxId = None  # Inicializa textBoxId a None
    global textBoxNombre  # Declara textBoxNombre como una variable global
    textBoxNombre = None  # Inicializa textBoxNombre a None
    global textBoxApellido  # Declara textBoxApellido como una variable global
    textBoxApellido = None  # Inicializa textBoxApellido a None
    global textBoxTelefono  # Declara textBoxTelefono como una variable global
    textBoxTelefono = None  # Inicializa textBoxTelefono a None
    global combox  # Declara combox como una variable global
    combox = None  # Inicializa combox a None
    global textBoxDireccion  # Declara textBoxDireccion como una variable global
    textBoxDireccion = None  # Inicializa textBoxDireccion a None
    global ventana  # Declara ventana como una variable global
    tree = None  # Inicializa tree a None (redundante, ya inicializado antes)

    @staticmethod
    def listaPersonas():  # Define un método estático para listar personas
        global tree  # Hace referencia a la variable global tree
        global ventana  # Hace referencia a la variable global ventana
        global textBoxId  # Hace referencia a la variable global textBoxId
        global textBoxNombre  # Hace referencia a la variable global textBoxNombre
        global textBoxApellido  # Hace referencia a la variable global textBoxApellido
        global textBoxTelefono  # Hace referencia a la variable global textBoxTelefono
        global combox  # Hace referencia a la variable global combox
        global textBoxDireccion  # Hace referencia a la variable global textBoxDireccion

        try:
            ventana = Tk()  # Crea la ventana principal
            ventana.geometry('1230x240')  # Establece las dimensiones de la ventana
            ventana.title('Listas Personas')  # Establece el título de la ventana

            # Configuración de las columnas
            groupBox = LabelFrame(ventana, text='Listas Personas', padx=5, pady=5)  # Crea un marco con una etiqueta
            groupBox.grid(row=0, column=0, padx=5, pady=5)  # Posiciona el marco en la ventana

            # Crea un Treeview con columnas específicas
            tree = ttk.Treeview(groupBox, columns=('Id', 'Nombres', 'Apellidos', 'Telefonos', 'Generos', 'Direcciones'), show='headings', height=5)
            tree.column("#1", anchor="center")  # Configura la columna Id
            tree.heading("#1", text="Id")  # Establece el encabezado de la columna Id

            tree.column("#2", anchor="center")  # Configura la columna Nombres
            tree.heading("#2", text="Nombres")  # Establece el encabezado de la columna Nombres

            tree.column("#3", anchor="center")  # Configura la columna Apellidos
            tree.heading("#3", text="Apellidos")  # Establece el encabezado de la columna Apellidos

            tree.column("#4", anchor="center")  # Configura la columna Telefono
            tree.heading("#4", text="Telefono")  # Establece el encabezado de la columna Telefono

            tree.column("#5", anchor="center")  # Configura la columna Genero
            tree.heading("#5", text="Genero")  # Establece el encabezado de la columna Genero

            tree.column("#6", anchor="center")  # Configura la columna Direcciones
            tree.heading("#6", text="Direcciones")  # Establece el encabezado de la columna Direcciones

            tree.pack()  # Empaqueta el treeview en el marco

            # Muestra datos en el treeview
            for row in Persona.mostrarPersonas():  # Itera sobre los resultados de la consulta
                tree.insert('', 'end', values=row)  # Inserta cada fila en el treeview

            tree.bind("<<TreeviewSelect>>", seleccionListaPersonas)  # Vincula el evento de selección con la función seleccionListaPersonas

            ventana.mainloop()  # Inicia el bucle principal de la ventana

        except Exception as error:  # Captura cualquier excepción que ocurra
            print("Error al mostrar la interfaz: {}".format(error))  # Imprime un mensaje de error con el detalle del mismo

@staticmethod
def seleccionListaPersonas(event):  # Define un método estático para manejar la selección en el treeview
    try:
        itemSeleccionado = tree.focus()  # Obtiene el ítem seleccionado en el treeview

        if itemSeleccionado:  # Si hay un ítem seleccionado
            values = tree.item(itemSeleccionado)['values']  # Obtiene los valores del ítem seleccionado

            textBoxId.delete(0, 'END')  # Borra el contenido del textBoxId
            textBoxId.insert(0, values[0])  # Inserta el valor del ID en textBoxId
            textBoxNombre.delete(0, 'END')  # Borra el contenido del textBoxNombre
            textBoxNombre.insert(0, values[1])  # Inserta el valor del nombre en textBoxNombre
            textBoxApellido.delete(0, 'END')  # Borra el contenido del textBoxApellido
            textBoxApellido.insert(0, values[2])  # Inserta el valor del apellido en textBoxApellido
            textBoxTelefono.delete(0, 'END')  # Borra el contenido del textBoxTelefono
            textBoxTelefono.insert(0, values[3])  # Inserta el valor del teléfono en textBoxTelefono
            combox.set(values[4])  # Establece el valor del comboBox
            textBoxDireccion.delete(0, 'END')  # Borra el contenido del textBoxDireccion
            textBoxDireccion.insert(0, values[5])  # Inserta el valor de la dirección en textBoxDireccion
    except ValueError as error:  # Captura cualquier excepción de valor
        print("Error al mostrar la interfaz: {}".format(error))  # Imprime un mensaje de error con el detalle del mismo

# Crear una instancia de la clase y llamar al método listaPersonas
if __name__ == "__main__":
    ListaPersonas.listaPersonas()  # Llama al método listaPersonas de la clase ListaPersonas
