from math import e
import random

def create_list():
    entry_list = []
    while True:
        temp_entry = [0,0,1]
        temp_entry[0] = input("Escribe título de la tarjeta ")
        temp_entry[1] = input("Escribe la respuesta, definición o \
            explicacion de la tarjeta ")
        entry_list.append(temp_entry)

        iterate = input("Si deseas añadir una nueva tarjeta escribe \
            1 o presiona enter para continuar ")
        if  iterate == "1":
            continue
        break
    return(entry_list)

def review(list):
    entry_num = len(list)
    study_iterations = int(input("Escribe cuántas tarjetas quieres \
        que aparezcan "))
    for i in range(study_iterations):
        rand_entry = random.randint(0, entry_num-1)
        print(entries[rand_entry][0])
        input()
        print(entries[rand_entry][1], "\n")
        entries[rand_entry][2]= rating_exception()

def rating_exception():
    print("Califica del 1 al 5 que tanto recuerdas esta tarjera \n \
        1 = nada \n 5 = perfectamente \n")
    while True:
        rating = input()
        if not(rating.isnumeric()):
            print("Ingresa un valor numérico")
            continue
        rating = int(rating)
        print("hola")
        if (rating > 5 or rating < 1):
            print("Ingresa un número del 1 al 5")
            continue
        return rating

def menu():
    print("Bienvenido al programa de estudio Anki, elige una \
        opción del menú \n Crear una nueva entrada = 1 \n \
             Repasar la unidad = 2 \n Imprimir todas las entradas = 3 \
                Salir del programa = 4")
    answer = menu_exception()
    if answer == 1:
        create_list()
    elif answer == 2:
        review()
    elif answer == 3:
        print()
    else:
        return


def menu_exception():
    while True:
        answer = input()
        if not(answer.isnumeric()):
            print("Ingresa un valor numérico")
            continue
        answer = int(answer)
        if (answer > 4 or answer < 1):
            print("Un valor válido del menú \n \
                Crear una nueva entrada = 1 \n \
                Repasar la unidad = 2 \n \
                Imprimir todas las entradas = 3 \
                Salir del programa = 4")
            continue
        return answer

menu()

#entries = create_list()
#review(entries)

input("Lol")



