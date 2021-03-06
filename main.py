import os
from functions import get_files, test_walk, populate, fix_numbers_filenames

def menu():
    os.system('cls')
    print('Selecciona una opcion:')
    print('\t1 - Obtener nombres de archivos de un direcctorio')
    print('\t2 - Ver directorios de un Directorio')
    print('\t3 - Populate')
    print('\t4 - Eliminar primeros numeros de los archivos en directorio')

while True:
    menu()

    opcion = input('Seleccionar >>')

    if opcion == '1':
        dir = input('Ingrese la ruta del directorio: ')
        files = get_files(dir)
        for file in files:
            print(file)
    if opcion == '2':
        dir = input('Ingrese la ruta del directorio: ')
        test_walk(dir)
    if opcion == '3':
        dir = input('Ingrese ruta ("." para ruta actual)>> ')
        type = input('Ingrese tipo de archivo a crear>> ')
        cuantity = input('Ingrese cantidad de Archivos a crear >>')
        populate(dir, type, cuantity)
    if opcion == '4':
        dir = input('Ingrese directorio>>')
        fix_numbers_filenames(dir)