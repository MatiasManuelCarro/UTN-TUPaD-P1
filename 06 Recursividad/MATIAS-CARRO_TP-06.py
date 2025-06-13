#Ejercicio 1
#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

print("\nEjercicio 1\n")
#Inicializamos las variables numericas
numero = int(0)

#funcion recursiva que calcula el factorial
def funcion_factorial(numero):
    if numero == 0:
        return 1
    else:
        return funcion_factorial(numero - 1) * numero

def validacion_datos(numero_ingresado): #Valida que el numero ingresado sea un entero positivo
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero > 0 and numero < 999: #verifica que el entero sea positivo y menor a 999 si no lo es, vuelve a pedir ingreso de datos
                return numero #si es entero, positivo, y menor a 999, devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        
print("Programa que muestra el factorial de un numero ingresado, ademas de todos los factoriales entre ese numero y 1")
numero_ingresado = input("Ingrese un numero entero positivo para mostrar su factorial (maximo 998):\n")
numero = validacion_datos(numero_ingresado)

#ciclo FOR que reduce el numero ingresado por cada vuelta, para mostrar todos los factoriales 
#Entre el numero ingresado y 1 
for i in range(numero, 0, -1): 
        fact = funcion_factorial(numero) #llamada a la funcion factorial
        print(f"{numero}! = {fact}") #se imprime el resultado
        numero = numero -1 #se reduce el numero ingresado en 1

#Ejercicio 2 
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

print("\nEjercicio 2\n")

#Funcion recursiva para fibonacci
def funcion_fibonacci_recursiva(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        #print(f"posicion! {posicion}")
        return funcion_fibonacci_recursiva(posicion - 1) + funcion_fibonacci_recursiva(posicion - 2)

#Funcion para validar datos ingresados
def validacion_datos(numero_ingresado):                                 #Valida que el numero ingresado sea un entero positivo
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            posicion = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if posicion > 0 and posicion <= 35: #verifica que el entero sea positivo y maximo 35
                return posicion #si es entero y positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor o igual a 35:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor o igual a 35:\n") #volvemos a pedir ingreso

print("Programa que muestra el valor de la posicion en una secuencia de fibonacci")
numero_ingresado = input("ingrese posicion (maximo 35)") #dato ingresado por el usuario, falta validar si el ingreso es correcto
posicion = validacion_datos(numero_ingresado) #se valida el ingreso y se devuelve a la variable posicion
fibonacci = funcion_fibonacci_recursiva(posicion) #se busca el valor de esa posicion en la secuencia 

#Creamos la lista de fibonacci, usando un ciclo for por cada valor desde 0 hasta la posicion ingresada
lista_fibonacci = [funcion_fibonacci_recursiva(i) for i in range(posicion)]
#mostramos los resultados
print(f"El valor de la posicion {posicion} en la serie de fibonacci es: {fibonacci}")
print(f"La serie hasta la posicion {posicion} es: {lista_fibonacci}")

#Ejercicio 3

#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general

print("\nEjercicio 3\n")
#funcion de potencia recursiva
def potencia_recursiva(base, exponente):
    if exponente == 0: #el exponente 0 es lo que frena la recursividad 
        return 1 #al retornar 1 se termina todos los calculos almacenados en el call stack
    
    return base * potencia_recursiva(base, exponente -1)

def validacion_datos(base_ingreso, exponente_ingreso): #Valida que los numeros ingresados sean enteros
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar los ingresos a un integer
            base = int(base_ingreso) #si es integer, se guarda en la variable numero
            exponente = int(exponente_ingreso)
            if base > 0 and exponente > 0 and base < 999 and exponente < 999: #verifica que sean positivos
                return base, exponente 
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal 
            print("\nDatos ingresados incorrectos")
            print("\nIngrese otros numeros, recuende recuerde que tiene que ser un entero positivo menor a 999:\n")
            base_ingreso = input("Ingrese un numero entero positivo para la base:\n") #volvemos a pedir ingreso
            exponente_ingreso = input("Ingrese un numero entero positivo para el exponente\n")

#solicitud de ingreso de datos
print("Programa que calcula la potencia de un numero, ingresando la base (numero) y el exponente")
base_ingreso = input("Ingrese un numero entero positivo para la base: (maximo 998)\n")
exponente_ingreso = input("Ingrese un numero entero positivo para el exponente: (maximo 998 )\n")

#se llama a la funcion de validacion de datos
base, exponente = validacion_datos(base_ingreso, exponente_ingreso)

#se llama a la funcion recursiva de potencia
resultado = potencia_recursiva(base, exponente)
print(f"El resultado de {base} elevado a {exponente} es igual a: {resultado}")

#Ejercicio 4
# Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

print("\nEjercicio 4\n")

#inicializamos la variable
resultado = str("")

#Funcion recursiva para pasar a binarios
def conversor_binario_recursivo(numero_decimal):
    if numero_decimal == 0: #condicion de salida, si la division entera recursiva del numero decimal es igual a 0, devolvemos 0 como texto
        return "0"
    if numero_decimal == 1:
        return "1" #condicion de salida, si la division entera recursiva del numero decimal es igual a 1, devolvemos 1 como texto
    #se devuelve la division entera del numero ingresado, de manera que llegue a un 0 o un 1
    #y se agrega como string el resto de la division de ese numero dividido por 2 a la cadena de texto
    return conversor_binario_recursivo(numero_decimal // 2) + str(numero_decimal % 2) 

def validacion_datos(numero_ingresado): #Valida que el numero ingresado sea un entero positivo
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero_decimal = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero_decimal > 0: #verifica que el entero sea positivo si no lo es, vuelve a pedir ingreso de datos
                return numero_decimal #si es entero, positivo, y menor a 999, devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positvo:\n") #volvemos a pedir ingreso

#pedimos los datos al usuraio
print("Ingrese un numero entero positivo para pasar a decimal  ")
numero_ingresado = input("Ingrese numero\n")
numero_decimal = validacion_datos(numero_ingresado) #se verifica que el ingreso sea correcto
resultado = conversor_binario_recursivo(numero_decimal) #llamamos a la funcion recursiva para pasar a binarios 
print(f"El numero {numero_decimal} en binario es: {resultado}")

print("\nEjercicio 5\n")

#Lista de las vocales para reemplazar en la cadena de texto
vocales_con_acentos = ['á', 'é', 'í', 'ó', 'ú', 'ü']
vocales_sin_acentos = ['a', 'e', 'i', 'o', 'u', 'u']

#funcion recursiva que devuelve si una palabra o frase es un palindromo
#utiliza dos indices, uno parte de la izquierda en 0
#el otro desde la derecha, que se saca del numero total de letras
def es_palindromo(palabra, indice_izquierdo, indice_derecho):
    #si los indices pasan a ser iguales (se encuentran en el medio de la palabra)
    #y todas las letras coinciden, la palabra es un palindromo
    if indice_izquierdo >= indice_derecho: 
        return True
    if palabra[indice_izquierdo] != palabra[indice_derecho]: #si en algun momento las letras son distintas, NO es un palindromo
        return False
    #se vuelve a llamar a la funcion de manera recursiva moviendo los indices
    return es_palindromo(palabra, indice_izquierdo+1, indice_derecho-1, )

#ingreso validacion de datos
def ingreso_de_datos():
    palabra = str(input("Ingrese una palabra o frase sin espacio, para mostar si es un palindromo o no:\n"))
    palabra_original = palabra #se guarda la palabra como la ingreso el usuario
    palabra = palabra.replace(" ", "") #se eliminan los espacios
    palabra = palabra.lower() #se pasa a minusculas
    for i in range(len(vocales_con_acentos)): #ciclo for, reemplaza las vocales con acentos por vocales sin acento
        palabra = palabra.replace(vocales_con_acentos[i], vocales_sin_acentos[i])
    
    return palabra, palabra_original

palabra, palabra_original = ingreso_de_datos()
#indices para las posiciones de las letras en la cadena de texto
indice_izquierdo = 0
indice_derecho = len(palabra) -1

palindromo = es_palindromo(palabra, indice_izquierdo, indice_derecho)

#se devuelve el resultado
if palindromo == True:
    print(f"{palabra_original} es un palindromo")
else:
    print(f"{palabra_original} NO es un palindromo")

#Ejercicio 6

print("\nEjercicio 6\n")

#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos

#funcion recursiva que suma todos los digitos de un numero
def suma_digitos(numero):
    if numero < 10: # la condicion de corte es que el numero quede en un solo digito 
        return numero
    #devuelve la suma de numero % 10 (el ultimo numero) + numero // 10 (reduce el numero en una cifra, esto comienza la recursividad)
    return suma_digitos(numero % 10) + suma_digitos(numero // 10)

def ingreso_datos(): #Valida que el numero ingresado sea un entero positivo
    numero_ingresado = input("Ingrese un numero entero positivo para mostrar la suma de sus cifras\n")
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero > 0: #verifica que el entero sea positivo, si no lo es, vuelve a pedir ingreso de datos
                return numero, numero_ingresado #si es entero positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso


#pedimos ingreso de datos
numero, numero_ingresado = ingreso_datos()
#llamamos a la funcion recursiva
suma = suma_digitos(numero)

#se muestra el resultado
print (f"La suma de los digitos de {numero_ingresado} es: {suma}")

#Ejercicio 7

#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.

print("\n Ejercicio 7\n")
print("Ingrese la cantidad de bloques que tiene una piramide en su base, se sumara el total de bloques de la piramide")

#funcion recursiva que devuelve la cantidad de bloques de la piramide
def contar_bloques(numero_bloques):
    if numero_bloques == 2:         #condicion de frenado al ser 2, sabemos que queda un solo piso mas con 1
        return numero_bloques + 1       #se suma el ultimo bloque y se evita una iteracion extra
    #retorno recursivo, resta un bloque por cada capa de la piramide
    return contar_bloques(numero_bloques-1) + numero_bloques

def ingreso_datos():        #Valida que el numero ingresado sea un entero positivo
    numero_bloques = input("Ingrese la cantidad de bloques de la base de la piramide\n")
    while True:         #Se repite el loop hasta que la funcion retorne el numero
        try:        #intenta pasar el ingreso a un integer
            numero_bloques = int(numero_bloques)        #si es integer, se guarda en la variable numero
            if numero_bloques > 0:      #verifica que el entero sea positivo, si no lo es, vuelve a pedir ingreso de datos
                return numero_bloques       #si es entero positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_bloques = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n")         #volvemos a pedir ingreso
        except ValueError:      #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_bloques = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n")         #volvemos a pedir ingreso


numero_bloques = ingreso_datos()
cantidad_total_bloques = contar_bloques(numero_bloques)

print(f"Una piramide con {numero_bloques} bloques en la base, tiene {cantidad_total_bloques} bloques en total")


#Ejercicio 8
#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

print("\n Ejercicio 8\n")
print("Programa donde se ingresa un numero y un digito \n luego se muestra cuantas veces ese digito se encuentra dentro de este numero")

#funcion recursiva que cuenta la cantidad de veces que esta un digito en un numero ingresado
def contar_digito(numero, digito,):
    #condicion de corte, si el numero es menor a 10 (un solo digito)
    if numero < 10:
        #devolvemos 1 SI el numero es igual al digito, sino, devolvemos 0
        return 1 if numero == digito else 0
    #llamada a la funcion recursiva
    #devuelve 1 si el ultimo numero del numero ingresado es igual al digito + el numero // 10
    #numero // 10 quita el ultimo numero del numero ingresado, se repite hasta que quede un solo digito
    return (1 if numero % 10 == digito else 0) + contar_digito(numero//10, digito)

def ingreso_datos():        #Valida el ingreso de los datos, que sean enteros positivos
    numero = input("Ingrese un numero entero positivo\n")
    digito = input("Ingrese un solo digito para buscar cuantas veces esta en el numero ingresado\n")
    while True:         #Se repite el loop hasta que la funcion retorne el numero
        try:        #intenta pasar el ingreso a un integer
            numero = int(numero)        #si es integer, se guarda en la variable numero
            digito = int(digito)
            if numero > 0 and digito < 10:      #verifica que el entero sea positivo y digito un solo numero
                return numero, digito         #si es entero positivo devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n")       #volvemos a pedir ingreso
                digito = input("Ingrese un digito, recuerde que tiene que ser un solo numero")
        except ValueError:      #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n")       #volvemos a pedir ingreso
            digito = input("Ingrese un digito, recuerde que tiene que ser un solo numero")

#ingreso de datos
numero, digito = ingreso_datos()

#llamada a la funcion recursiva
digito_repeticiones = contar_digito(numero, digito)

#salida de datos
if digito_repeticiones == 1 and digito_repeticiones != 0:
    print(f"En el numero {numero} el digito {digito} se encuentra: {digito_repeticiones} vez")
else:
    print(f"En el numero {numero} el digito {digito} se encuentra: {digito_repeticiones} veces")
