import pathlib, os
# __nombre__ Dunder: Metodo Magico
path = pathlib .Path( __file__ ) .parent .absolute()

def analiza_data( data_list ) :
    index_data = data_list[ 0 ] .index( 'Date' )
    index_high = data_list[ 0 ] .index( 'High' )
    index_low = data_list[ 0 ] .index( 'Low' )

    # Definimos valores por defecto (Primeros datos del archivo)
    mayor = data_list[ 1 ][ 2 ] # High
    menor = data_list[ 1 ][ 3 ] # Low
    fecha_mayor = data_list[ 1 ][ 0 ]
    fecha_menor = data_list[ 1 ][ 0 ]

    for index, registro in enumerate( data_list ) :
        if index > 0 :

            if registro[ index_low ] < menor :
                menor = registro[ index_low ]
                fecha_menor = registro[ index_data ]
            if registro[ index_high ] > mayor :
                mayor = registro[ index_high ]
                fecha_mayor = registro[ index_data ]

    return fecha_mayor, float( mayor ), fecha_menor, float( menor )

def separa_data( data_list ) :
    data_procesada = []

    for registro in data_list :
        campos = registro .split( ',' )     # split: retorna una lista con los valores separados de acuerdo al patron
        data_procesada .append( campos )

    return data_procesada

def crear_archivo( nombre_archivo, data_list ) :
    # Linux / Windows \
    with open( f'{ path }{ os .sep }{ nombre_archivo }', 'w' ) as file :
        #file .write( data_list )           # Se rompe por que espera escribir un string no una lista
        for registro in data_list :
            for campo in registro :
                if campo in ( 'Fecha', 'Concepto', 'Concepto' ) :
                    file .write( f'{ campo }\t' )
                else :
                    file .write( f'{ campo }\t' )

            file .write( '\n' )

def procesar_data( data_list: list ) :
    data_procesada = []  # Lista vacia que espera por datos procesados
    #enunciados = data_list[ 0 ] .split( ',' )      # Enunciados => split retorna una lista
    #print( ' XXX ', enunciados )

    for index, registro in enumerate( data_list ):
        if index > 0 :
            campos = registro .split( ',' )
            data_procesada .append( [ campos[ 0 ], campos[ 4 ] ] )

    return data_procesada

def leer_archivo( nombre_archivo ) :
    data = None

    # Linux / Windows \
    with open( f'{ path }{ os .sep }{ nombre_archivo }', 'r' ) as file :
        # print( file .readlines() )

        data_list = file .readlines()
        data = data_list

    return data

def etiquetado( data_list ) :
    for registro in data_list :
        valor = float( registro[ 1 ] )

        if valor < 200 :
            registro[ 1 ] = 'MUY BAJO'
        elif valor < 300 :
            registro[ 1 ] = 'BAJO'
        elif valor < 500 :
            registro[ 1 ] = 'MEDIO'
        elif valor < 600 :
            registro[ 1 ] = 'ALTO'
        else :
            registro[ 1 ] = 'MUY ALTO'

    data_list .insert( 0, ['Fecha', 'Concepto'] )   # Inserta los nuevos enunciados

    return data_list

# ! Testing: Solo funciona si es ejecutado desde este archivo
if __name__ == '__main__':

    def solucion():

        data_original = leer_archivo( 'TSLA.csv' )
        data_procesada = procesar_data( data_original )
        data_etiquetada = etiquetado( data_procesada )
        crear_archivo( 'analisis_archivo.csv', data_etiquetada )

        data_separada = separa_data( data_original )
        fmayor, vmayor, fmenor, vmenor = analiza_data( data_separada )

        return fmenor, vmenor, fmayor, vmayor
        #return date_lowest, lowest_value, date_highest, highest_value

    print( solucion() )
