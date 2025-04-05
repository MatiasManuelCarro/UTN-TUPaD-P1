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


