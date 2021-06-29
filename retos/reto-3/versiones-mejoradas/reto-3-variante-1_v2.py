def traductor_a_morse( mensaje_a_traducir ) :
    letras = []
    alphabet = { ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }
    mensaje_traducido = ''

    for letra in mensaje_a_traducir : 
        letras .append( letra .upper() )

    for i in range( len( letras ) ):
        for key in alphabet :
            if letras[ i ] == key :
                mensaje_traducido += alphabet[ key ] + ' '

    return mensaje_traducido[ : -1 ]


mensaje = 'Nos han picado los mosquitos'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar

mensaje = 'hemos encontrado una planta Nunca antes vista'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar

mensaje = 'teNeMOS COmida para tres Dias mas'
print( f'{ traductor_a_morse( mensaje )}' )   # Esta linea para el validador la puedes obviar