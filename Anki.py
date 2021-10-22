"""
José Pablo Martínez Valdivia
A01275676

Anki
Programa de estudio por repetición espaciada.
Este programa te permiete realizar tarjetas de estudio
y calificarlas según tu nivel de retención, 
la calificación que les asignes determinará la 
frecuencia con la que estas aparezcan.
"""
#bibliotecas
import random
"""
librería para generar números aleatorios 
https://docs.python.org/3/library/random.html
"""
import csv
"""
Referencia de lectura y escritura de archivos csv
https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
"""


"""
==================== funciones de lectura y escritura csv ====================
"""
def read_file():
    """
    (uso de funciones, listas anidadas, archivos de texto)
    recibe: nada
    lee el archivo y lo combierte en una lista
    devuelve: lista con los datos del archivo
    """
    #with nos permite manejar el archivo dentro del bloque y despues cerrarlo
    with open('Entries.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def write_file(entries):
    """
    (uso de funciones, listas, listas anidadas, archivos de texto)
    recibe: entires lista
    sobrescribe el archivo y añade las nuevas entradas
    devuelve: nada
    """
    data = read_file()
    with open('Entries.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        data.extend(entries)
        writer.writerows(data)

def update_file(entries):
    """
    (uso de funciones, listas, listas anidadas, archivos de texto)
    recibe: entires lista
    sobrescribe el archivo reemplazando los valores de calificación
    devuelve: nada
    """
    with open('Entries.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(entries)

"""
============================ funciones principales ============================
"""
def create_list():
    """
    (uso de listas, listas anidadas, condicionales, funciones)
    recibe: nada
    ciclo que crea listas con datos ingresados por el usario y
    actualiza el archivo
    devuelve: nada
    """
    entry_list = []
    while True:                                                   
        temp_entry = [0, 0, 1, 0]
        temp_entry[0] = input("Escribe título de la tarjeta ")
        temp_entry[1] = input("Escribe la respuesta, definición o"
            " explicacion de la tarjeta ")
        entry_list.append(temp_entry)

        iterate = input("Si deseas añadir una nueva tarjeta escribe" 
            " 1 o presiona enter para continuar ")
        if iterate == "1":
            continue
        break
    write_file(entry_list)

def review(study_iterations):
    """
    (uso de funciones, ciclos, listas, listas anidadas)
    recibe: study_iterations entero
    pide un número de tarjetas a imprimir
    despliega el título y después la definición 
    pide una calificación para la tarjeta
    sobrescribe la calificación y la manda a update_file()
    devuelve: nada
    """
    
    message = ("""\nCalifica del 1 al 5 que tanto recuerdas esta tarjera
        1 = nada
        5 = perfectamente\n""")
    
    for i in range(study_iterations):
        matrix = read_file()
        lists, new_matrix = choose_entry(matrix)
        entry_num = len(lists)
        rand_entry = random.randint(0, entry_num-1)

        print("|| ", lists[rand_entry][0])
        input("\nPresiona enter para girar la tarjerta \n")
        print("|| " + lists[rand_entry][1])
        print(message)

        rating = numeric_handler(0, 5, message)

        lists[rand_entry][2]= rating
        lists[rand_entry][3] = int(lists[rand_entry][3]) + 1
        print("Has estudiado esta tarjeta {} veces\n".format(
            lists[rand_entry][3]))

        new_matrix.extend(lists)
        update_file(new_matrix)

def choose_entry(matrix):
    """
    (uso de funciones, operadores, ciclos, ciclos anidados, condicionales)
    recibe: matrix lista anidada
    calcula la probabilidad de elegir tarjetas según su calificación
    devuelve: una lista con las tarjetas del ranking elegido
        lista con las tarjetas sobrantes
    """
    
    probability = random.randint(1, 100)

    if probability <= 30:
        target_rating = 1
    elif probability > 30 and probability <= 55:
        target_rating = 2
    elif probability > 55 and probability <= 75:
        target_rating = 3
    elif probability > 75 and probability <= 90:
        target_rating = 4
    elif probability > 90 and probability <= 100:
        target_rating = 5

    while True:
        selected_list = []
        residue_list = []
        for lists in matrix:
            if int(lists[2]) == target_rating:
                selected_list.append(lists)
            else:
                residue_list.append(lists)
        if selected_list:
            break
        if target_rating < 5:
            target_rating += 1
        else:
            target_rating = 1
    return selected_list, residue_list

"""
====================== funcion para forzar el formato =======================
"""

def numeric_handler(min, max, message):
    """
    (uso de funciones, ciclos, condicionales)
    recibe: min valor mínimo, max valor máximo, message mensaje de error
    bucle que solo se rompe si el valor ingresado 
    es numérico y está en el rango de valores solicitados
    imprime el mensaje de error para recordar al usuario que hacer
    devuelve: answer valor numérico
    """
    while True:
        answer = input()
        if not(answer.isnumeric()):
            print("Ingresa un valor numérico" + message)
            continue
        answer = int(answer)
        if (answer > max or answer < min):
            print("Ingresa un valor válido" + message)
            continue
        return answer

"""
============================= Programa principal =============================
"""

print("Bienvenido al programa de estudio Anki, elige una opción del menú")
menu = """\n    Crear una nueva entrada.................1 
    Repasar la unidad.......................2 
    Imprimir todas las entradas.............3
    Salir del programa......................4
    """

while True:
    print(menu)

    answer = numeric_handler(1, 4, menu)
    if answer == 1:
        create_list()

    elif answer == 2:
        print("Escribe cuántas tarjetas quieres que aparezcan. (Max: 10)")
        message = "\nIngresa un número mayor a cero y menor a 40"
        iterations = numeric_handler(1, 10, message)
        print("\n")
        review(iterations)

    elif answer == 3:
        entry_list = read_file()
        index = 1
        print("\n")
        for lists in entry_list:
            text_index = str(index)
            print(text_index, ".- ", lists[0], ": ", lists[1], 
                "| Calificación: ", lists[2], "| Veces repasada: ", lists[3])
            index += 1
        input("\npulsa enter para continuar")
    else:
        break
print("Gracias por usar el programa")



