from tkinter import *
from tkinter import ttk
import os
import re

# Declaracion variables globales
programaActual = 'programa1'

# Declaracion de la raiz de nuestra interfaz
root = Tk()
root.title('Proyecto final FDP')
root.geometry('650x350')

# Campos de texto programa
name_program = StringVar()
cant_semesters_program = IntVar()
cant_subjects_program = IntVar()

# Campos de texto estudiantes
code_student = StringVar()
name_student = StringVar()

# Campos de text para las materias
name_subjects = StringVar()
rating_subjects = DoubleVar()
porcentage_subjects = DoubleVar()

# Tablas en la interfaz
tree_student = ttk.Treeview(height=10, columns=('#0', '#1'))

"""############################################
        Agregar tabla de programas
############################################"""


def table_student():
    tree_student.column('#0', width=100)
    tree_student.heading('#0', text='#', anchor=CENTER)
    tree_student.heading('#1', text='Nombre', anchor=CENTER)
    tree_student.heading('#2', text='Codigo', anchor=CENTER)


"""############################################
        Parte logica del software
############################################"""


def select_student(event):
    item = tree_student.identify('item', event.x, event.y)
    code_student.set(tree_student.item(item, 'values')[1])
    name_student.set(tree_student.item(item, 'values')[0])


tree_student.bind('<Double-1>', select_student)


def create_student_program(path, name):
    if not os.path.exists('programas'):
        os.mkdir('programas')
    if not os.path.exists(f'programas/{path}'):
        os.mkdir(f'programas/{path}')
    if not len(name) == 0:
        with open(f'programas/{path}/{name}.txt', 'a+') as p:
            print(f'archivo {name} creado')
    with open(f'programas/general.txt', 'a+') as p:
        print(f'archivo general creado')


def read_file(name):
    file = open(f'programas/{name}', 'r+')
    return file.readlines()

def validar_estudiante():
    if len(name_student.get()) == 0:
        name_student.set('N/A')
    if len(code_student.get()) == 0:
        code_student.set('N/A')
    data = f'{name_student.get()},{code_student.get()}'
    return data
    
def add_tree_student():
    file = open(f'programas/{programaActual}/estudianteP.txt', 'a+')
    data = validar_estudiante()
    file.write(f'{data}\n')
    show_tree_student()

def show_tree_student():
    # Borramos los datos que ya tenia
    logs = tree_student.get_children()
    for element in logs:
        tree_student.delete(element)
    res = read_file(f'{programaActual}/estudianteP.txt')
    if not len(res) == 0:
        cont = 0
        for line in res:
            cont += 1
            d_split = line.split(',')
            tree_student.insert('', 0, text=cont, values=(
                d_split[0], d_split[1]))

def sobreescribir(archivo,data):
    with open(f'programas/{archivo}','w+') as archivo:
        for linea in data:
            archivo.write(linea)
        
def delete_tree_student():
    res = read_file(f'{programaActual}/estudianteP.txt')
    print(res)
    nombre = re.sub(r'\n','',name_student.get())
    codigo = re.sub(r'\n','',code_student.get())
    lineaBorrar = (f'{nombre},{codigo}\n')
    posicion = res.index(lineaBorrar)
    res.pop(posicion)
    sobreescribir(f'{programaActual}/estudianteP.txt', res)
    show_tree_student()

"""############################################
        Declaracion de widgets
############################################"""

# Declarando los labels de programas
label_n_program = Label(root, text='Nombre del programa: ')
label_c_sem_program = Label(root, text='Cantidad de semestres: ')
label_c_sub_program = Label(root, text='Cantidad de materias (Por semestre): ')

# Declarando las entradas de programas
txt_n_program = Entry(root, textvariable=name_program, width=40)
txt_c_sem_program = Entry(root, textvariable=cant_semesters_program, width=40)
txt_c_sub_program = Entry(root, textvariable=cant_subjects_program, width=40)

# Declarando los labels de estudiantes
label_code_student = Label(root, text='Codigo del estudiante: ')
label_name_student = Label(root, text='Nombre del estudiante: ')

# Declarando las entradas de estudiantes 
txt_code_student = Entry(root, textvariable=code_student, width=40)
txt_name_student = Entry(root, textvariable=name_student, width=40)

# Declarando todos los botones
btn_show_table = Button(root, text='Mostrar', command=show_tree_student)
btn_add_table = Button(root, text='Agregar', command=add_tree_student)
btn_update_table = Button(root, text='Modificar', command=show_tree_student)
btn_remove_table = Button(root, text='Eliminar', command=delete_tree_student)

"""############################################
        Agregar widgets a la interfaz
############################################"""

# Todos los labels
# label_n_program.place(x=10, y=40)
# label_c_sem_program.place(x=10, y=60)
# label_c_sub_program.place(x=10, y=80)
label_code_student.place(x=10, y=40)
label_name_student.place(x=10, y=60)
# Todos los inputs
# txt_n_program.place(x=260, y=40)
# txt_c_sem_program.place(x=260, y=60)
# txt_c_sub_program.place(x=260, y=80)
txt_code_student.place(x=260, y=40)
txt_name_student.place(x=260, y=60)

# Todas las tablas
tree_student.place(x=0, y=150)

# Todos los botones
btn_add_table.place(x=100, y=110)
btn_show_table.place(x=180, y=110)
btn_update_table.place(x=260, y=110)
btn_remove_table.place(x=350, y=110)

create_student_program('programa1', 'estudianteP')
create_student_program('programa2', 'estudianteP')
table_student()
show_tree_student()

# Ejecutamos nuestra interfaz
root.mainloop()
