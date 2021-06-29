
def traductor_a_morse( mensaje ):

    alphabet = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }
    mensaje_traducido = ''

    for c in mensaje:
        if c != ' ' and c .upper() in alphabet :
            mensaje_traducido += f'{ alphabet[ c .upper() ] } '
        else :
            mensaje_traducido += '/ '

    return mensaje_traducido .strip()

mensaje = 'Nos han picado los mosquitos'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar

mensaje = 'hemos encontrado una planta Nunca antes vista'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar

mensaje = 'teNeMOS COmida para tres Dias mas'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar
