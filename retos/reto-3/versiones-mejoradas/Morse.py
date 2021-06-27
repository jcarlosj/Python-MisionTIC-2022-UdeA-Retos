class Morse :

    alphabet = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }

    @classmethod
    def get_codes( cls, morse: str ):
        characters = []

        words = morse .split( ' / ' )

        for word in words :
            characters .append( word .split( ' ' ) )

        return characters

    @classmethod
    def decode( cls, word: list ) :
        list_word = []

        for char in word :
            for key, code in cls .alphabet .items() :
                if code == char :
                    list_word .append( key )

        return list_word

    @classmethod
    def encode( cls, words: list ) :
        list_word = []

        for word in words :
            for char in word :
                for key, code in cls .alphabet .items() :
                    if key == char :
                        list_word .append( f'{ code } ' )

            list_word .append( ' / ' )

        return list_word

    @classmethod
    def get_phrase( cls, msg: list ) :
        phrase = ''

        for word in msg :
            for character in word :
                phrase += character

            phrase += ' '

        return phrase .strip()

    @classmethod
    def get_message( cls, codes ) :
        list_message = []

        for list_word in codes:
            list_message .append( cls .decode( list_word ) )

        return cls .get_phrase( list_message )

    @classmethod
    def get_morse_code( cls, words: list ) :
        list_message = []

        for list_word in words:
            list_message .append( cls .encode( list_word ) )

        return cls .get_phrase( list_message )

    @classmethod
    def decode_msg( cls, code_morse ) :
        codes = cls .get_codes( code_morse )

        return cls .get_message( codes )

    @classmethod
    def encode_msg( cls, message ) :
        words = cls .get_codes( message .upper() )

        return cls .get_morse_code( words )

# ! Testing Class
if __name__ == '__main__' :
    message = 'Hola Terricolas estan apunto de ser invadidos'
    code_morse = Morse .encode_msg( message )
    print( code_morse )

    message = Morse .decode_msg( code_morse )
    print( message )

    # code_morse = '-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ...'
    # message = Morse .decode_msg( code_morse )
    # print( message )

    # code_morse = '.... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-'
    # morse = Morse()
    # message = Morse .decode_msg( code_morse )
    # print( message )

    # code_morse = '- . -. . -- --- ... / -.-. --- -- .. -.. .- / .--. .- .-. .- / - .-. . ... / -.. .. .- ... / -- .- ...'
    # morse = Morse()
    # message = Morse .decode_msg( code_morse )
    # print( message )

    # code_morse = '.... . -- --- ... / . -. -.-. --- -. - .-. .- -.. ---'
    # morse = Morse()
    # message = Morse .decode_msg( code_morse )
    # print( message )

    # code_morse = '.... --- .-.. .- / .- / - --- -.. --- ...'
    # morse = Morse()
    # message = Morse .decode_msg( code_morse )
    # print( message )