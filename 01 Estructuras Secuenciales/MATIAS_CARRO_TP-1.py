#Trabajo practico 1: Secuenciales
#Alumno: Matias Carro 


#Ejercicio 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("EJERCICIO 1\n")

print("Hola Mundo!")

#Ejercicio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
print("-------------")
print("EJERCICIO 2\n")

nombre = str(input("Ingrese su nombre:\n"))
print(f"Hola {nombre}!")

#Ejercicio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
print("-------------")
print("EJERCICIO 3\n")

nombre = str(input("Ingrese su nombre:\n"))
apellido = str(input("Ingrese su apellido\n"))
edad = str(input("Ingrese su edad:\n"))
residencia = str(input("Ingrese su lugar de residencia:\n"))
print(f"Soy {nombre} {apellido} tengo {edad} Años y vivo en {residencia}")


#Ejercicio4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
print("-------------")
print("EJERCICIO 4\n")

radio = float(input("Ingrese el radio de un circulo para calcular su area y perimetro:\n"))
area = float(3.14 * radio**2)
perimetro = float(2*radio*3.14)
perimetro = round(perimetro, 2)
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
print("-------------")
print("EJERCICIO 5\n")

segundos = int(input("Ingrese el tiempo en segundos para calcular a cuantas horas equivale:\n"))
horas = float(segundos / 3600)
horas = round(horas, 2)
print(f" {segundos} Segundos equivale a {horas} horas")

#Ejercicio 6
#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
print("-------------")
print("EJERCICIO 6\n")

numero = int(input("Ingrese un numero para mostar su tabla de multiplicacion\n"))
resultado = int(numero * 1)
print(f"{numero} x 1 = {resultado}")
resultado = int(numero * 2)
print(f"{numero} x 2 = {resultado}")
resultado = int(numero * 3)
print(f"{numero} x 3 = {resultado}")
resultado = int(numero * 4)
print(f"{numero} x 4 = {resultado}")
resultado = int(numero * 5)
print(f"{numero} x 5 = {resultado}")
resultado = int(numero * 6)
print(f"{numero} x 6 = {resultado}")
resultado = int(numero * 7)
print(f"{numero} x 7 = {resultado}")
resultado = int(numero * 8)
print(f"{numero} x 8 = {resultado}")
resultado = int(numero * 9)
print(f"{numero} x 9 = {resultado}")

#La forma mas simple de hacerlo seria con un ciclo for:
#for i in range(10):
#    multiplicacion = int(numero * i)
#    print(f"{numero} X {i} = {multiplicacion}")
#    i = i + 1

#Ejercicio 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("-------------")
print("EJERCICIO 7\n")

print("Ingrese dos numeros enteros distintos de 0")
num1 = int(input("Ingrese un numero: \n"))
num2 = int(input("Ingrese un numero: \n"))

#Sumamos los numeros
suma = num1 + num2
print (f"la suma entre {num1} y {num2} es: {suma}")

#dividimos los numeros
if num2 == 0:
    print(f"No es posible dividir {num1} por 0, No se puede dividir por 0")
else:
    division = float(num1 / num2)
    division = round(division, 2)
    print(f"La division entre {num1} Y {num2} es {division}")

if num1 == 0:
    print(f"No es posible dividir {num2} por 0, No se puede dividir por 0")
else:
    division = float(num2 / num1)
    division = round(division, 2)
    print(f"La division entre {num2} Y {num1} es {division}")

#restamos los numeros
resta = num1 - num2
print(f"La resta entre {num1} Y {num2} es {resta}")
resta = num2 - num1
print(f"La resta entre {num2} Y {num1} es {resta}")

#multiplicamos los numeros
multiplicacion = int(num1 * num2)
print(f"La mutiplicacion entre {num1} Y {num2} es {multiplicacion}")

#Ejercicio 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.
print("-------------")
print("EJERCICIO 8\n")

print("Ingrese su altura y peso para calcular su indice masa corporal")
altura = int(input("Ingrese su altura en centimetros\n")) #Pedimos la altura en centimetros
peso = float(input("Ingrese su peso en kilogramos\n"))
altura = float(altura / 100) #pasamos la altura a metros para el calculo
imc = float(round(peso / (altura ** 2),1)) #Calculamos el imc
print(f"Su indice de masa corporal es {imc}")

#Ejercio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia
print("-------------")
print("EJERCICIO 9\n")

celsius = float(input("Ingrese una temperatura en celsius para convertirla a farenheit: \n"))
farenheit = float(9/5 * celsius) + 32
print (f"{celsius} celsius es igual a {farenheit} grados farenheit")

#Ejercicio 10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
print("-------------")
print("EJERCICIO 10\n")

print("Ingrese 3 numeros para calcular su promedio")
num_1 = int(input("Ingrese el primer numero\n"))
num_2 = int(input("Ingrese el segundo numero\n"))
num_3 = int(input("Ingrese el tercer numero\n"))

promedio = float((num_1 + num_2 + num_3) / 3) #Se calcula el promedio
promedio = round(promedio, 2)
print(f"El promedio entre los numeros {num_1}, {num_2} y {num_3} es {promedio}")
