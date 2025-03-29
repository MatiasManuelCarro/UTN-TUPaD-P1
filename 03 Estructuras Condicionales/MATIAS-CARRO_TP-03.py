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




