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
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados 

# Importar libreria "math" para usar pi
import math 

#Creamos la funcion para calcular el area
def calcular_area_circulo(radio):
    return math.pi * radio**2

#funcion para calcular perimetro
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Solicitamos ingreso de datos al usuario
radio = float(input("Ingrese el radio del circulo para calcular su area y perimetro\n"))

#llamamos a las funciones, asignamos el return de cada una a una variable
area = round(calcular_area_circulo(radio), 2) #asignamos el return de la funcion a area, ademas redondeamos a 2 decimales
perimetro = round(calcular_perimetro_circulo(radio), 2) #asignamos el return de la funcion a perimetro, ademas redondeamos a 2 decimales

#informamos el resultado
print(f"El area del circulo es: {area} \nEl perimetro del circulo es: {perimetro}")

#Ejercicio 5

#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función.

#Funcion segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

#Solicitamos ingreso al usuario
segundos = float(input("Ingrese un tiempo en segundos para recibir la cantidad de horas a que equivale\n"))

#llamamos a la funcion segundos a horas
horas = round(segundos_a_horas(segundos), 2) #Asignamos el retorno de la funcion a la variable horas, redondeada a 2 decimales

#Devolvemos el resultado al usuario
print(f"{segundos} equivalen a {horas} horas")

#Ejercicio 6

#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun-
#ción.

#Creamos la funcion tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 10): #repetimos el ciclo entre 1 y 9
        multiplicacion = int(numero * i) #multiplicamos el numero por el valor actual de i
        print(f"{numero} X {i} = {multiplicacion}") #imprimimos el resultado
        i += 1 #i suma un valor mas

#Solicitamos ingreso de datos al usuario
numero = int(input("Ingrese un numero para mostar su tabla de multiplicacion\n"))

#llamamos a la funcion tabla de multiplicar y mostramos el resultado
tabla_multiplicar(numero)


#Ejercicio 7
#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultdo 
# de  sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
#sultados de forma clara.

#Creamos la funcion operacion basica
def operaciones_basica(a, b):
    suma = int(a + b) #sumamos
    resta = int(a - b) #restamos
    multiplicacion = int(a * b) #multiplicacion
    if b == 0: #verificamos que el segundo numero no sea 0
        division = str("No es posible dividir por 0") #si es 0 devolvemos un mensaje
    else:
        division = float(a / b) #si no es cero, hacemos la division
    
    return [suma, resta, multiplicacion, division] #se devuelve los resultado en una tupla

#Solicitamos ingreso al usuario
print("Ingrese dos numeros enteros para mostar todos los resultado de las operaciones basicas entre si")
num_1 = int(input("Ingrese el primer numero \n"))
num_2 = int(input("Ingrese el segundo numero \n"))

#llamamos a la funcion operaciones basicas
resultados = operaciones_basica(num_1, num_2) #se almacena la lista devuelta por la funcion en la variable resultado

#Devolvemos los resultados al usuario
print(f"El resultado de la suma entre {num_1} y {num_2}: {resultados[0]}\n") #Devolvemos suma, en la posicion 0
print(f"El resultado de la resta entre {num_1} y {num_2}: {resultados[1]}\n") #Devolvemos resta, en la posicion 1
print(f"El resultado de la multiplicacion entre {num_1} y {num_2}: {resultados[2]}\n") #devolvemos multiplicacion en la posicion 2
print(f"El resultado de la division entre {num_1} y {num_2}: {resultados[3]}\n") #devolvemos division en la posicion 3

#Ejercicio 8
#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
#ción para mostrar el resultado con dos decimales

#creamos la funcion calcular imc
def calcular_imc(peso, altura):
    imc = float(round(peso / (altura ** 2),1))
    if imc < 18.5:
        clasificacion = str("Bajo peso")
    elif 18.5 < imc < 24.9:
        clasificacion = str("Peso normal")
    elif 25.0 < imc < 29.9:
        clasificacion = str("Sobrepeso")
    elif imc > 30:
        clasificacion = str("Obesidad")
    return [imc, clasificacion]

#Solicitamos ingreso al usuario
print("Ingrese su peso y altura para calcular su indice masa corporal")
peso = float(input("Ingrese su peso en kilogramos\n"))
altura = float(input("Ingrese su altura en metros\n"))

#llamamos a la funcion calcular_imc
resultado = calcular_imc(peso, altura)

#informamos el resultado al usuario
print(f"Su indice de masa corporal es {resultado[0]}, su clasificacion es {resultado[1]}")
