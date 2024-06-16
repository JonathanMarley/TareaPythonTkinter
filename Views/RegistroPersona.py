import tkinter as tk  # Importa el módulo tkinter para la creación de interfaces gráficas
from tkinter import *  # Importa todos los contenidos del módulo tkinter
from tkinter import ttk  # Importa el módulo ttk para widgets más avanzados
from tkinter import messagebox  # Importa el módulo messagebox para cuadros de mensajes

from Models.Personas import Persona  # Asumo que importas correctamente el modelo Persona

class FormularioPersonas:  # Define la clase FormularioPersonas
    def __init__(self, master):  # Método constructor
        self.base = master  # Ventana principal
        self.base.geometry('1240x710')  # Dimensiones de la ventana
        self.base.title('Formulario Persona')  # Título de la ventana

        self.groupBox = LabelFrame(self.base, text="Formulario Persona", padx=50, pady=50)  # Crea un marco para el formulario
        self.groupBox.grid(row=1, column=0, padx=15, pady=15)  # Posiciona el marco en la ventana

        self.textBoxId = Entry(self.groupBox, state='disabled')  # Campo de ID deshabilitado
        self.textBoxId.grid(row=0, column=1, padx=(0, 10), pady=10)  # Posiciona el campo de ID

        labelId = Label(self.groupBox, text="Id", width=10, font=("arial", 12))  # Etiqueta para ID
        labelId.grid(row=0, column=0)  # Posiciona la etiqueta de ID

        # Nombre
        labelNombre = Label(self.groupBox, text="Ingrese su nombre", width=20, font=("arial", 10))  # Etiqueta para Nombre
        labelNombre.grid(row=1, column=0)  # Posiciona la etiqueta de Nombre
        self.textBoxNombre = Entry(self.groupBox)  # Campo de entrada para Nombre
        self.textBoxNombre.grid(row=1, column=1, padx=(0, 10), pady=10)  # Posiciona el campo de Nombre

        # Apellido
        labelApellido = Label(self.groupBox, text="Ingrese su apellido", width=20, font=("arial", 10))  # Etiqueta para Apellido
        labelApellido.grid(row=2, column=0)  # Posiciona la etiqueta de Apellido
        self.textBoxApellido = Entry(self.groupBox)  # Campo de entrada para Apellido
        self.textBoxApellido.grid(row=2, column=1, padx=(0, 10), pady=10)  # Posiciona el campo de Apellido

        # Teléfono
        labelTelefono = Label(self.groupBox, text="Ingrese su teléfono", width=20, font=("arial", 10))  # Etiqueta para Teléfono
        labelTelefono.grid(row=3, column=0)  # Posiciona la etiqueta de Teléfono
        self.textBoxTelefono = Entry(self.groupBox)  # Campo de entrada para Teléfono
        self.textBoxTelefono.grid(row=3, column=1, padx=(0, 10), pady=20)  # Posiciona el campo de Teléfono

        # Género
        labelGenero = Label(self.groupBox, text="Ingrese su género", width=20, font=("arial", 10))  # Etiqueta para Género
        labelGenero.grid(row=4, column=0)  # Posiciona la etiqueta de Género
        self.selecciongenero = tk.StringVar()  # Variable para almacenar la selección del género
        self.combox = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], textvariable=self.selecciongenero)  # ComboBox para Género
        self.combox.grid(row=4, column=1, padx=(0, 10), pady=10)  # Posiciona el ComboBox de Género
        self.selecciongenero.set("Selecciona un género")  # Valor por defecto del ComboBox

        # Dirección
        labelDireccion = Label(self.groupBox, text="Ingrese su dirección", width=20, font=("arial", 10))  # Etiqueta para Dirección
        labelDireccion.grid(row=5, column=0)  # Posiciona la etiqueta de Dirección
        self.textBoxDireccion = Entry(self.groupBox)  # Campo de entrada para Dirección
        self.textBoxDireccion.grid(row=5, column=1, padx=(0, 10), pady=10)  # Posiciona el campo de Dirección

        # Botones
        Button(self.groupBox, text="Guardar", width=12, height=2, bg="blue", fg="white", command=self.guardarPersona).grid(row=6, column=0, padx=(0, 10), pady=20)  # Botón para Guardar
        Button(self.groupBox, text="Actualizar", width=12, height=2, bg="blue", fg="white", command=self.ActualizarPersona).grid(row=6, column=1, padx=(0, 20), pady=20)  # Botón para Actualizar
        Button(self.groupBox, text="Eliminar", width=12, height=2, bg="blue", fg="white", command=self.EliminarPersona).grid(row=6, column=2, padx=(0, 20), pady=20)  # Botón para Eliminar
        Button(self.groupBox, text="Limpiar Datos", width=12, height=2, bg="OrangeRed", fg="white", command=self.LimpiarCampos).grid(row=7, column=1, padx=(0, 20), pady=20)  # Botón para Limpiar Campos

        # Configuración de las columnas
        groupBoxListas = LabelFrame(self.base, text='Listas Personas', padx=5, pady=5)  # Crea un marco para la lista de personas
        groupBoxListas.grid(row=0, column=0, padx=5, pady=5)  # Posiciona el marco de la lista

        # Crea un Treeview con columnas específicas
        self.tree = ttk.Treeview(groupBoxListas, columns=('Id', 'Nombres', 'Apellidos', 'Telefonos', 'Generos', 'Direcciones'), show='headings', height=5)
        self.tree.column("#1", anchor="center")  # Configura la columna Id
        self.tree.heading("#1", text="Id")  # Encabezado de la columna Id

        self.tree.column("#2", anchor="center")  # Configura la columna Nombres
        self.tree.heading("#2", text="Nombres")  # Encabezado de la columna Nombres

        self.tree.column("#3", anchor="center")  # Configura la columna Apellidos
        self.tree.heading("#3", text="Apellidos")  # Encabezado de la columna Apellidos

        self.tree.column("#4", anchor="center")  # Configura la columna Telefono
        self.tree.heading("#4", text="Telefono")  # Encabezado de la columna Telefono

        self.tree.column("#5", anchor="center")  # Configura la columna Genero
        self.tree.heading("#5", text="Genero")  # Encabezado de la columna Genero

        self.tree.column("#6", anchor="center")  # Configura la columna Direcciones
        self.tree.heading("#6", text="Direcciones")  # Encabezado de la columna Direcciones

        self.tree.pack()  # Empaqueta el Treeview en el marco

        # Asociar evento de clic en la tabla a la función de manejo
        self.tree.bind('<ButtonRelease-1>', self.seleccionDatosPersonas)  # Vincula el evento de clic con la función seleccionDatosPersonas

        # Mostrar datos en la tabla
        self.actualizarDatosTabla()  # Llama a la función para actualizar los datos de la tabla

    def guardarPersona(self):  # Define el método para guardar una persona
        try:
            nombres = self.textBoxNombre.get()  # Obtiene el valor del campo Nombre
            apellidos = self.textBoxApellido.get()  # Obtiene el valor del campo Apellido
            telefono = self.textBoxTelefono.get()  # Obtiene el valor del campo Teléfono
            genero = self.combox.get()  # Obtiene el valor del ComboBox de Género
            direccion = self.textBoxDireccion.get()  # Obtiene el valor del campo Dirección

            if nombres == "" or apellidos == "" or telefono == "" or genero == "" or direccion == "":  # Verifica que no haya campos vacíos
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")  # Muestra una advertencia si hay campos vacíos
                return

            Persona.registroPersona(nombres, apellidos, telefono, genero, direccion)  # Llama al método registroPersona de la clase Persona
            messagebox.showinfo("Datos guardados", "Correcto")  # Muestra un mensaje de información
            self.actualizarDatosTabla()  # Actualiza los datos de la tabla

            # Limpia los campos del formulario
            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:  # Manejo de excepciones
            print("Error al ingresar los datos {}".format(error))  # Imprime el error en la consola

    def actualizarDatosTabla(self):  # Define el método para actualizar los datos de la tabla
        self.tree.delete(*self.tree.get_children())  # Elimina todos los elementos del Treeview
        try:
            datos = Persona.mostrarPersonas()  # Llama al método mostrarPersonas de la clase Persona
            for row in datos:  # Recorre los datos obtenidos
                self.tree.insert('', 'end', values=row)  # Inserta cada fila en el Treeview
        except ValueError as error:  # Manejo de excepciones
            print("Error al actualizar los datos {}".format(error))  # Imprime el error en la consola

    def seleccionDatosPersonas(self, event):  # Define el método para seleccionar datos de personas
        item = self.tree.selection()[0]  # Obtiene el elemento seleccionado
        datos = self.tree.item(item, 'values')  # Obtiene los valores del elemento

        # Muestra los datos en los campos de texto
        self.textBoxId.config(state='normal')  # Habilita el campo de ID
        self.textBoxId.delete(0, END)
        self.textBoxId.insert(0, datos[0])  # ID
        self.textBoxId.config(state='disabled')  # Vuelve a deshabilitar el campo de ID
        self.textBoxNombre.delete(0, END)
        self.textBoxNombre.insert(0, datos[1])  # Nombre
        self.textBoxApellido.delete(0, END)
        self.textBoxApellido.insert(0, datos[2])  # Apellido
        self.textBoxTelefono.delete(0, END)
        self.textBoxTelefono.insert(0, datos[3])  # Teléfono
        self.combox.set(datos[4])  # Género
        self.textBoxDireccion.delete(0, END)
        self.textBoxDireccion.insert(0, datos[5])  # Dirección

    def ActualizarPersona(self):  # Define el método para actualizar una persona
        try:
            idClientes = self.textBoxId.get()  # Obtiene el valor del campo ID
            nombres = self.textBoxNombre.get()  # Obtiene el valor del campo Nombre
            apellidos = self.textBoxApellido.get()  # Obtiene el valor del campo Apellido
            telefono = self.textBoxTelefono.get()  # Obtiene el valor del campo Teléfono
            genero = self.combox.get()  # Obtiene el valor del ComboBox de Género
            direccion = self.textBoxDireccion.get()  # Obtiene el valor del campo Dirección

            if idClientes == "" or nombres == "" or apellidos == "" or telefono == "" or genero == "" or direccion == "":  # Verifica que no haya campos vacíos
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")  # Muestra una advertencia si hay campos vacíos
                return

            Persona.ActualizarDatos(idClientes, nombres, apellidos, telefono, genero, direccion)  # Llama al método ActualizarDatos de la clase Persona
            messagebox.showinfo("Datos fueron actualizados", "Correcto")  # Muestra un mensaje de información
            self.actualizarDatosTabla()  # Actualiza los datos de la tabla

            # Limpia los campos del formulario
            self.textBoxId.delete(0, END)
            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:  # Manejo de excepciones
            print("Error al momento de actualizar los datos {}".format(error))  # Imprime el error en la consola

    def EliminarPersona(self):  # Define el método para eliminar una persona
        try:
            idClientes = self.textBoxId.get()  # Obtiene el valor del campo ID

            Persona.EliminacionDatos(idClientes)  # Llama al método EliminarDatos de la clase Persona
            messagebox.showinfo("Datos fueron eliminados", "Correcto")  # Muestra un mensaje de información
            self.actualizarDatosTabla()  # Actualiza los datos de la tabla

            # Limpia los campos del formulario
            self.textBoxId.config(state='normal')
            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:  # Manejo de excepciones
            print("Error al momento de eliminar los datos {}".format(error))  # Imprime el error en la consola

    def LimpiarCampos(self):  # Define el método para limpiar los campos del formulario
        self.textBoxId.config(state='normal')  # Habilita el campo de ID
        self.textBoxId.delete(0, END)  # Limpia el campo de ID
        self.textBoxId.config(state='disabled')  # Deshabilita el campo de ID
        self.textBoxNombre.delete(0, END)  # Limpia el campo de Nombre
        self.textBoxApellido.delete(0, END)  # Limpia el campo de Apellido
        self.textBoxTelefono.delete(0, END)  # Limpia el campo de Teléfono
        self.textBoxDireccion.delete(0, END)  # Limpia el campo de Dirección
        self.combox.set("Selecciona un género")  # Restablece el valor del ComboBox

if __name__ == "__main__":  # Punto de entrada de la aplicación
    root = Tk()  # Crea la ventana principal
    app = FormularioPersonas(root)  # Crea una instancia de FormularioPersonas
    root.mainloop()  # Inicia el bucle principal de la ventana