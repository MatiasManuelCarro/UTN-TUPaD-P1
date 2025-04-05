#Trabajo practico 4: Estructuras Repetitivas
#Alumno: Matias Carro 


#Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

i = int(0)
for i in range(101): #se utiliza in range 101 para que recorra desde el 0 hasta el 100 inclusive
    print(i)
    i += 1

#Ejercicio 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un numero entero\n"))
#inicializacion las varariables
i = int(num)
digitos = int(0)
#comienza la iteracion y se repite mientras que i sea > 0
while i > 0:
    digitos += 1
    i = int(i/10) #se divide i por 10 y se quita los decimales pasando ese resultado a integer

print(f"El numero {num}, tiene {digitos} digitos")

#nota, en python podemos contar la cantidad de digitos simplemente utilizando la funcion len de strings:
#digitos = len(str(num))


#ejercicio 3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

print("Ingrese dos numeros enteros para mostar todos los valores comprendidos entre esos dos numeros")
#Ingreso de datos
while True: #Este loop corre indefinidamente hasta que se ingrese correctamente los numeros
    num_1 = int(input("Ingrese el primer numero \n"))
    num_2 = int(input("Ingrese el segundo numero \n"))
    if num_1 > num_2:#Se verifica que se haya ingresado correctamente
        print("El primer numero debe ser menor que el segundo, ingrese nuevamente")
    else:
        break #si se ingresa correctamente se sale del loop

print(f"los numeros entre {num_1} y {num_2} son:\n")
i = int(num_1) #se inicializa i como el primer numero
for i in range(num_1+1, num_2): #el ciclo for corre desde el primer numero+1 hasta el segundo numero
    print(i)
    i += i


#Ejercicio 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

print("Ingrese numero enteros, el programa los sumara. Para finalizar, ingrese un 0")
num = int(input("Ingrese un numero entero\n"))
while num != 0:
    sum = int(sum + num)
    num = int(input("Ingrese otro numero entero\n"))

print(f"La suma de los numeros es {sum}")


#Ejercicio 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número
from random import randrange #de la funcion random se utiliza randrange
random = randrange(10) #se crea un numero random entre 0 y 9

#ingreso de datos
print("Adivine cual es el numero entero aleatorio entre 0 y 9")
num = int(input("Ingrese un numero entero\n"))
#Inicializacion de i, ya se cuenta el primer intento por eso i = 1
i = int(1)

while num != random: #mientras que el numero sea distitno de random, corre el loop
    num = int(input("No adivinaste el numero, intenta nuevamente:\n"))
    i += 1 #contamos los intentos

#Se informa al usuario
print(f"Avidinaste! numero de intentos: {i}")


#Ejercicio 6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

i = int(100) #inciamos la variable i como 100
#Creamos el loop for que va a ir desde 98 hasta 0, decreciendo en -2 por cada paso
for i in range(98, 0, -2):
    print(i) #imprimimos 


#Ejercicio 7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

print("Ingrese un numero para sumar todos los numeros entre el 0 y el ingresado")
num = int(input("Ingrese un numero entero\n")) #pedido de ingreso al usuario
#Se inicializan las variables
i = int(0)
suma = int(0)

#El loop for suma todos los numeros entre 0 y num
for i in range(num):
    i += 1
    suma += i

print(f"La suma de los numeros entre 0 y {num} es: {suma}")


#Ejercicio 8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio)

#Se inician las variables contadores
pares = int(0)
impares = int(0)
negativos = int(0)
positivos = int(0)

#Variable ingreso, comentar la que no corresponda, se deja en 10 para poder testear rapidamente
#ingreso = int(100)
ingreso = int(10)

#se pide ingreso de datos al usuario
print(f"Ingrese {ingreso} numeros, al final se le informara cuantos son pares, impares, positivos y negativos")
for i in range(ingreso): #El loop se repite hasta el valor de la variable ingreso
    num = int(input("Ingrese un numero entero\n"))
    i += 1
    if num % 2 == 0: #Verificamos si el numero es pa
        pares += 1
    else: #Si no, el numero es impar y se cuenta
        impares +=1
    if num > 0: #Verificamos si el numero es positivo
        positivos += 1
    else: #si no, se cuenta como negativo
        negativos += 1


print(f"Se ingresaron un total de {pares} numeros pares")
print(f"Se ingresaron un total de {impares} numeros impares")
print(f"Se ingresaron un total de {positivos} numeros positivos")
print(f"Se ingresaron un total de {negativos} numeros negativos")


#Ejercicio9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#iniciamos las variables
i = int(0)
sum = int(0)
#Variable ingreso, comentar la que no corresponda, se deja en 10 para poder testear rapidamente
#ingreso = int(100)
ingreso = int(10)

#se pide ingreso de datos al usuario
print(f"Ingrese {ingreso} numeros, al final se le informara cual es la media de dichos numeros")
for i in range(ingreso): #El loop se repite hasta el valor de la variable ingreso
    num = int(input("Ingrese un numero entero\n"))
    i += 1 #sumamos +1 al contador i para el loop
    sum = sum + num #sumamos los numeros en el sumador "sum"

promedio = float(sum / ingreso)
print(f"El promedio de los numeros es: {promedio}")
