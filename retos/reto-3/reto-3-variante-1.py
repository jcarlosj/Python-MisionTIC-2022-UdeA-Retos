#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

def get_codes( morse: str ) :
    characters = []

    words = morse .split( ' / ' )

    for word in words :
        characters .append( word .split( ' ' ) )

    return characters

def encode( words: list ) :
    list_word = []
    alphabet = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }

    for word in words :
        for char in word :
            for key, code in alphabet .items() :
                if key == char :
                    list_word .append( f'{ code } ' )

        list_word .append( '/ ' )

    return list_word

def get_phrase( msg: list ) :
    phrase = ''

    for word in msg :
        for character in word :
            phrase += character

        phrase += ' '

    return phrase .strip()

def get_morse_code( words: list ) :
    list_message = []

    for list_word in words:
        list_message .append( encode( list_word ) )

    return get_phrase( list_message )[:-2]   # Elimina el ultimo espacio y la ultima barra
#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES



"""Fin espacio para programar funciones propias"""

def traductor_a_morse(mensaje_a_traducir):
    #PROGRAMA ACÁ TU SOLUCIÓN
    words = get_codes( mensaje_a_traducir .upper() )
    mensaje_traducido = get_morse_code( words )

    return mensaje_traducido

mensaje_a_traducir = 'Nos han picado los mosquitos'
print( f'"{traductor_a_morse( mensaje_a_traducir )}"' )

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
#pruebas_codigo_estudiante(traductor_a_morse)