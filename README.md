# TC1028_Proyecto_anki
Programa de aprendizaje de conceptos basado en el método anki
# Método Anki

### Contexto
El método "Anki" está basado en la memorización por repetición espaciada, básicamente es un sistema con el que se pueden memorizar conceptos, utilizando un sistema de ranqeo con el que los conceptos se repetirán con mayor frecuencia cuando la calificación de memorización sea menor, esta es una manera más eficiente de recordar: nombres, definiciones, descripciones, etc. Esto puede ser útil para un estudiante universitario para poder facilitar sus estudios de conceptos difíciles y mejorar su rendimiento en exámenes teóricos, como dato curioso este sistema es muy utilizado entre estudiantes de medicina y de lenguas como el chino y japonés.

### Planteamiento
En este proyecto planeo crear un programa con dos funciones: la de ingresar conceptos y definiciones para crear nuevas cartas de estudio y la de repasar las cartas. Esto viene junto a un sistema de ranqeo, el cual configurara la frecuencia con la que el sistema te enseñará dicha tarjeta de estudio.

### Pseudocódigo

E0(elegir fución de estudio o de crear tarjeta)
si eliges crear tarjeta

  concepto = preguntar concepto
  definición = preguntar definición
  escribir en archivo de texto el concepto y la definición
  
pero si eliges estudio
  
  mientras el usuario quiera repetir
    calcular aleatroreamente una entrada de estudio
    imprimir el concepto y esperar a que el usuario de cualquier input para continuar
    imprimir definición
    pedir ranqueo del 1 al 5
    modificar la probabilidad de muestra de la tarjeta dependiendo de la calificación
    preguntar si desea repetir o cerrar el programa 
