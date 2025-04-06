#Trabajo Práctico 2: Funciones en Python
#Alumno: Matias Carro 

#Ejercicio 1
#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#Funcion que imprime hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

#llamamos a la funcion
imprimir_hola_mundo()

#Ejercicio 2
#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#funcion que saluda al usuario
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#llamamos a la funcion
usuario = str(input("Ingrese su nombre\n"))
saludar_usuario(usuario)

#Ejercicio 3
#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
#dir los datos al usuario y llamar a esta función con los valores in-
#gresados.

#Funcion informacion personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Solicitamos datos al usuario
nombre = str(input("Ingrese su nombre por favor\n"))
apellido = str(input("Ingrese su apellido\n"))
edad = int(input("Ingrese su edad\n"))
residencia = str(input("Ingrese su lugar de residencia\n"))

#llamamos a la funcion informacion_personal
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
