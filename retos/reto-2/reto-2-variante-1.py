import random, time, numpy as np

def is_odd( num ):
    return num % 2 != 0

def matriz() :
    n_rows = 9
    n_columns = 9

    colums = [] * n_rows

    for i in range( n_rows ) :
        rows = [ 0 ] * n_columns
        colums .append( rows )

    return colums

def fill( matriz ) :
    k = 10
    for i in range( len( matriz ) ) :
        for j in range( len( matriz ) ) :
            matriz[ i ][ j ] = k
            k += 1

def show( matriz ) :
    print( '' )
    for i in range( len( matriz ) ) :
        for j in range( len( matriz[ 0 ] ) ) :
            print( matriz[ i ][ j ], end='  ')

        if i < len( matriz ) :
            print( '' )

    print( '' )

def odd_fields( matriz ):
    #print( '' )
    for i in range( len( matriz ) ) :
        for j in range( len( matriz[ 0 ] ) ) :

            if is_odd( i + j ) :
                pass
                #print( matriz[ i ][ j ], end='  ')
            else :
                matriz[ i ][ j ] = 'xx'
                #print( matriz[ i ][ j ], end='  ')

        if i < len( matriz ) :
            pass
            #print( '' )

    #print( '' )

    return matriz

def upper_secondary_diagonal( matriz ):
    print( '' )
    for i in range( len( matriz ) ) :
        for j in range( len( matriz[ 0 ] ) - i ) :
            print( matriz[ i ][ j ], end='  ')

        if i < len( matriz ) :
            print( '' )

    print( '' )

def of_usd( matriz ) :
    print( '' )
    for i in range( len( matriz ) ) :
        for j in range( len( matriz[ 0 ] ) - i ) :

            if is_odd( i + j ) :
                #pass
                print( matriz[ i ][ j ], end='  ')
            #else :
                #matriz[ i ][ j ] = 'xx'
                #print( matriz[ i ][ j ], end='  ')

        if i < len( matriz ) :
            print( '' )

    print( '' )

def of_usd_less( matriz ) :
    print( '' )
    coords = []
    minor = matriz[ 0 ][ 1 ]

    for i in range( len( matriz ) ) :
        for j in range( len( matriz[ 0 ] ) - i ) :

            if is_odd( i + j ) :

                if matriz[ i ][ j ] == minor :
                    coords .append( ( i, j ) )
                    minor = matriz[ i ][ j ]
                elif matriz[ i ][ j ] < minor :
                    coords .clear()
                    coords .append( ( i, j ) )
                    minor = matriz[ i ][ j ]

                print( matriz[ i ][ j ], end='  ')

        if i < len( matriz ) :
            print( '' )

    print( '' )
    print( minor, coords )

# Pruebas con una matriz de datos auto generada
#m1 = matriz()
#print( m1 )
#show( m1 )
#fill( m1 )
#m1[3][2] = 5
#m1[4][3] = 5
#show( m1 )
#m1_odd = odd_fields( m1 )
#show( m1_odd )
#upper_secondary_diagonal( m1 )

#of_usd_less( m1 )

# Matriz del Codigo
matriz_entrada = np.array([
    [89, 13, 23, 72],
    [29, 11, 81, 62],
    [27, 26, 88, 33],
    [5, 78, 11, 11]
])

# Matriz del PDF
matriz_entrada_pdf = np.array([
    [89, 5, 23, 72],
    [51, 5, 81, 62],
    [27, 26, 88, 5],
    [ 5, 78, 11, 11]
])

# En las siguientes funciones cambia el nombre de las matrices y prueba con funciona correctamente
print( '' )
print( 'Matriz del PDF' .center( 40, '-' ) )
show( matriz_entrada_pdf )          # Muestra matriz PDF
of_usd_less( matriz_entrada_pdf )   # Muestra datos segmentados y resultado

print( 'Matriz del Original' .center( 40, '-' ) )
show( matriz_entrada )              # Muestra matriz original
of_usd_less( matriz_entrada )       # Muestra datos segmentados y resultado