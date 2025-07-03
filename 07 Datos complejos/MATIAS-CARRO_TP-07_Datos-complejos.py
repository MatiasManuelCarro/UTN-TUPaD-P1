#Ejercicio 1 
#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

print ("\nEjercicio 1\n")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(f"Diccionario inicial: {precios_frutas}")

#Se agregan al diccionario los keys y los valores
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"\nSe agregan los elementos: {precios_frutas}")

#Ejercicio 2
#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

print ("\nEjercicio 2\n")

print(f"Diccionario inicial: {precios_frutas}")

#se actualizan los valores de los items 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 3000

print(f"\nSe actualizan los precios: {precios_frutas}")

#Ejercicio 3
#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

print ("\nEjercicio 3\n")

#se pasan las keys a una lista con la funcion list()
listado_frutas = list(precios_frutas.keys())

print(f"Listado de las frutas: \n{listado_frutas}")

#Ejercicio 4
#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

print ("\nEjercicio 4\n")

def validacion_datos(numero_ingresado):              #Valida que el numero ingresado sea un entero positivo
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero_contacto = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero_contacto > 0: #verifica que el entero sea positivo 
                return numero_contacto #si es entero y positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, el numero de telefono no debe contener ni simbolos ni letras:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, el numero de telefono no debe contener ni simbolos ni letras:\n") #volvemos a pedir ingreso

print("Ingrese nombre y numero de las personas a agendar")

datos_contactos = {}

for i in range(5):
    nombre_contacto = str(input("Ingrese el nombre del contacto para agendar:\n"))
    numero_contacto = input("Ingrese el numero del contacto para agendar:\n")
    #Agregamos los datos ingresados al diccionario
    datos_contactos[nombre_contacto] = numero_contacto

#solicitamos un nombre para la busqueda 
nombre_busqueda = input("Ingrese un nombre para buscar sus datos en la agenda:\n")

if nombre_busqueda in [contacto for contacto in datos_contactos]:
    print(f"El numero de {nombre_busqueda} es: {datos_contactos[nombre_contacto]}") 
else:
    print(f"El nombre {nombre_busqueda} no se encuentra agendado")

#Ejercicio 5
#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

print ("\nEjercicio 5\n")

frase_ingresada = str(input("ingrese una frase:\n"))
frase_ingresada = frase_ingresada.split() #se separa el str en palabras con split, formando una lista

palabras_unicas = set() #se crea el, set vacio
recuento_palabras = {}
for palabra in frase_ingresada:
    palabras_unicas.add(palabra) #se agregan las palabras al set

    if palabra in recuento_palabras: #recorre la lista
        recuento_palabras[palabra] += 1 #si la palabra ya estaba agregada, se suma 1 al conteo
    else:
        recuento_palabras[palabra] =1 #si no, se crea el elemento en el diccionario

print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento de palabras {recuento_palabras}")

#Ejercicio 6
#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno

print ("\nEjercicio 6\n")

#se crean las listas
lista_alumnos = []
lista_notas_alum_1 = []
lista_notas_alum_2 = []
lista_notas_alum_3 = []
lista_notas = [lista_notas_alum_1, lista_notas_alum_2, lista_notas_alum_3] #lista con listas dentro para poder iterar

def validacion_datos(numero_ingresado):              #Valida que el numero ingresado sea un entero positivo entre menor o igual a 10
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero_ingresado = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero_ingresado > 0 and numero_ingresado <= 10:#verifica que el entero sea positivo y menor o igual a 10
                return numero_ingresado #si es entero y positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, entre 0 y 10:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, entre 0 y 10:\n") #volvemos a pedir ingreso

for i in range(3):
    alumno = str(input(f"Ingrese el nombre del alumno N° {i+1}:\n")) #se ingresan los 3 alumnos en el ciclo for
    lista_alumnos.append(alumno)
    for c in range (3):
        notas = input(f"Ingrese la nota N°{c+1} del alumno {lista_alumnos[i]}:\n") #se ingresan las 3 notas por cada alumno
        notas = validacion_datos(notas) #validacion de datos
        lista_notas[i].append(notas) #se agregan las notas a la lista correspondiente (valor de i)

#se crean las tuplas y la lista de tuplas para iterar
tupla_alumno_1 = tuple(lista_notas_alum_1)
tupla_alumno_2 = tuple(lista_notas_alum_2)
tupla_alumno_3 = tuple(lista_notas_alum_3)
lista_tuplas = [tupla_alumno_1, tupla_alumno_2, tupla_alumno_3]

#se crean los dos diccionarios
diccionario_notas = {}
diccionario_promedios = {}


for i in range(3):
    #se agregan al diccionario la clave (nombre del alumno en la posicion i) y las notas (tupla que corresponde a la posicion i)
    diccionario_notas[lista_alumnos[i]] = lista_tuplas[i]
    #Se agrega al diccionario la clave del nombre del alumno (posicion i de la lista de alumnos) y el promedio de las notas en la tupla
    diccionario_promedios[lista_alumnos[i]] = (sum(lista_tuplas[i])/3)

#se imprimen los valores de los diccionarios
for clave, valor in diccionario_notas.items():
    print(f"Notas del alumno {clave}: {valor}\n")

for clave, valor in diccionario_promedios.items():
    print(f"Promedio del alumno {clave}: {valor}\n")

#Ejercicio 7
#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

print ("\nEjercicio 7\n")

# Listas de studiantes que aprobaron cada parcial
parcial_1 = {10, 12, 15, 16}
parcial_2 = {18, 15, 12, 11}

# Estudiantes que aprobaron ambos parciales 
ambos_parciales = parcial_1 & parcial_2
print("Estudiantes que  Aprobaron ambos parciales:", ambos_parciales)

#Estudiantes que aprobaron un solo parcial
solo_un_parcial = parcial_1 ^ parcial_2
print("Estudiantes que probaron solo uno:", solo_un_parcial)

#Estudiantes que aprobaron al menos uno 
al_menos_un_parcial = parcial_1 | parcial_2
print("Estudiantes que aprobaron al menos un parcial:", al_menos_un_parcial)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

print ("\nEjercicio 8\n")

import os

diccionario_productos = {}

def validacion_datos(numero_ingresado):              #Valida que el numero ingresado sea un entero positivo
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero_ingresado = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero_ingresado > 0: #verifica que el entero sea positivo
                return numero_ingresado #si es entero y positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero:\n") #volvemos a pedir ingreso
menu = str("a")

while menu != "S":
    print("Control de stock, por favor ingrese una opcion: ")
    print("A: para ver el stock de los productos")
    print("B: Actualizar cantidades de producto")
    print("C: Para agregar un nuevo producto")
    print("S para salir")
    menu = str(input("Ingrese opcion:\n").upper())

    match menu:
        case "A":
            if not diccionario_productos:
                print("El inventario esta vacio\n")
            else:
                print(diccionario_productos)
            input("Presione enter para continuar")
            os.system("cls")
        case "B":
            producto = str(input("Ingrese un producto que quiera agregar cantidades al stock:\n").lower())
            if producto in diccionario_productos:
                cantidad= input("Ingrese la cantidad a agregar:\n")
                cantidad = validacion_datos(cantidad)
                diccionario_productos[producto] += cantidad
            else:
                print("El producto no existe en stock")
            input("Presione enter para continuar")
            os.system("cls")
        case "C": 
            producto = str(input("Ingrese un producto que quiera agregar al inventario:\n").lower())
            if producto not in diccionario_productos:
                cantidad= input("Ingrese la cantidad a agregar:\n")
                cantidad = validacion_datos(cantidad)
                diccionario_productos[producto] = cantidad
            else:
                print("Este item ya se encuentra en el inventario")
            input("Presione enter para continuar")
            os.system("cls")
        case _:
            if menu == "S":
                print("Saliendo del programa")
            else:
                print("Ingrese un valor correcto")
                input("Presione enter para continuar")
                os.system("cls")

#Ejercicio 9
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Ejemplo

print ("\nEjercicio 9\n")

#Agenda:
agenda = {
    ("lunes", "19:00"): "Clases Organizacion empresarial",
    ("martes", "18:00"): "Clases Programacion",
    ("martes", "19:00"): "Clases Arq. y Sistemas Operativos",
    ("miercoles", "18:00"): "Clases Matematica",
    ("miercoles", "19:00"): "Clases Organizacion empresarial",
    ("jueves", "18:00"): "Clases Programacion",
    ("jueves", "19:00"): "Clases Arq. y Sistemas Operativos",
    ("verines", "20:30"): "Clases Matematica",
}

#funcion para buscar los eventos
def consultar_evento(dia, hora):
    clave = (dia.lower(), hora) #pasa a minusculas el dia
    evento = agenda.get(clave) #se guarda la busqueda en evento 

    if evento: #verifica que exista en la agenda, si no se informa que no hay
        print(f"Tenes una Actividad el {dia} a las {hora}: {evento}")
    else:
        print(f"No tenes una actividad programada el {dia} a las {hora}.")

#Ingreso del usuario
dia = input("Ingrese el dia que que quiere ver si tiene un evento:\n")
hora = input("Ingrese la hora para verificar si existe un evento:\n")
consultar_evento(dia, hora)

#Eventos de prueba
consultar_evento("martes", "18:00")
consultar_evento("miércoles", "11:00")


#ejercicio 10

#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

print ("\nEjercicio 10\n")

#diccionario original
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

#invertimos el diccionario con list comprehension
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

#mostramos el resultado
print(f"Lista original:\n{paises_capitales}")
print(f"Lista invertida:\n{capitales_paises}")