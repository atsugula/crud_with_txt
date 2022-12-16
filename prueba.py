# leer el archivo y devolver la lista
def leer(nombre_archivo):
    with open(nombre_archivo, 'r+') as archivo:
        return archivo.readlines()
# Modificar el archivo de texto, sobreescribiendo
def modificar():
    carlos = leer('prueba.txt')
    carlos[1] = 'linea modificada\n'
    with open('prueba.txt', 'w+') as archivo:
        print(carlos)
        for linea in carlos:
            archivo.write(linea)

def eliminar():
    carlos = leer('prueba.txt')
    print(carlos)
    # indice = carlos.index('linea modificada2')
    print(carlos.index('taller\n')) # Eliminar por posicion
    carlos[1] = 'linea modificada\n'
    with open('prueba.txt', 'w+') as archivo:
        print(carlos)
        for linea in carlos:
            archivo.write(linea)

def promedio():
    lista = leer('prueba.txt')
    temp = lista[1].split(',')
    temp.pop(0)
    for linea in temp:
        print(linea)

# modificar()
promedio()
# promedio()
