import pathlib, os

path = pathlib .Path( __file__ ) .parent .absolute()    # Obtengo la ruta absoluta => '/home/jcarlosj/Learning/Libro de Python/archivos'
                                                        # __file__: Nombre del archivo actual

def add_tab( character ) :
    return character if character != ',' else '\t'

def separate_data( data ) :
    data_list = []

    for register in data :
        field_list = register .split( ',' )
        data_list .append( field_list )

    return data_list

def extract_data( data ) :
    data_list = []

    for register in data :
        data_list .append( [ register[ 0 ], register[ 4 ] ] )

    return data_list

def add_label( data ) :
    data_list = []

    for index, register in enumerate( data ) :
        if index != 0 :
            #print( index, register )

            value = float( register[ 1 ] )
            if value < 200 :
                register[ 1 ] = 'MUY BAJO'
            elif value < 300 :
                register[ 1 ] = 'BAJO'
            elif value < 500 :
                register[ 1 ] = 'MEDIO'
            elif value < 600 :
                register[ 1 ] = 'ALTO'
            else :
                register[ 1 ] = 'MUY ALTO'

        data_list .append( register )
        data_list[ 0 ][ 0 ] = 'Fecha'
        data_list[ 0 ][ 1 ] = 'Concepto'

    return data_list

def get_index( fields, value ) :
    return fields .index( value )

def analyze_data( data ) :
    date_field_index = get_index( data[ 0 ], 'Date' )
    low_field_index = get_index( data[ 0 ], 'Low' )
    high_field_index = get_index( data[ 0 ], 'High' )
    # print( 'date_field_index', date_field_index )

    # TODO: Mejorar la forma de asignar el valor por defecto
    lowest_price = data[ 1 ][ low_field_index ]
    lowest_price_date = data[ 1 ][ date_field_index ]
    # TODO: Mejorar la forma de asignar el valor por defecto
    highest_price = data[ 1 ][ high_field_index ]
    highest_price_date = data[ 1 ][ date_field_index ]

    # print( 'Low: ', lowest_price, lowest_price_date )
    # print( 'High: ', highest_price, highest_price_date )

    for index, register in enumerate( data ) :
        # print( register[ date_field_index ], register[ low_field_index ], register[ high_field_index ] )

        # ! Itera solo las listas que poseen los valores a analizar
        if index != 0 :

            # ? Verifica el precio mas bajo y la fecha
            if register[ low_field_index ] < lowest_price :
                lowest_price = register[ low_field_index ]
                lowest_price_date = register[ date_field_index ]

            # ? Verifica el precio mas alto y la fecha
            if register[ high_field_index ] > highest_price :
                highest_price = register[ high_field_index ]
                highest_price_date = register[ date_field_index ]

    # print( 'Low: ', lowest_price, lowest_price_date )
    # print( 'High: ', highest_price, highest_price_date )

    return (
        ( lowest_price_date, lowest_price ),
        ( highest_price_date, highest_price )
    )

def create_file( data ) :

    data = process_data( data )         #   Procesa los datos y los transforma en los datos esperados

    file_name = 'analisis_archivo.csv'
    with open( f'{ str( path ) }{ os .sep }{ file_name }' , 'w', encoding='utf8' ) as file :

        for register in data :
            #print( register )
            for field in register :
                if field in ( 'MUY BAJO', 'BAJO', 'MEDIO', 'ALTO', 'MUY ALTO', 'Concepto' ) :
                    file .write( f'{ field }' )
                else :
                    file .write( f'{ field }\t' )
                #print( field, end='\t' )
            #print( '' )
            file .write( '\n' )

def read_file() :
    data_list = None

    file_name = "TSLA.csv"
    with open( f'{ str( path ) }{ os .sep }{ file_name }' , 'r', encoding='utf8' ) as file :      # Abre y cierra el archivo automaticamente, no necesitamos el try-finally y el close()
        data = file .readlines()        # Retorna una lista con cada una de las lineas del archivo
        data = separate_data( data )
        data_list = data

    return data_list

def process_data( data ) :
    data = extract_data( data )
    data = add_label( data )

    return data

def solucion() :
    data_list = read_file()         #   Lee data del archivo
    create_file( data_list )        #   Escribe la data del archivo

    info = analyze_data( data_list )
    #print( type( info ), info )
    #return date_lowest, lowest_value, date_highest, highest_value
    return info[ 0 ][ 0 ], info[ 0 ][ 1 ], info[ 1 ][ 0 ], info[ 1 ][ 1 ]

# ! Testing
if __name__== "__main__":
    print( solucion() )
