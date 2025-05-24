#Ejercicio 6

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
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo:\n") #volvemos a pedir ingreso


#pedimos ingreso de datos
numero, numero_ingresado = ingreso_datos()
#llamamos a la funcion recursiva
suma = suma_digitos(numero)

#se muestra el resultado
print (f"La suma de los digitos de {numero_ingresado} es: {suma}")