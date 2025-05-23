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