#Trabajo practico 1: Secuenciales
#Alumno: Matias Carro 

#Ejercicio 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#Ejercicio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = str(input("Ingrese su nombre:\n"))
print(f"Hola {nombre}!")

#Ejercicio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = str(input("Ingrese su nombre:\n"))
edad = str(input("Ingrese su edad:\n"))
residencia = str(input("Ingrese su lugar de residencia:\n"))
print(f"Soy {nombre} tengo {edad} Años y vivo en {residencia}")


#Ejercicio4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio de un circulo para calcular su area y perimetro:\n"))
area = float(3.14 * radio**2)
perimetro = float(2*radio*3.14)
perimetro = round(perimetro, 2)
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese el tiempo en segundos para calcular a cuantas horas equivale:\n"))
horas = float(segundos / 3600)
horas = round(horas, 2)
print(f" {segundos} Segundos equivale a {horas} horas")

#Ejercicio 6
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un numero para mostar su tabla de multiplicacion\n"))
for i in range(10):
    multiplicacion = int(numero * i)
    print(f"{numero} X {i} = {multiplicacion}")
    i = i + 1

#Ejercicio 7

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingrese dos numeros enteros distintos de 0")
#validamos el ingreso de los datos, verificando que no sea 0
#creamos la funcion de validacion de datos
def validacion_datos():
    while True: #Repite la validacion hasta que se ingrese correctamente y salga del if
        num = int(input("Ingrese un numero: \n"))
        if num != 0:
            return num
        else: #Si el numero es 0, volvemos a solicitar el ingreso hasta que sea correcto.
            print("Ingrese el numero nuevamente, recuerde que debe ser entero y distinto de 0")

#llamamos a la funcion de verificacion, para realizar el ingreso de los dos numeros
num_1 = validacion_datos()
num_2 = validacion_datos()

#creamos la funcion suma
def sumar_num(x,y):
    suma = int(x + y)
    print(f"La suma entre {x} Y {y} es {suma}")

#creamos la funcion resta
def restar_num(x,y):
    resta = int(x - y)
    print(f"La resta entre {x} Y {y} es {resta}")

#creamos la funcion division
def dividir_num(x,y):
    division = float(x / y)
    if division.is_integer(): #verificamos si el resultado no tiene decimales, lo pasamos a entero, para poder expresarlo sin .00 al final
        division = int(division)
        print(f"La division entre {x} Y {y} es {division}")
    else:
        division = round(division, 4) #Si tiene decimales, limitamos la cantidad a 4 
        print(f"La division entre {x} Y {y} es {division}")

#creamos la funcion multiplicacion
def multiplicar_num(x,y):
    multiplicacion = int(x * y)
    print(f"La mutiplicacion entre {x} Y {y} es {multiplicacion}")

#llamamos a la funcion suma
sumar_num(num_1, num_2)

#verificamos si el numero es igual para no repetir la operacion de dividir
if num_1 == num_2:
    dividir_num(num_1, num_2)
else:
    #llamamos a la funcion division para la primer division
    dividir_num(num_1, num_2)
    #llamamos a la funcion division para la segunda division
    dividir_num(num_2, num_1)

#llamamos a la funcion multiplicacion
multiplicar_num(num_1, num_2)

#verificamos si el numero es igual para no repetir la operacion de restar
if num_1 == num_2:
    restar_num(num_1, num_2)
else:
    #llamamos a la funcion resta para la primer resta
    restar_num(num_1, num_2)
    #llamamos a la funcion resta para la segunda resta
    restar_num(num_2, num_1)

#Ejercicio 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

print("Ingrese su altura y peso para calcular su indice masa corporal")
altura = int(input("Ingrese su altura en centimetros\n")) #Pedimos la altura en centimetros
peso = float(input("Ingrese su peso en kilogramos\n"))
altura = float(altura / 100) #pasamos la altura a metros para el calculo
imc = float(round(peso / (altura ** 2),1)) #Calculamos el imc
print(f"Su indice de masa corporal es {imc}")

#Ejercio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia

celsius = float(input("Ingrese una temperatura en celsius para convertirla a farenheit: \n"))
farenheit = float(9/5 * celsius) + 32
print (f"{celsius} celsius es igual a {farenheit} grados farenheit")

#Ejercicio 10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Ingrese 3 numeros para calcular su promedio")
num_1 = int(input("Ingrese el primer numero\n"))
num_2 = int(input("Ingrese el segundo numero\n"))
num_3 = int(input("Ingrese el tercer numero\n"))

promedio = float((num_1 + num_2 + num_3) / 3) #Se calcula el promedio
promedio = round(promedio, 2)
print(f"El promedio entre los numeros {num_1}, {num_2} y {num_3} es {promedio}")
