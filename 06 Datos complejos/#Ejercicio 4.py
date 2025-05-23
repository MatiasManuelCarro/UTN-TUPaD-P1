#Ejercicio 4
# Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

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
