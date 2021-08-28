import random

print("Bienvenido al programa de estudio Anki \n Crea por lo menos una entrada de estudio para continuar")
no_de_entradas = 1
lista_de_entradas = [[],[]]
for i in range(no_de_entradas):
    lugar = i-1
    lista_de_entradas[[lugar],[0]] = input("Escribe título de la tarjeta ")
    lista_de_entradas[[lugar],[1]] = input("Escribe la respuesta, definición o explicacion de la tarjeta ")
    iterar = int(input("Si deseas añadir una nueva tarjeta escribe 1 o presiona enter para continuar "))
    if  iterar == 1:
        no_de_entradas = no_de_entradas+1

iteraciones_de_estudio = int(input("Escribe cuántas targetas quieres que aparezcan "))

for i in range(iteraciones_de_estudio):
    entrada_aleatoria = random.randint(0, no_de_entradas-1)
    print(lista_de_entradas[[entrada_aleatoria],[0]])
    input("Enter para continuar")
    print(lista_de_entradas[[entrada_aleatoria],[1]])

input("Gracias por probar la primera versión del programa")



