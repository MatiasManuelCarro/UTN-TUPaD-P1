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










