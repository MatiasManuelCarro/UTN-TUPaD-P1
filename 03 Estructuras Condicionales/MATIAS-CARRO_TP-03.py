#Trabajo practico 3: Estructuras condicionales
#Alumno: Matias Carro 

#Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad:\n"))
if edad >= 18:
    print("Es mayor de edad")

#Ejercicio 2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota final:\n"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

