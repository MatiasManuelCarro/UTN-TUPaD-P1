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

posicion = int(input("ingrese posicion"))
fibonacci = funcion_fibonacci_recursiva(posicion)
#Creamos la lista de fibonacci, usando un ciclo for por cada valor desde 0 hasta la posicion ingresada
lista_fibonacci = [funcion_fibonacci_recursiva(i) for i in range(posicion)]
print(f"El valor de la posicion {posicion} en la serie de fibonacci es: {fibonacci}")
print(f"La serie hasta la posicion {posicion} es: {lista_fibonacci}")