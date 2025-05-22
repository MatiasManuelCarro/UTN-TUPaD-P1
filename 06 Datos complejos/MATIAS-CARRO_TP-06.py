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
                return numero #si es entero, positivo, y menor a 999, retora el numero
            else:
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo menor a 999:\n") #volvemos a pedir ingreso
        
print("Programa que muestra el factorial de un numero ingresado, ademas de todos los factoriales entre ese numero y 1")
numero_ingresado = int(input("Ingrese un numero entero positivo para mostrar su factorial (maximo 998):\n"))
numero = validacion_datos(numero_ingresado)

#ciclo FOR que reduce el numero ingresado por cada vuelta, para mostrar todos los factoriales 
#Entre el numero ingresado y 1 
for i in range(numero, 0, -1): 
        fact = funcion_factorial(numero) #llamada a la funcion factorial
        print(f"{numero}! = {fact}") #se imprime el resultado
        numero = numero -1 #se reduce el numero ingresado en 1

