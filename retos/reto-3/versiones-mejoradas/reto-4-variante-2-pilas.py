class SoftMed :

    texto_actual = ''
    texto_escrito = []
    rehacer = []
    inputs = 0

    @classmethod
    def restart( cls ) :
        cls .texto_actual = ''
        cls .texto_escrito = []
        cls .rehacer = []
        cls .inputs = 0

    @classmethod
    def ingresa_datos( cls, values: list ) :
        action = ''
        cls .restart()

        for value in values :

            if value == 'DESHACER' :
                cls .deshacer()
                action = value

            elif value == 'REHACER' :
                cls .re_hacer()
                action = value

            else :
                cls .inserta( value )
                action = 'INSERTAR'

            print( f' Accion: { action } ' .center( 50, '-' ) )
            print( 'Actual: ', cls .texto_actual, '\nEscrito: ', cls .texto_escrito, '\nRehacer: ', cls .rehacer, '\n' )

        return cls .concatenar()

    @classmethod
    def inserta( cls, value ) :

        if cls .inputs == 0 :
            cls .texto_actual = value
        else :
            cls .texto_escrito .append( cls .texto_actual )
            cls .texto_actual = value

        cls .rehacer .clear()

        cls .inputs += 1

    @classmethod
    def deshacer( cls ) :
        cls .rehacer .append( cls .texto_actual )
        cls .texto_actual = cls .texto_escrito[ -1 ]
        cls .texto_escrito .pop()

    @classmethod
    def re_hacer( cls ) :
        cls .texto_escrito .append( cls .texto_actual )
        cls .texto_actual = cls .rehacer[ -1 ]
        cls .rehacer .pop()

    @classmethod
    def concatenar( cls ) :
        cadena_texto = ''

        for texto in cls .texto_escrito:
            cadena_texto += texto

        cadena_texto += cls .texto_actual

        print( ' Resultados Finales ' .center( 50, '-' ) )
        print( 'Actual: ', cls .texto_actual, '\nEscrito: ', cls .texto_escrito, '\nRehacer: ', cls .rehacer, '\n' )

        return cadena_texto


# Método que agrega la plataforma
def actualizar_estado_editor( operaciones_usuario ) :

    cadena_final = SoftMed .ingresa_datos( operaciones_usuario )

    return cadena_final

operaciones_usuario = [
    'Definamos qué es una función de Python: ',
    'Una función es ',
    'un arreglo unidimensional de datos',
    'DESHACER',
    'DESHACER',
    'REHACER',
    'un grupo de instrucciones'
]

print( f'Cadena Final: "{ actualizar_estado_editor( operaciones_usuario ) }"' )