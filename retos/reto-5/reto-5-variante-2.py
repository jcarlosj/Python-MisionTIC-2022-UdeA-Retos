import pathlib, os

path = pathlib .Path( __file__ ) .parent .absolute()    # Obtengo la ruta absoluta => '/home/jcarlosj/Learning/Libro de Python/archivos'
print( path )                                                     # __file__: Nombre del archivo actual

# Obtener la fecha y el valor del precio mas alto y el mas bajo
def obtener_info( data ) :
    # Definir valores por defecto para establecer comparaciones
    mayor = data[ 0 ][ 2 ]
    menor = data[ 0 ][ 3 ]
    fecha_mayor = data[ 0 ][ 0 ]
    fecha_menor = data[ 0 ][ 0 ]

    for registro in data :
        if registro[ 2 ] > mayor :
            mayor = registro[ 2 ]
            fecha_mayor = registro[ 0 ]
        if registro[ 3 ] < menor :
            menor = registro[ 3 ]
            fecha_menor = registro[ 0 ]

    return fecha_mayor, float( mayor ), fecha_menor, float( menor )

# Crea y escribe el archivo procesado
def escribir_archivo( nombre_archivo, data ) :

    with open( f'{ path }{ os .sep }{ nombre_archivo }', 'w' ) as file :
        file .write( data )

# Une la data procesada
def unir_data( data ) :

    data .insert( 0, ['Fecha', 'Mean-Max-Min', 'Concepto'] )

    lineas = ''

    for registros in data :
        for campos in registros :
            lineas += f'{ str( campos ) }\t'

        lineas += '\n'

    return lineas

# Etiquetar el promedio
def etiquetar( promedio ) :
    etiqueta = None

    if promedio < 207 :
        etiqueta = 'MUY BAJO'
    elif promedio < 221 :
        etiqueta = 'BAJO'
    elif promedio < 235 :
        etiqueta = 'MEDIO'
    elif promedio < 249 :
        etiqueta = 'ALTO'
    else :
        etiqueta = 'MUY ALTO'

    return etiqueta

# Calcular el promedio de los precios alto y bajo
def prom_precio_alto_bajo( precio_alto, precio_bajo ) :
    return float( precio_alto ) + float( precio_bajo ) / 2

# Abre el archivo y procesa la data
def abrir_archivo( nombre_archivo ) :
    data_completa = []
    data_separada = []

    with open( f'{ path }{ os .sep }{ nombre_archivo }', 'r' ) as file :

        for index, registro in enumerate( file .readlines() ) :
            if index > 0 :
                campos = registro .split( ',' )

                promedio = prom_precio_alto_bajo( campos[ 2 ], campos[ 3 ] )
                etiqueta = etiquetar( promedio )

                data_completa .append( campos )                                 # Toda la data separada
                data_separada .append( [ campos[ 0 ], promedio, etiqueta ] )    # Toda la data filtrada de salida

        return data_completa, data_separada


def solucion() :
    d_completa, d_separada = abrir_archivo( 'MSFT.csv' )
    d_salida = unir_data( d_separada )
    escribir_archivo( 'analisis_archivo.csv', d_salida )
    fecha_mayor, mayor, fecha_menor, menor = obtener_info( d_completa )

    return fecha_menor, menor, fecha_mayor, mayor

print( solucion() )