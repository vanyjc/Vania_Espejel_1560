# EL JUEGO DE LA VIDA
'''
- Del tipo zero_player
- Creado por john H. Conway(1970)
- Ejemplifica, el acenso, caida y alternancia de seres vivos
'''
#Reglas
'''
1. Si una celula esta viva y tiene dos o tres vecinos vivos,
la celula sobrevive a la siguiente generacion.
Los vecinos son las 8 celulas que la rodean inmediatamente,
tanto en vertical, horizontal y diagonal

2. Una celula que no tiene vecinos vivos o que tiene
solamente un vecino vivo muere por soledad
para la sig. generacion

3. Una celula viva que tiene 4 o mas vecinos vivos,
muere por sobrepoblacion para la siguiente generacion

4. Una celula muerte con exactamente 3 vecinos vivos
resulta en un nacimiento cuya vida iniciara en la
sig. generacion. Todas las celulas muertas restantes,
se mantienen muertas en la sig generacion
'''
from Array2D import Array2D

class SoporteVida:
    def __init__ ( self , rows , cols ):
        self.__rows = rows
        self.__cols = cols
        self.__grid = Array2D( rows , cols )
        self.__grid.clearing(0)

    def get_num_rows( self ):
        return self.__rows

    def get_num_cols( self ):
        return self.__cols

    def get_gens( self ):
        return self.__gens

    def set_gens( self, generacion ):
        self.__gens = generacion

    def configure( self , inicial , generaciones ):
        '''inicial es una lista de la forma:
        inicial = [[1,2],[2,2],[2,3],[3,1]]'''
        self.__grid.clearing(0)
        self.__gens = generaciones
        for cell in inicial:
            self.__grid.set_item(cell[0],cell[1],1)

    def clear_cell(self , row , col):
        self.__grid.set_item(row,col,0)

    def set_cell(self , row , col):
        self.__grid.set_item(row,col,1)

    def is_alive_cell(self , row , col):
        if self.__grid.get_item(row,col)==1:
            return True
        else:
            return False
        
    def get_alive_neighbors( self, row,col ):
        c = 0
        x = row - 1
        y = col - 1
        for i in range(3):
            for j in range(3):
                if(0 <= x and x <= (self.get_num_rows() - 1) and 0 <= y and y <= (self.get_num_cols() - 1)):
                    if( self.is_alive_cell( x, y )):
                        c += 1
                x += 1
            x = row - 1
            y += 1
        if(self.is_alive_cell( row, col )):
            c -= 1
        return c
        
        
    def to_string( self ):
        self.__grid.to_string()

'''
def main():
    
    juego = SoporteVida(5 , 5)
    juego.to_string()
    juego.configure([[1,2],[2,1],[2,2],[2,3]], 5)
    print("Población inicial:")
    juego.to_string()
    juego.get_alive_neighbors(2,2)
    print(juego.get_alive_neighbors(2,2))
    
main()
'''

