#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

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
    for i in range(len(vocales_con_acentos)): #ciclo for, reemplaza las vocales con acentos por vocales
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
