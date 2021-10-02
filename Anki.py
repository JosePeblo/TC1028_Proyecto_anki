"""
Programa de estudio por repetición espaciada.
Este programa te permiete realizar tarjetas de estudio
y calificarlas según tu nivel de retención, 
la calificación que les asignes determinará la 
frecuencia con la que estas aparezcan.
"""
#bibliotecas
from math import e
import random
import csv

"""
==================== funciones de lectura y escritura csv ====================
"""
def read_file():
    """
    lee el archivo
    devuelve: lista con los datos del archivo
    """
    with open('Entries.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def write_file(entries):
    """
    sobrescribe el archivo y añade las nuevas entradas
    recibe: entries lista de listas
    """
    data = read_file()
    with open('Entries.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        data.extend(entries)
        writer.writerows(data)

def update_file(entries):
    """
    sobrescribe el archivo reemplazando los valores de calificación
    recibe: entries lista de listas
    """
    with open('Entries.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(entries)

"""
============================ funciones principales ============================
"""
def create_list():
    """
    ciclo que crea listas con datos ingresados por el usario
    devuelve la lista generada a write_file()
    """
    entry_list = []
    while True:                                                   
        temp_entry = [0,0,1]                                        #Listas
        temp_entry[0] = input("Escribe título de la tarjeta ")
        temp_entry[1] = input("Escribe la respuesta, definición o"
            "explicacion de la tarjeta ")
        entry_list.append(temp_entry)

        iterate = input("Si deseas añadir una nueva tarjeta escribe" 
            " 1 o presiona enter para continuar ")
        if iterate == "1":
            continue
        break
    write_file(entry_list)

def review():
    """
    pide un número de tarjetas a imprimir
    despliega el título y después la definición 
    sobrescribe la calificación y la manda a update_file()
    """
    lists = read_file()
    entry_num = len(lists)
    study_iterations = int(input("Escribe cuántas tarjetas quieres" 
        " que aparezcan "))
    for i in range(study_iterations):                            
        rand_entry = random.randint(0, entry_num-1)
        print(lists[rand_entry][0])                               #Listas
        input()
        print(lists[rand_entry][1], "\n")
        lists[rand_entry][2]= rating_exception()
    update_file(lists)

"""
====================== funciones para forzar el formato ======================
"""
def rating_exception():
    """
    bucle que solo se rompe si el valor ingresado 
    es numérico y está en el rango de valores solicitados
    devuelve: rating valor numérico
    """
    print("Califica del 1 al 5 que tanto recuerdas esta tarjera \n" 
        " 1 = nada \n 5 = perfectamente \n")
    while True:
        rating = input()
        if not(rating.isnumeric()):
            print("Ingresa un valor numérico")
            continue
        rating = int(rating)
        if (rating > 5 or rating < 1):
            print("Ingresa un número del 1 al 5")
            continue
        return rating

def menu_exception():
    """
    bucle que solo se rompe si el valor ingresado 
    es numérico y está en el rango de valores solicitados
    devuelve: answer valor numérico
    """
    while True:
        answer = input()
        if not(answer.isnumeric()):
            print("Ingresa un valor numérico")
            continue
        answer = int(answer)
        if (answer > 4 or answer < 1):
            print("Ingresa un valor válido del menú \n"
            " Crear una nueva entrada.................1 \n" 
            " Repasar la unidad.......................2 \n" 
            " Imprimir todas las entradas.............3 \n"
            " Salir del programa......................4")
            continue
        return answer

"""

"""
print("Bienvenido al programa de estudio Anki, elige una opción del menú \n"
" Crear una nueva entrada.................1 \n" 
" Repasar la unidad.......................2 \n" 
" Imprimir todas las entradas.............3 \n"
" Salir del programa......................4")
answer = menu_exception()
if answer == 1:
    create_list()
elif answer == 2:
    review()
elif answer == 3:
    print(read_file())

input("Lol")



