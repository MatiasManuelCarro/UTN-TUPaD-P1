#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

vocales_con_acentos = ['á', 'é', 'í', 'ó', 'ú', 'ü']
vocales_sin_acentos = ['a', 'e', 'i', 'o', 'u', 'u']

#funcion recursiva que devuelve si una palabra o frase es un palindromo
def es_palindromo(palabra, indice_izquierdo, indice_derecho):

    if indice_izquierdo >= indice_derecho:
        return True
    if palabra[indice_izquierdo] != palabra[indice_derecho]:
        return False
    
    return es_palindromo(palabra, indice_izquierdo+1, indice_derecho-1, )

def ingreso_de_datos():
    palabra = str(input("Ingrese una palabra o frase sin espacio, para mostar si es un palindromo o no:\n"))
    palabra_original = palabra
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    for i in range(len(vocales_con_acentos)):
        palabra = palabra.replace(vocales_con_acentos[i], vocales_sin_acentos[i])
    
    return palabra, palabra_original

palabra, palabra_original = ingreso_de_datos()
indice_izquierdo = 0
indice_derecho = len(palabra) -1

palindromo = es_palindromo(palabra, indice_izquierdo, indice_derecho)

if palindromo == True:
    print(f"{palabra_original} es un palindromo")
else:
    print(f"{palabra_original} NO es un palindromo")
