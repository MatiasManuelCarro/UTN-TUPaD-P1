#Trabajo practico 3: Estructuras condicionales
#Alumno: Matias Carro 

#Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Solicitamos ingreso de la edad
edad = int(input("Ingrese su edad:\n"))
if edad >= 18: #si la edad es mayor o igual a 18, se muestra el mensaje en pantalla
    print("Es mayor de edad")

#Ejercicio 2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#Solicitamos ingreso de la nota al usuario
nota = int(input("Ingrese su nota final:\n"))
if nota >= 6: #Si la nota es mayor o igual a 6, esta aprobado
    print("Aprobado")
else: #Si la nota es menor a 6, esta desaprobado
    print("Desaprobado")

#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

#Se solicita el ingreso de un numero par al usuario
num = int(input("Ingrese un numero par:\n"))
if num % 2 == 0: #Si el resto de division del numero ingresado por 2 da 0 el numero es par
    print("Ha ingresado un número par")
else: #de lo contrario el numero es impar
    print("Por favor, ingrese un número par")

#Ejercicio 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#Se solicita el ingreso de la edad al usuario
edad = int(input("Ingrese su edad:\n"))
if edad >= 0 and edad <= 12: #primera condicion, hasta 12 años es niño
    print("Eres un Niño/a")
elif edad >= 13 and edad < 18: #Entre 13 y 18 es adolescente
    print("Eres un Adolescente")
elif edad >= 18 and edad < 30: #entre 18 y 30 es adulto joven
    print("Eres un Adulto/a joven")
else: #Si es mayor o igual a 30, es adulto
    print("Eres un Adulto/a")

#Ejercicio 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

#Se informa al usuario los requisitos de la contraseña
print("Ingrese una contraseña, la misma debe tener entre 8 y 14 caracteres")
password = str(input("Ingrese la contraseña:\n")) #se solicita ingreso 

#comparamos la longitud del string con la funcion (len)
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#Del paquete statistics importamos mode, median y mean (Moda, Mediana y Media)
from statistics import mode, median, mean
#importamos el modulo random para generar los numeros
import random
#se generan 50 numeros aleatorios entre 1y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

#Utilizamos la funcion mode para calcular la moda
moda = float(mode(numeros_aleatorios))
#Utilizamos la funcion median para calcular la mediana
mediana = float(median(numeros_aleatorios))
#utilizamos la funcion mean para calular la media
media = float(mean(numeros_aleatorios))

#Realizamos las condiciones para calcular los sesgos e imprimir en pantalla el resultado
if media > mediana and mediana > moda: #condicion sesgo positivo
    print("Hay un sesgo positivo en la lista de numeros")
elif media < mediana and mediana < moda: #condicion sesgo negativo
    print("Hay un sesgo negativo en la lista de numeros")
elif media == mediana and mediana == moda: #condicion sin sesgo
    print("No hay un sesgo en la lista de numeros")

#Ejercicio 7
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

palabra = str(input("Ingrese una frase o palabra:\n")) #se solicita ingreso
#pasamos a minusculas a palabra o frase
palabra_minusculas = str(palabra.lower())
#Creamos una lista con todas las vocales, para poder comparar mas facilmente
vocales = ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú"]

#realizamos la condicion donde se compara la ultima posicion del str ingresado con la lista de vocales
if palabra_minusculas[-1] in vocales:
    print(f"{palabra}!") #si termina en una vocal, se agrega ! al final
else:
    print(palabra) #si no, termina en una consonante, por lo tanto no se agrega nada 


#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nombre:\n")) #se solicita ingreso
#Se informa al usuario el funcionamiento del programa
print("Seleccion una opcion: ")
print("Ingrese 1 si quiere su nombre en mayúsculas")
print("Ingrese 2 si quiere su nombre en minúsculas.")
print("Ingrese 3 si quiere su nombre con la primera letra mayúscula")
num = int(input("Ingrese 1, 2 o 3: \n")) #Se solicita que ingrese la opcion

if num == 1:
    print(nombre.upper()) #la funcion upper convierter el string a mayusculas
elif num == 2:
    print(nombre.lower()) #la funcion lower convierte el string a minusculas
elif num == 3:
    print(nombre.title()) #la funcion title cambia la primer letra de cada palabra del string a mayusculas

#Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala

#solicitamos al usuario el ingreso de la magnitud
escala = float(input("Ingrese la magnitud del terremoto para clasificarlo:\n"))

#Condicional para la escala de ritcher
if escala < 3:
    print("Muy leve (imperceptible).")
elif escala >= 3 and escala < 4:
    print("Leve (ligeramente perceptible).")
elif escala >= 4 and escala < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif escala >= 5 and escala < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif escala >= 6 and escala < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif escala >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#
