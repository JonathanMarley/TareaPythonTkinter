import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Models.Personas import Persona

class ListaPersonas:
    global tree
    tree = None

    global textBoxId
    textBoxId = None
    global textBoxNombre
    textBoxNombre = None
    global textBoxApellido
    textBoxApellido = None
    global textBoxTelefono
    textBoxTelefono = None
    global combox
    combox = None
    global textBoxDireccion
    textBoxDireccion = None
    global ventana
    tree = None

    @staticmethod
    def listaPersonas():
        global tree
        global ventana
        global textBoxId
        global textBoxNombre
        global textBoxApellido
        global textBoxTelefono
        global combox
        global textBoxDireccion

        try:
            ventana = Tk()  # Crear la ventana secundaria
            ventana.geometry('1230x240')
            ventana.title('Listas Personas')

            # Configuración de las columnas
            groupBox = LabelFrame(ventana, text='Listas Personas', padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=5, pady=5)

            tree = ttk.Treeview(groupBox, columns=('Id', 'Nombres', 'Apellidos', 'Telefonos', 'Generos', 'Direcciones'), show='headings', height=5)
            tree.column("#1", anchor="center")
            tree.heading("#1", text="Id")

            tree.column("#2", anchor="center")
            tree.heading("#2", text="Nombres")

            tree.column("#3", anchor="center")
            tree.heading("#3", text="Apellidos")

            tree.column("#4", anchor="center")
            tree.heading("#4", text="Telefono")

            tree.column("#5", anchor="center")
            tree.heading("#5", text="Genero")

            tree.column("#6", anchor="center")
            tree.heading("#6", text="Direcciones")



            tree.pack()

            #Mostrar datos de la tablas
            for row in Persona.mostrarPersonas():
                tree.insert('', 'end', values=row)

            tree.bind("<<TreeviewSelect>>",seleccionListaPersonas)



            ventana.mainloop()

        except Exception as error:
            print("Error al mostrar la interfaz: {}".format(error))

@staticmethod
def seleccionListaPersonas(event):
    try:
        itemSeleccionado = tree.focus()

        if itemSeleccionado:

         values = tree.item(itemSeleccionado)['values']

        textBoxId.delete(0, 'END')
        textBoxId.insert(0, values[0])
        textBoxNombre.delete(0, 'END')
        textBoxNombre.insert(0, values[1])
        textBoxApellido.delete(0, 'END')
        textBoxApellido.insert(0, values[2])
        textBoxTelefono.delete(0, 'END')
        textBoxTelefono.insert(0, values[3])
        combox.set(values[4])
        textBoxDireccion.delete(0, 'END')
        textBoxDireccion.insert(0, values[5])
    except ValueError as error:
        print("Error al mostrar la interfaz: {}".format(error))

# Crear una instancia de la clase y llamar al método formularioPersona
if __name__ == "__main__":
    ListaPersonas.listaPersonas()



