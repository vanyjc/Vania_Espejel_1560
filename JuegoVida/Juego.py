from SoporteVida import SoporteVida

class Juego:

    def __init__( self, rows, cols ):
        self.__panel = SoporteVida( rows, cols )
        self.__contador = 1

    def configure( self, inicial, generaciones ):
        self.__panel.configure( inicial, generaciones )

    def to_string( self ):
        self.__panel.to_string()
    
    def get_gens( self ):
        return self.__panel.get_gens()
    
    def reglas( self, row, col ):
        vecinos = self.__panel.get_alive_neighbors( row, col )
        if( self.__panel.is_alive_cell( row, col )):
            if( vecinos == 2 or vecinos == 3):
                return True
            else:
                return False
        else:
            if( vecinos == 3):
                return True
            else:
                return False

    def aplicarReglas( self ):
        nuevaConfig = []
        for i in range( self.__panel.get_num_rows() ):
            for j in range( self.__panel.get_num_cols() ):
                if(self.reglas( i, j )):
                    coordenada = [i, j]
                    nuevaConfig.append(coordenada)
        return nuevaConfig

    def iterarGeneracion( self ):
        if self.__panel.get_gens() > 1 :
            self.__contador += 1
            arregloNuevaGen = self.aplicarReglas()
            self.__panel.set_gens( self.__panel.get_gens() -1 )
            self.__panel.configure( arregloNuevaGen,  self.__panel.get_gens())
            print(f"-------- {self.__contador}° Generación --------")
            self.to_string()
            self.iterarGeneracion()
    
def main():
    partida = Juego( 5, 5 )
    partida.configure( [[1,2],[2,1],[2,2],[2,3]], 10 )
    print("-------- Poblacion inicial/1° Generación --------")
    partida.to_string()
    partida.iterarGeneracion()

main()
