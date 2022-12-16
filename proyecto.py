from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import re

"""###########################################
        CREAR RAIZ DE LA INTERFAZ
###########################################"""
root = Tk()
root.title('Proyecto final FDP')
root.geometry('650x350')

"""###########################################
            VARIABLES GLOBALES
###########################################"""
programaActual = ''
seleccionado = ''
dataDefectoP1 = '''Matematica,0,0,0,0,0,0
Programación,0,0,0,0,0,0
Taller,0,0,0,0,0,0
Definitiva Matematica,0
Definitiva Programación,0
Definitiva Taller,0
promedio,0'''
dataDefectoP2 = '''Cálculo,0,0,0,0,0,0
Proceso administrativo,0,0,0,0,0,0
Taller,0,0,0,0,0,0
Definitiva Cálculo,0
Definitiva Proceso administrativo,0
Definitiva Fundamentos de contabilidad,0
promedio,0'''

# Campos de text para las materias
nota1 = StringVar()
nota2 = StringVar()
nota3 = StringVar()

# Campos de text para los estudiante
codigo_estu = StringVar()  # Pregunta pal profesor, porque no se puede poner antes
nombre_estu = StringVar()

"""###########################################
            LOGICA DEL SOFTWARE
###########################################"""


def leerArchivo(name):
    file = open(f'programas/{name}', 'r+')
    return file.readlines()


def validar_estudiante():
    if len(nombre_estu.get()) == 0:
        nombre_estu.set('N/A')
    if len(codigo_estu.get()) == 0:
        codigo_estu.set('N/A')
    data = f'{nombre_estu.get()},{codigo_estu.get()}'
    return data


def seleccionarEstudiante(event):
    global seleccionado

    item = tree.identify('item', event.x, event.y)
    nombre_estu.set(tree.item(item, 'values')[0])
    codigo_estu.set(tree.item(item, 'values')[1])

    seleccionado = separar()


def ver_table_estudiante():
    # Borramos los datos que ya tenia
    logs = tree.get_children()
    for element in logs:
        tree.delete(element)
    res = leerArchivo(f'{programaActual}/estudianteP.txt')
    if not len(res) == 0:
        cont = 0
        for line in res:
            cont += 1
            d_split = line.split(',')
            tree.insert('', END, text=cont, iid=cont, values=(
                d_split[0], d_split[1]))
            print(f'{d_split[0]} {d_split[1]}')


def menu_bienvenida():
    labelBorrar()  # Limpiamos el frame o la interfaz
    l_mensaje = Label(root, text='--- Todos aprendemos ---', width=50)
    btn_ingresar = Button(root, text='INGRESAR', command=menu_programas)
    l_mensaje.place(x=120, y=100)
    btn_ingresar.place(x=270, y=150, width=100, height=40)
    # Se crean los archivos iniciales
    crear_carpetas('programa1', 'estudianteP')
    # Se crean los archivos iniciales
    crear_carpetas('programa2', 'estudianteP')
    root.update()


def menu_programas():
    labelBorrar()  # Limpiamos el frame o la interfaz
    l_mensaje = Label(
        root, text='Presione la carrera que desea ingresar', width=50)
    btn_p1 = Button(
        root, text='1. Tecnologia en Desarrollo de software', command=menu_p1)
    btn_p2 = Button(root, text='2. Administración de empresas',
                    command=menu_p2)
    btn_salir = Button(root, text='Salir del software', command=salir)
    l_mensaje.place(x=120, y=100)
    btn_p1.place(x=180, y=150, width=300, height=40)
    btn_p2.place(x=180, y=200, width=300, height=40)
    btn_salir.place(x=180, y=250, width=300, height=40)
    root.update()


def menu_p1():
    global programaActual
    programaActual = 'programa1'
    labelBorrar()  # Limpiamos el frame o la interfaz
    l_mensaje = Label(
        root, text='Tecnologia en Desarrollo de software', width=50)
    btn_info = Button(root, text='Información', command=info, width=50)
    btn_obje = Button(root, text='Objetivos', command=objetivo, width=50)
    btn_entrar = Button(root, text='Entrar', command=entrar, width=50)
    btn_volver = Button(root, text='Volver', command=menu_programas, width=50)
    l_mensaje.place(x=120, y=50)
    btn_info.place(x=100, y=100)
    btn_obje.place(x=100, y=150)
    btn_entrar.place(x=100, y=200)
    btn_volver.place(x=100, y=250)
    root.update()


def menu_p2():
    global programaActual
    programaActual = 'programa2'
    labelBorrar()  # Limpiamos el frame o la interfaz
    l_mensaje = Label(
        root, text='Administración de empresas', width=50)
    btn_info = Button(root, text='Información', command=info, width=50)
    btn_obje = Button(root, text='Objetivos', command=objetivo, width=50)
    btn_entrar = Button(root, text='Entrar', command=entrar, width=50)
    btn_volver = Button(root, text='Volver', command=menu_programas, width=50)
    l_mensaje.place(x=120, y=50)
    btn_info.place(x=100, y=100)
    btn_obje.place(x=100, y=150)
    btn_entrar.place(x=100, y=200)
    btn_volver.place(x=100, y=250)
    root.update()


def crear_carpetas(path, name):
    if not os.path.exists('programas'):
        os.mkdir('programas')
    if not os.path.exists(f'programas/{path}'):
        os.mkdir(f'programas/{path}')
    if not len(name) == 0:
        pestudiante = open(f'programas/{path}/{name}.txt', 'a+')
        print(f'archivo {name} creado')
        pinfo = open(f'programas/{path}/infop.txt', 'a+')
        print(f'archivo info {name} creado')
        pobje = open(f'programas/{path}/objep.txt', 'a+')
        print(f'archivo objetivo {name} creado')
    with open(f'programas/general.txt', 'a+') as pg:
        print(f'archivo general creado')


def info():
    info = []
    with open(f'programas/{programaActual}/infop.txt', 'r+') as archivo:
        for linea in archivo:
            # :-1: es para quitar un salto de linea rarito
            info.append(linea[:-1:])
    mensaje = ""  # Agregamos todo aca
    for parte in info:
        mensaje += f'{parte}\n'
    # Parte definimos lo que queremos mostrar en el frame
    if programaActual == 'programa1':
        btn_volver = Button(root, text='Volver', command=menu_p1, width=50)
    else:
        btn_volver = Button(root, text='Volver', command=menu_p2, width=50)
    frameScroll = Frame(root)
    scroll = Scrollbar(frameScroll)
    textArea = Text(frameScroll, height=4, width=300)
    scroll.pack(side=RIGHT, fill=Y)
    textArea.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)
    # Agregamos informacion pertienente del archivo
    textArea.insert(END, mensaje)
    # Agregamos esa vaina a la interfaz
    frameScroll.place(x=10, y=10, width=630, height=300)
    btn_volver.place(x=100, y=310)


def objetivo():
    info = []
    with open(f'programas/{programaActual}/objep.txt', 'r+') as archivo:
        for linea in archivo:
            # :-1: es para quitar un salto de linea rarito
            info.append(linea[:-1:])

    mensaje = ""  # Agregamos todo aca
    for parte in info:
        mensaje += f'{parte}\n'
    # Parte definimos lo que queremos mostrar en el frame
    if programaActual == 'programa1':
        btn_volver = Button(root, text='Volver', command=menu_p1, width=50)
    else:
        btn_volver = Button(root, text='Volver', command=menu_p2, width=50)
    frameScroll = Frame(root)
    scroll = Scrollbar(frameScroll)
    textArea = Text(frameScroll, height=4, width=300)
    scroll.pack(side=RIGHT, fill=Y)
    textArea.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)
    # Agregamos informacion pertienente del archivo
    textArea.insert(END, mensaje)
    # Agregamos esa vaina a la interfaz
    frameScroll.place(x=10, y=10, width=630, height=300)
    btn_volver.place(x=100, y=310)


def separar():
    nombre = re.sub(r'\n', '', nombre_estu.get())
    codigo = re.sub(r'\n', '', codigo_estu.get())
    linea = (f'{nombre},{codigo}\n')
    return linea


def archivo_por_estudiante():
    nombre = re.sub(r'\n', '', separar())
    with open(f'programas/{programaActual}/{nombre}.txt', 'a+') as archivo:
        if programaActual == 'programa1':
            archivo.write(separar()+dataDefectoP1)
        else:
            archivo.write(separar()+dataDefectoP2)


def editar_por_estudiante():
    nombreActual = re.sub(r'\n', '', seleccionado)
    res = leerArchivo(f'{programaActual}/{nombreActual}.txt')
    res[0] = separar()
    nuevoNombre = re.sub(r'\n', '', separar())
    sobreescribir(f'{programaActual}/{nuevoNombre}.txt', res)
    os.remove(f'programas/{programaActual}/{nombreActual}.txt')


def notas():
    nombre = re.sub(r'\n', '', seleccionado)
    res = leerArchivo(f'{programaActual}/{nombre}.txt')
    # Separamos por linea del archivo y materia
    mate = res[1].split(',')
    fdp = res[2].split(',')
    taller = res[3].split(',')
    lineMate = res[4].split(',')
    lineFDP = res[5].split(',')
    lineTaller = res[6].split(',')
    lineProm = res[7].split(',')
    # Caculamos la definitiva
    defiMate = ((int(mate[1])*int(mate[2]))/100) + ((int(mate[3])
                                                     * int(mate[4]))/100) + ((int(mate[5])*int(mate[6]))/100)
    defiFDP = ((int(fdp[1])*int(fdp[2]))/100) + ((int(fdp[3])
                                                  * int(fdp[4]))/100) + ((int(fdp[5])*int(fdp[6]))/100)
    defiTaller = ((int(taller[1])*int(taller[2]))/100) + (
        (int(taller[3])*int(taller[4]))/100) + ((int(taller[5])*int(taller[6]))/100)
    
    # Calculamos el promedio
    promedio = (defiMate + defiFDP + defiTaller)/3
    # Reemplazamos la lista del archivo
    res[4] = f'Definitiva Matematica,{defiMate}\n'
    res[5] = f'Definitiva Programación,{defiFDP}\n'
    res[6] = f'Definitiva Taller,{defiTaller}\n'
    res[7] = f'promedio,{promedio}\n'
    # Sobreescrimos la informacion actual
    sobreescribir(f'{programaActual}/{nombre}.txt', res)

def guardar():
    archivo = open(f'programas/{programaActual}/estudianteP.txt', 'a+')
    data = validar_estudiante()
    archivo.write(f'{data}\n')
    archivo_por_estudiante()
    limpiar()
    ok()
    ver_table_estudiante()


def sobreescribir(archivo, data):
    with open(f'programas/{archivo}', 'w+') as archivo:
        for linea in data:
            archivo.write(linea)


def modificar():
    try:
        res = leerArchivo(f'{programaActual}/estudianteP.txt')
        posicion = res.index(seleccionado)
        res[posicion] = separar()
        sobreescribir(f'{programaActual}/estudianteP.txt', res)
        editar_por_estudiante()
        ver_table_estudiante()
        limpiar()
        ok()
    except ValueError:
        error_lista()


def eliminar():
    try:
        nombre = re.sub(r'\n', '', seleccionado)
        os.remove(f'programas/{programaActual}/{nombre}.txt')
        res = leerArchivo(f'{programaActual}/estudianteP.txt')
        lineaBorrar = separar()
        posicion = res.index(lineaBorrar)
        res.pop(posicion)
        sobreescribir(f'{programaActual}/estudianteP.txt', res)
        ver_table_estudiante()
        limpiar()
        ok()
    except ValueError:
        error_lista()

def agregarNotas():
    labelBorrar()  # Limpiamos el frame o la interfaz
    menuBoton()
    inputsEstudiante() # Entradas por defecto
    # Labels
    l_nota1 = Label(root,text='Nota 1: ')
    l_nota2 = Label(root,text='Nota 2: ')
    l_nota3 = Label(root,text='Nota 3: ')
    # Entradas
    e_nota1 = Entry(root, textvariable=nota1, width=50)
    e_nota2 = Entry(root, textvariable=nota2, width=50)
    e_nota3 = Entry(root, textvariable=nota3, width=50)
    # BOTONES PARA EL PROCESO DE TXT
    btn_buscar = Button(root, text='Buscar')
    # Agregamos a la interfaz
    btn_buscar.place(x=570,y=60)
    l_nota1.place(x=20,y=110)
    l_nota2.place(x=20,y=140)
    l_nota3.place(x=20,y=170)
    prevenir()
    
def inputsEstudiante():
    # Labels
    l_codigo = Label(root, text='Codigo estudiante: ')
    l_nombre = Label(root, text='Nombre estudiante: ')
    # Entradas
    e_codigo = Entry(root, textvariable=codigo_estu, width=50)
    e_nombre = Entry(root, textvariable=nombre_estu, width=50)
    # Agregamos a la interfaz
    l_codigo.place(x=20, y=50)
    l_nombre.place(x=20, y=80)
    e_codigo.place(x=160, y=50)
    e_nombre.place(x=160, y=80)
    btn_guardar = Button(root, text='Guardar', command=guardar)
    
def agregarEstudiante():
    global tree
    labelBorrar()  # Limpiamos el frame o la interfaz
    menuBoton()
    inputsEstudiante() # Entradas por defecto
    # BOTONES PARA EL PROCESO DE TXT
    btn_guardar = Button(root, text='Agregar', command=guardar)
    btn_mostrar = Button(root, text='Mostrar', command=ver_table_estudiante)
    btn_modificar = Button(root, text='Modificar', command=modificar)
    btn_eliminar = Button(root, text='Eliminar', command=eliminar)
    btn_limpiar = Button(root, text='Limpiar', command=limpiar)
    # Agregamos a la interfaz
    btn_guardar.place(x=30, y=110)
    btn_mostrar.place(x=120, y=110)
    btn_modificar.place(x=210, y=110)
    btn_eliminar.place(x=310, y=110)
    btn_limpiar.place(x=410, y=110)
    """###########################################
           AGREGAMOS LA TABLA DE ESTUDIANTES
    ###########################################"""
    tree = ttk.Treeview(height=9, columns=('#0', '#1', '#2'))
    tree.column('#0', width=100)
    tree.heading('#0', text='#', anchor=CENTER)
    tree.heading('#1', text='Nombre', anchor=CENTER)
    tree.heading('#2', text='Codigo', anchor=CENTER)
    tree.column('#3', width=150)
    tree.heading('#3', text='Promedio', anchor=CENTER)
    tree.place(x=10, y=150)
    ver_table_estudiante()
    tree.bind('<Double-1>', seleccionarEstudiante)


def menuBoton():
    labelBorrar()  # Limpiamos el frame o la interfaz
    btn_agregar = Button(root, text='Agregar', command=agregarEstudiante)
    btn_notas = Button(root, text='Notas', command=agregarNotas)
    btn_volver = Button(root, text='Volver', command=menu_p1)
    btn_agregar.place(x=10, y=10)
    btn_notas.place(x=100, y=10)
    btn_volver.place(x=180, y=10)


def entrar():
    labelBorrar()  # Limpiamos el frame o la interfaz
    menuBoton()
    agregarEstudiante()


def labelBorrar():
    l_borrar = Label(root, text='')
    l_borrar.place(x=10, y=10, width=650, height=350)  # Limpiamos el frame


def limpiar():
    nombre_estu.set('')
    codigo_estu.set('')


def salir():
    root.destroy()


def error_lista():
    messagebox.showwarning(
        'ERROR', 'El estudiante ingresado no se encuentra en el sistema.')

def prevenir():
    messagebox.showinfo('MENSAJE', 'Recuerde buscar el estudiante primero.')

def ok():
    messagebox.showinfo('MENSAJE', 'La operación funciono correctamente.')

menu_bienvenida()
root.mainloop()
