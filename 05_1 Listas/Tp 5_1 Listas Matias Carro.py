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

print(f"\nEjercicio 2")
frutas = ["Manzana", "Banana", "Naranja", "Uva", "Pera"]
print(f"Lista: {frutas}")

#Para mostrar el Penultimo elementos de la lista, utilizamos la posicion -2
print(frutas[-2])


#Ejercicio 3

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por

print(f"\nEjercicio 3")

lista_ejercicio3 = []

for i in range(3):
    palabra = input(str("Ingrese una palabra para agregar a la lista\n"))
    lista_ejercicio3.append(palabra)

print(lista_ejercicio3)

#Ejercicio 4

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!

print(f"\nEjercicio 4")

animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista inicial:\n {animales}")

animales[1] = "loro" #reemplazamos el indice 1 de la lista, que es la segunda posicion
animales[-1] = "oso" #reemplazamos el valor -1 la lista, que es la ultima posicion

print(f"Lista final:\n {animales}")

#Ejercicio 5
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

print(f"\nEjercicio 5")

numeros =[8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Respuesta:
print("El programa remueve el valor maximo de la lista, utilizando la funcio max para encontrar el valor maximo \n")
print("Y utiliza la funcion .remove para removerlo. Devuelve la lista sin el numero 22")

#Ejercicio 6

# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

print(f"\nEjercicio 6")

lista_ejercicio6 = []

for i in range(10, 31, 5):
    lista_ejercicio6.append(i)

print(lista_ejercicio6)
print(f"Primeros dos numeros de la lista: {lista_ejercicio6[:2]}") #[:2] muestra desde el indice 0 al 1

#Ejercicio 7

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.

print(f"\nEjercicio 7")

autos = ["sedan", "polo", "suran", "gol"]
print(autos)

autos[1] = "fiesta"
autos[2] = "cronos"
print("Lista con los valores centrales reemplazados:")
print(autos)

#Ejercicio 8

#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla

print(f"\nEjercicio 8")

dobles = []

#El ciclo for va a ir de 5 a 10 a 15
for i in range(5, 16, 5):
    dobles.append(i*2) #agregamos el doble del valor de i

print(dobles)

#Ejercicio 9

#Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:

print(f"\nEjercicio 9")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print("Lista inicial:")
print(f"{compras}\n")
#a-  Agregar "jugo" a la lista del tercer cliente usando append
print("Agregar \"jugo\" a la lista del tercer cliente")
compras[2].append("jugo") 
print(f"{compras}\n")
#b Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
print("Reemplazar \"fideos\" por \"tallarines\" en la lista del segundo cliente.")
compras[1][1] = "tallarines"
print(f"{compras}\n")
#c- Eliminar "pan" de la lista del primer cliente.
print("Eliminar \"pan\" de la lista del primer cliente.")
del compras[0][0]
print(f"{compras}\n")

#d- Imprimir la lista resultante por pantalla
print("Lista Final:\n")
print(f"{compras}\n")

#Ejercicio 10

# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

#Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

print(f"\nEjercicio 10")

lista_anidada = [[], [], [], []]
lista_anidada[0].append(15)
lista_anidada[1].append(True)
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada[3].append(False)


print(lista_anidada)