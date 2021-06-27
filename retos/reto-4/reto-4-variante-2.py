#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIALv
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

class SoftMed :

    texto_actual = ''
    texto_escrito = []
    rehacer = []
    counter = 0

    @classmethod
    def restart( cls ) :
        cls .texto_actual = ''
        cls .texto_escrito = []
        cls .rehacer = []
        cls .counter = 0

    @classmethod
    def ingresa_datos( cls, values ) :
        cls .restart()

        for value in values :

            if value == 'DESHACER' :
                cls .deshacer()

            elif value == 'REHACER' :
                cls .re_hacer()

            else :
                cls .inserta( value )

        return cls .concatenar()

    @classmethod
    def inserta( cls, value ) :

        if cls .counter == 0 :
            cls .texto_actual = value

        else :
            cls .texto_escrito .append( cls .texto_actual )
            cls .texto_actual = value

        cls .rehacer .clear()
        cls .counter += 1

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

        for texto in cls .texto_escrito :
            cadena_texto += texto

        cadena_texto += cls .texto_actual

        return cadena_texto



"""Fin espacio para programar funciones propias"""

def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cadena_final = SoftMed .ingresa_datos( operaciones_usuario )
    return cadena_final

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA,  NO MODIFICARLA
"""
operaciones_usuario = [
    'Definamos qué es una función de Python: ',
    'Una función es ',
    'un arreglo unidimensional de datos',
    'DESHACER',
    'DESHACER',
    'REHACER',
    'un grupo de instrucciones'
]

print( actualizar_estado_editor( operaciones_usuario ) )
#pruebas_codigo_estudiante(actualizar_estado_editor)