#Ejercicio 1

#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
print("Ejercicio 1")
lista_numero = []

for i in range(1, 101):
    if (i % 4) == 0:
        lista_numero.append(i)

print(lista_numero)

#Ejercicio 2

#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

print("Ejercicio 2")
frutas = ["Manzana", "Banana", "Naranja", "Uva", "Pera"]

#Utilizamosla funcion len para contar la cantidad de items en la lista 
# #(se sabe que es 5 pero con len se aplica a cualquier lista ingresada)
#Con el valor de len(frutas) le restamos -2 al indice de la lista. esto seria el anteultimo, ya que la lista va de 0 a 4 y el valor de len(frutas) es 5

print(frutas[len(frutas)-2])

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por

print("Ejercicio 3")

lista_ejercicio3 = []

for i in range(3):
    palabra = input(str("Ingrese una palabra para agregar a la lista\n"))
    lista_ejercicio3.append(palabra)

print(lista_ejercicio3)

#Ejercicio 4

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!

print("Ejercicio 4")

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro" #reemplazamos el indice 1 de la lista, que es la segunda posicion
animales[len(animales)-1] = "oso" #reemplazamos el valor -1 del largo total de la lista, que es la ultima posicion

print(animales)

#Ejercicio 5
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

print("Ejercicio 5")

numeros =[8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Respuesta:
# El programa remueve el valor maximo de la lista, utilizando la funcio max para encontrar el valor maximo
#Y utiliza la funcion .remove para removerlo. Devuelve la lista sin el numero 22

#TECNICATURA UNIVERSITARIA

#Ejercicio 6

# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

print("Ejercicio 6")

lista_ejercicio6 = []

for i in range(10, 31, 5):
    lista_ejercicio6.append(i)

print(lista_ejercicio6)



