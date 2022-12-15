# Importamos las librerias
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Desarrollo de la interfaz
root = Tk()
root.title('CRUD con base de datos')
root.geometry('600x350')

miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()


def conexionBD():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            create table if not exists empleado
            (
                id int primary key auto_increment,
                nombre varchar(30) not null,
                cargo varchar(30) not null,
                salario int
            );''')
        messagebox.showinfo(
            'CONEXION', 'Base de datos conectada correctamente')
    except:
        messagebox.showerror('CONEXION', 'Surgio un error al conectar')
    miConexion.close()


def eliminarBD():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()
    if messagebox.askyesno(message='¿Los datos se perderan, desea continuar?', title='ADVERTENCIA'):
        miCursor.execute('DROP TABLE empleado')
    else:
        pass
    miConexion.close()
    limpiarCampos()
    mostrar()


def salirAplicacion():
    valor = messagebox.askquestion('Salir', '¿Está seguro que desea salir?')
    if valor == 'yes':
        root.destroy()


def limpiarCampos():
    miId.set('')
    miNombre.set('')
    miCargo.set('')
    miSalario.set('')


def mensaje():
    acerca = '''
        Aplicacion CRUD
        version 1.0
        Tecnologia PYTHON Tkinter
    '''
    messagebox.showinfo(
        'INFORMACION', acerca)

###########  METODOS CRUD  ###########


def crear():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()
    try:
        datos = (miNombre.get(), miCargo.get(), miSalario.get())
        miCursor.execute('INSERT INTO empleado values(NULL,%s,%s,%s)', (datos))
        miConexion.commit()
    except:
        messagebox.showwarning(
            'ADVERTENCIA', 'Ocurrió un error al crear el registro')
        pass
    miConexion.close()
    limpiarCampos()
    mostrar()


def mostrar():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        miCursor.execute('SELECT * FROM empleado')
        for row in miCursor:
            tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass
    miConexion.close()


def actualizar():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()
    try:
        datos = miNombre.get(), miCargo.get(), miSalario.get()
        miCursor.execute(
            'UPDATE empleado SET NOMBRE=%s, CARGO=%s, SALARIO=%s WHERE ID='+miId.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning(
            'ADVERTENCIA', 'Ocurrió un error al actualizar el registro')
        pass
    miConexion.close()
    limpiarCampos()
    mostrar()


def borrar():
    miConexion = mysql.connector.connect(
        host='localhost', user='root', passwd='', db='base')
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message='¿Quiere eliminar el registro', title='ADVERTENCIA'):
            miCursor.execute('DELETE FROM empleado WHERE ID='+miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning(
            'ADVERTENCIA', 'Ocurrió un error al eliminar el registro')
        pass
    miConexion.close()
    limpiarCampos()
    mostrar()


###########  TABLA  ###########

tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text='ID', anchor=CENTER)
tree.heading('#1', text='Nombre', anchor=CENTER)
tree.heading('#2', text='Cargo', anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text='Salario', anchor=CENTER)


def seleccionarUsandoClick(event):
    item = tree.identify('item', event.x, event.y)
    miId.set(tree.item(item, 'text'))
    miNombre.set(tree.item(item, 'values')[0])
    miCargo.set(tree.item(item, 'values')[1])
    miSalario.set(tree.item(item, 'values')[2])


tree.bind('<Double-1>', seleccionarUsandoClick)

###########  COLOCAR WIDGETS EN LA VISTA  ###########
menubar = Menu(root)
menuBaseDat = Menu(menubar, tearoff=0)
menuBaseDat.add_command(label='Conectar BD', command=conexionBD)
menuBaseDat.add_command(label='Eliminar BD', command=eliminarBD)
menuBaseDat.add_command(label='Salir', command=salirAplicacion)
menubar.add_cascade(label='Inicio', menu=menuBaseDat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label='Resetear campo', command=limpiarCampos)
ayudamenu.add_command(label='Acerca', command=mensaje)
menubar.add_cascade(label='Ayuda', menu=ayudamenu)

########### CREANDO ETIQUETAS Y CAJAS DE TEXTO ###########

e1 = Entry(root, textvariable=miId)

l2 = Label(root, text='Nombre: ')
l2.place(x=40, y=10)
e2 = Entry(root, textvariable=miNombre, width=50)
e2.place(x=100, y=10)

l3 = Label(root, text='Cargo: ')
l3.place(x=40, y=35)
e3 = Entry(root, textvariable=miCargo)
e3.place(x=100, y=35)

l4 = Label(root, text='Salario: ')
l4.place(x=280, y=35)
e4 = Entry(root, textvariable=miSalario, width=10)
e4.place(x=340, y=35)

l5 = Label(root, text='USD')
l5.place(x=430, y=35)

########### CREANDO BOTONES ###########

b1 = Button(root, text='Agregar', command=crear)
b1.place(x=40, y=90)

b2 = Button(root, text='Modificar', command=actualizar)
b2.place(x=120, y=90)

b3 = Button(root, text='Mostrar lista', command=mostrar)
b3.place(x=200, y=90)

b3 = Button(root, text='Eliminar', bg='yellow', command=borrar)
b3.place(x=310, y=90)

root.config(menu=menubar)

root.mainloop()
