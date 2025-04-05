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
    i = int(i/10) #se divide i por 10 y se quita los decimales pasando ese resultado a integeger

print(f"El numero {num}, tiene {digitos} digitos")


