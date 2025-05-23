#Ejercicio 2 
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

def funcion_fibonacci_recursiva(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        #print(f"posicion! {posicion}")
        return funcion_fibonacci_recursiva(posicion - 1) + funcion_fibonacci_recursiva(posicion - 2)

#Funcion para validar datos ingresados
def validacion_datos(numero_ingresado): #Valida que el numero ingresado sea un entero positivo
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
numero_ingresado = input("ingrese posicion")
posicion = validacion_datos(numero_ingresado)
fibonacci = funcion_fibonacci_recursiva(posicion)

#Creamos la lista de fibonacci, usando un ciclo for por cada valor desde 0 hasta la posicion ingresada
lista_fibonacci = [funcion_fibonacci_recursiva(i) for i in range(posicion)]
print(f"El valor de la posicion {posicion} en la serie de fibonacci es: {fibonacci}")
print(f"La serie hasta la posicion {posicion} es: {lista_fibonacci}")