from tkinter import *
from tkinter import ttk

"""############################################
        Parte logica del software
############################################"""
def read_file(name):
        file = open(name, 'r+')
        return file.readlines()
def add_tree_program():
        file = open('programas.txt','a+')
        data = [name_program.get(), cant_semesters_program.get(), cant_subjects_program.get()]
        file.write(f'{data}\n')
def show_tree_program():
        # Borramos los datos que ya tenia
        registros = tree_program.get_children()
        for element in registros:
                tree_program.delete(element)
        res = read_file('programas.txt')
        print(res[0])
        cont=0
        for line in res:
                cont+=1
                tree_program.insert('', 0, text=cont, values=(line[0], line[1], line[2]))
        

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

# Declarando todos los botones
btn_show_table = Button(root, text='Mostrar', command=show_tree_program)
btn_add_table = Button(root, text='Agregar', command=add_tree_program)
btn_update_table = Button(root, text='Modificar', command=show_tree_program)
btn_remove_table = Button(root, text='Eliminar', command=show_tree_program)

"""############################################
        Agregar tabla de programas
############################################"""
tree_program = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
tree_program.column('#0', width=100)
tree_program.heading('#0', text='#', anchor=CENTER)
tree_program.heading('#1', text='Nombre', anchor=CENTER)
tree_program.heading('#2', text='Cant. semestres', anchor=CENTER)
tree_program.column('#3', width=140)
tree_program.heading('#3', text='Cant. Cursos', anchor=CENTER)

"""############################################
        Agregar widgets a la interfaz
############################################"""

# Todos los labels
label_n_program.place(x=10, y=40)
label_c_sem_program.place(x=10, y=60)
label_c_sub_program.place(x=10, y=80)

# Todos los inputs
txt_n_program.place(x=260, y=40)
txt_c_sem_program.place(x=260, y=60)
txt_c_sub_program.place(x=260, y=80)

# Todas las tablas
tree_program.place(x=0, y=150)

# Todos los botones
btn_add_table.place(x=100, y=110)
btn_show_table.place(x=180, y=110)
btn_update_table.place(x=260, y=110)
btn_remove_table.place(x=350, y=110)
show_tree_program()
# Ejecutamos nuestra interfaz
root.mainloop()
