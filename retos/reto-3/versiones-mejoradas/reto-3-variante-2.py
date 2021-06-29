def traductor_a_espanol( mensaje_a_traducir ):
    # Declarando variables
    mensaje_traducido = ''
    alfabeto = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }
    letras = []         # Mensaje completo separado por conjuntos de letras por palabra

    palabras = mensaje_a_traducir .split( ' / ' )

    for palabra in palabras :
        letras .append( palabra .split( ' ' ) )     #

    #print( letras )

    for lista_palabras in letras :
        for codigo in lista_palabras :              # codigo: es cada uno de los codigos del clave morse
            for llave, valor in alfabeto .items():  # items() funcion que retorna la llave y valor del diccionario
                if codigo == valor :                # dict { llave: valor, ... }
                    # Debug
                    # print( codigo, llave ) # Comparar dentro del Alfabeto( codigo morse => equivalente )
                    mensaje_traducido += llave
        #print( '' ) # Aqui
        mensaje_traducido += ' '

    return mensaje_traducido

morse = '-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ...'
print( traductor_a_espanol( morse ) )

morse = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-"
print( traductor_a_espanol( morse ) )

morse = "- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ..."
print( traductor_a_espanol( morse ) )

morse = ".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. ---"
print( traductor_a_espanol( morse ) )