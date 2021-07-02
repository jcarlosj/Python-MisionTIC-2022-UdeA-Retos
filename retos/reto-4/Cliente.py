class Cliente :

    def __init__( self, nombre, edad, dinero, fila_interes, transaccion, cantidad_retirar, cantidad_consignar ) :
        self .nombre = nombre
        self .edad = edad
        self .dinero = dinero
        self .fila_interes = fila_interes
        self .transaccion = transaccion
        self .cantidad_retirar = cantidad_retirar
        self .cantidad_consignar = cantidad_consignar

    # Metodo Magico (Dunder)
    def __str__( self ) :
        return f' > { self. nombre }, { self. edad }, { self. dinero }, { self. fila_interes }, { self. transaccion }, { self. cantidad_retirar }, { self. cantidad_consignar }'
