import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Models.Personas import Persona  # Asumo que importas correctamente el modelo Persona

class FormularioPersonas:
    def __init__(self, master):
        self.base = master
        self.base.geometry('1240x710')
        self.base.title('Formulario Persona')

        self.groupBox = LabelFrame(self.base, text="Formulario Persona", padx=50, pady=50)
        self.groupBox.grid(row=1, column=0, padx=15, pady=15)

        self.textBoxId = Entry(self.groupBox, state='disabled')  # Campo de ID deshabilitado
        self.textBoxId.grid(row=0, column=1, padx=(0, 10), pady=10)

        labelId = Label(self.groupBox, text="Id", width=10, font=("arial", 12))
        labelId.grid(row=0, column=0)

        # Nombre
        labelNombre = Label(self.groupBox, text="Ingrese su nombre", width=20, font=("arial", 10))
        labelNombre.grid(row=1, column=0)
        self.textBoxNombre = Entry(self.groupBox)
        self.textBoxNombre.grid(row=1, column=1, padx=(0, 10), pady=10)

        # Apellido
        labelApellido = Label(self.groupBox, text="Ingrese su apellido", width=20, font=("arial", 10))
        labelApellido.grid(row=2, column=0)
        self.textBoxApellido = Entry(self.groupBox)
        self.textBoxApellido.grid(row=2, column=1, padx=(0, 10), pady=10)

        # Teléfono
        labelTelefono = Label(self.groupBox, text="Ingrese su teléfono", width=20, font=("arial", 10))
        labelTelefono.grid(row=3, column=0)
        self.textBoxTelefono = Entry(self.groupBox)
        self.textBoxTelefono.grid(row=3, column=1, padx=(0, 10), pady=20)

        # Género
        labelGenero = Label(self.groupBox, text="Ingrese su género", width=20, font=("arial", 10))
        labelGenero.grid(row=4, column=0)
        self.selecciongenero = tk.StringVar()
        self.combox = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], textvariable=self.selecciongenero)
        self.combox.grid(row=4, column=1, padx=(0, 10), pady=10)
        self.selecciongenero.set("Selecciona un género")

        # Dirección
        labelDireccion = Label(self.groupBox, text="Ingrese su dirección", width=20, font=("arial", 10))
        labelDireccion.grid(row=5, column=0)
        self.textBoxDireccion = Entry(self.groupBox)
        self.textBoxDireccion.grid(row=5, column=1, padx=(0, 10), pady=10)

        Button(self.groupBox, text="Guardar", width=12, height=2, bg="blue", fg="white", command=self.guardarPersona).grid(row=6, column=0, padx=(0, 10), pady=20)
        Button(self.groupBox, text="Actualizar", width=12, height=2, bg="blue", fg="white",command=self.ActualizarPersona).grid(row=6, column=1, padx=(0, 20), pady=20)
        Button(self.groupBox, text="Eliminar", width=12, height=2, bg="blue", fg="white", command=self.EliminarPersona).grid(row=6, column=2, padx=(0, 20), pady=20)
        Button(self.groupBox, text="Limpiar Datos", width=12, height=2, bg="OrangeRed", fg="white",command=self.LimpiarCampos).grid(row=7, column=1, padx=(0, 20), pady=20)

        # Configuración de las columnas
        groupBoxListas = LabelFrame(self.base, text='Listas Personas', padx=5, pady=5)
        groupBoxListas.grid(row=0, column=0, padx=5, pady=5)

        self.tree = ttk.Treeview(groupBoxListas, columns=('Id', 'Nombres', 'Apellidos', 'Telefonos', 'Generos', 'Direcciones'),
                            show='headings', height=5)
        self.tree.column("#1", anchor="center")
        self.tree.heading("#1", text="Id")

        self.tree.column("#2", anchor="center")
        self.tree.heading("#2", text="Nombres")

        self.tree.column("#3", anchor="center")
        self.tree.heading("#3", text="Apellidos")

        self.tree.column("#4", anchor="center")
        self.tree.heading("#4", text="Telefono")

        self.tree.column("#5", anchor="center")
        self.tree.heading("#5", text="Genero")

        self.tree.column("#6", anchor="center")
        self.tree.heading("#6", text="Direcciones")

        self.tree.pack()

        # Asociar evento de clic en la tabla a la función de manejo
        self.tree.bind('<ButtonRelease-1>', self.seleccionDatosPersonas)

        # Mostrar datos en la tabla
        self.actualizarDatosTabla()

    def guardarPersona(self):
        try:
            nombres = self.textBoxNombre.get()
            apellidos = self.textBoxApellido.get()
            telefono = self.textBoxTelefono.get()
            genero = self.combox.get()
            direccion = self.textBoxDireccion.get()

            if nombres == "" or apellidos == "" or telefono == "" or genero == "" or direccion == "":
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
                return

            Persona.registroPersona(nombres, apellidos, telefono, genero, direccion)
            messagebox.showinfo("Datos guardados", "Correcto")
            self.actualizarDatosTabla()

            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:
            print("Error al ingresar los datos {}".format(error))

    def actualizarDatosTabla(self):
        self.tree.delete(*self.tree.get_children())
        try:
            datos = Persona.mostrarPersonas()
            for row in datos:
                self.tree.insert('', 'end', values=row)
        except ValueError as error:
            print("Error al actualizar los datos {}".format(error))

    def seleccionDatosPersonas(self, event):
        item = self.tree.selection()[0]  # Obtener el elemento seleccionado
        datos = self.tree.item(item, 'values')  # Obtener los valores del elemento

        # Mostrar los datos en los campos de texto
        self.textBoxId.config(state='normal')  # Habilitar el campo de ID
        self.textBoxId.delete(0, END)
        self.textBoxId.insert(0, datos[0])  # ID
        self.textBoxId.config(state='disabled')  # Volver a deshabilitar el campo de ID
        self.textBoxNombre.delete(0, END)
        self.textBoxNombre.insert(0, datos[1])  # Nombre
        self.textBoxApellido.delete(0, END)
        self.textBoxApellido.insert(0, datos[2])  # Apellido
        self.textBoxTelefono.delete(0, END)
        self.textBoxTelefono.insert(0, datos[3])  # Teléfono
        self.combox.set(datos[4])  # Género
        self.textBoxDireccion.delete(0, END)
        self.textBoxDireccion.insert(0, datos[5])  # Dirección

#Actualizacion de datos
    def ActualizarPersona(self):


        try:
            idClientes = self.textBoxId.get()
            nombres = self.textBoxNombre.get()
            apellidos = self.textBoxApellido.get()
            telefono = self.textBoxTelefono.get()
            genero = self.combox.get()
            direccion = self.textBoxDireccion.get()

            if idClientes == "" or nombres == "" or apellidos == "" or telefono == "" or genero == "" or direccion == "":
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
                return

            Persona.ActualizarDatos(idClientes, nombres, apellidos, telefono, genero, direccion)
            messagebox.showinfo("Datos fueron actualizados", "Correcto")
            self.actualizarDatosTabla()

            self.textBoxId.delete(0, END)
            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:
            print("Error al momento de actualizar los datos {}".format(error))

#Eliminar datos de personas
    def EliminarPersona(self):


        try:
            idClientes = self.textBoxId.get()


            Persona.ActualizarDatos(idClientes)
            messagebox.showinfo("Datos fueron eliminados", "Correcto")
            self.actualizarDatosTabla()

            self.textBoxId.config(state='normal')
            self.textBoxNombre.delete(0, END)
            self.textBoxApellido.delete(0, END)
            self.textBoxTelefono.delete(0, END)
            self.textBoxDireccion.delete(0, END)
            self.combox.set("Selecciona un género")

        except Exception as error:
            print("Error al momento de actualizar los datos {}".format(error))

#Limpiar campos
    def LimpiarCampos(self):
        self.textBoxId.config(state='normal')
        self.textBoxId.delete(0, END)
        self.textBoxId.config(state='disabled')
        self.textBoxNombre.delete(0, END)
        self.textBoxApellido.delete(0, END)
        self.textBoxTelefono.delete(0, END)
        self.textBoxDireccion.delete(0, END)
        self.combox.set("Selecciona un género")




if __name__ == "__main__":
    root = Tk()
    app = FormularioPersonas(root)
    root.mainloop()
