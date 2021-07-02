from Cliente import Cliente

# ! Obtiene los nombres de las listas de cliente
def obtener_lista_nombres( lista_nombres ) :
    nombres = []

    for cliente in lista_nombres :
        nombres .append( cliente .nombre )

    return nombres

# ! Obtiene la edad minima de acuerdo al tipo de transaccion
def obtener_edad_minima( cliente, tipo_transaccion, edad_minima ) :

    if cliente .transaccion == tipo_transaccion :
        if edad_minima == -1 :
            edad_minima = cliente .edad
        if cliente .edad < edad_minima :
            edad_minima = cliente .edad

    return edad_minima

# ! Obtiene clientes de las filas caja e informacion. Ademas calcula el total de consignaciones y retiros
def obtener_info_filas( cola_general ) :
    fila_caja = []          # Clientes
    fila_info = []          # Clientes
    total_retiros = 0
    total_consignaciones = 0

    # ! Verificando la fila de interes
    for cliente in cola_general:

        # ! Separa los clientes por fila de acuerdo al interes
        if ( cliente .fila_interes == "caja" ) :                    # ? Fila de Caja (Retiro, Consignacion)
            fila_caja.append( cliente )

            if ( cliente .transaccion == "retirar" ):               # ! Suma total de todos los retiros a realizar
                total_retiros += cliente .cantidad_retirar

            elif( cliente .transaccion == "consignar" ):            # ! Suma total de todos las consignaciones a realizar
                total_consignaciones += cliente .cantidad_consignar

        elif ( cliente .fila_interes == "info" ) :                  # ? Fila de Informacion
            fila_info.append( cliente )

    return fila_caja, fila_info, total_retiros, total_consignaciones

def sede_bancaria( cola_general ):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

    edad_minima_info = edad_minima_retiro = edad_minima_consignacion = -1        # Establecemos la edad por defecto como la edad del primer cliente en la lista (Comparar)

    list_caja, list_info, suma_retiros, suma_consignaciones = obtener_info_filas( cola_general )

    # ! Verifica la edad minima del cliente que esta en la fila de caja
    for cliente in list_caja :
        edad_minima_retiro = obtener_edad_minima( cliente, 'retirar', edad_minima_retiro )                  # ! Edad minima del cliente que retira (Fila caja)
        edad_minima_consignacion = obtener_edad_minima( cliente, 'consignar', edad_minima_consignacion )    # ! Edad minima del cliente que consigna (Fila caja)

    # ! Verifica la edad minima del cliente que esta en la fila de informacion
    for cliente in list_info :
        edad_minima_info = obtener_edad_minima( cliente, None, edad_minima_info )                         # ! Edad minima del cliente que no retira, ni consigna (Fila Informacion)

    cola_caja = obtener_lista_nombres( list_caja )
    cola_info = obtener_lista_nombres( list_info )

    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

# ! Inicio de ejecucion del programa
if __name__ == '__main__' :
    cola_general = [
        # nombre, edad, dinero, fila_interes, transaccion, cantidad_retirar, cantidad_consignar
        Cliente( 'Juan', 43, 11000, 'info', None, 0, 0 ),
        Cliente( 'Elisa', 44, 15000, 'caja', 'consignar', 0, 10000 ),
        Cliente( 'Luisa', 26, 22000, 'caja', 'retirar', 2000, 0 ),
        Cliente( 'Carlos', 43, 44000, 'info', None, 0, 0 ),
        Cliente( 'Juliana', 19, 16000, 'caja', 'consignar', 0, 3200 ),
        Cliente( 'Maria', 34, 19000, 'caja', 'consignar', 0, 4000 ),
        Cliente( 'Sandy', 23, 23000, 'caja', 'retirar', 2000, 0 ),
        Cliente( 'Ana', 26, 34000, 'caja', 'retirar', 2000, 0 ),
    ]

    cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion = sede_bancaria( cola_general )

    print( 'cola_caja:', cola_caja )
    print( 'cola_info:', cola_info )
    print( 'suma_retiros:', suma_retiros )
    print( 'suma_consignaciones:', suma_consignaciones )
    print( 'edad_minima_retiro:', edad_minima_retiro )
    print( 'edad_minima_info:', edad_minima_info )
    print( 'edad_minima_consignacion:', edad_minima_consignacion )