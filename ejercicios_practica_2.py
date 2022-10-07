# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv
from fileinput import close
from webbrowser import get


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    csvfile = open(archivo, 'r') # r es modo lectura

    data = list(csv.DictReader(csvfile))

    cantidad = range(len(data))
    suma_tornillos = 0

    for v in cantidad:
        suma_tornillos += int(data[v].get('tornillos'))
    
    print('La suma de tornilloses',suma_tornillos)

    csvfile.close()


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    csvfile = open(archivo, 'r') # r es modo lectura

    data = list(csv.DictReader(csvfile))     
    contar_ambiente = 0
    cantidad = range(len(data))

    for v in cantidad:
        ambiente = data[v].get('ambientes')
        if ambiente =='3' or ambiente =='2':
            contar_ambiente = 1 + contar_ambiente

    print("La cantidad de ambiestes con 2 y 3 domritorios es: ", contar_ambiente)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
