from math import e
import random

def create_list():
    entry_list = []
    while True:
        temp_entry = [0,0,1]
        temp_entry[0] = input("Escribe título de la tarjeta ")
        temp_entry[1] = input("Escribe la respuesta, definición o explicacion de la tarjeta ")
        entry_list.append(temp_entry)

        iterate = input("Si deseas añadir una nueva tarjeta escribe 1 o presiona enter para continuar ")
        if  iterate == "1":
            continue
        break
    return(entry_list)

def review(list):
    entry_num = len(list)
    study_iterations = int(input("Escribe cuántas tarjetas quieres que aparezcan "))
    for i in range(study_iterations):
        rand_entry = random.randint(0, entry_num-1)
        print(entries[rand_entry][0])
        input()
        print(entries[rand_entry][1], "\n")
        entries[rand_entry][2]=input("Califica del 1 al 5 que tanto recuerdas esta tarjera \n 1 = nada \n 5 = perfectamente \n")


print("Bienvenido al programa de estudio Anki \n Crea por lo menos una entrada de estudio para continuar")

entries = create_list()
review(entries)

input("Gracias por probar la primera versión del programa")



