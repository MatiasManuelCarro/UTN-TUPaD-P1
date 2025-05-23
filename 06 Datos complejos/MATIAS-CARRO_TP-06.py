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
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
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
            if posicion > 0: #verifica que el entero sea positivo 
                return posicion #si es entero y positivo devuelve el numero
            else:
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso

print("Programa que muestra el valor de la posicion en una secuencia de fibonacci")
numero_ingresado = input("ingrese posicion") #dato ingresado por el usuario, falta validar si el ingreso es correcto
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
            if base > 0 and exponente > 0: #verifica que sean positivos
                return base, exponente 
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal 
            print("\nIngrese otros numeros, recuende que deben ser enteros y positivo :\n")
            base_ingreso = input("Ingrese un numero entero positivo para la base:\n") #volvemos a pedir ingreso
            exponente_ingreso = input("Ingrese un numero entero positivo para el exponente:\n")

#solicitud de ingreso de datos
print("Programa que calcula la potencia de un numero, ingresando la base (numero) y el exponente")
base_ingreso = input("Ingrese un numero entero positivo para la base:\n")
exponente_ingreso = input("Ingrese un numero entero positivo para el exponente:\n")

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
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positvo:\n") #volvemos a pedir ingreso

#pedimos los datos al usuraio
print("Ingrese un numero entero positivo para pasar a decimal  ")
numero_ingresado = input("Ingrese numero\n")
numero_decimal = validacion_datos(numero_ingresado) #se verifica que el ingreso sea correcto
resultado = conversor_binario_recursivo(numero_decimal) #llamamos a la funcion recursiva para pasar a binarios 
print(f"El numero {numero_decimal} en binario es: {resultado}")
