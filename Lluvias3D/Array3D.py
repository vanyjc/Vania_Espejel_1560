class Array3D:
    def __init__( self , rows , cols , depth):
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        self.__data = []
        for d in range(self.__depth): #2
            aux = []
            for r in range(self.__rows): #3
                aux2 = []
                for c in range(self.__cols): #4
                    aux2.append(None)
                aux.append(aux2)
            self.__data.append(aux)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_num_depth(self):
        return self.__depth

    def set_item(self,r,c,d,value):
        self.__data[d][r][c] = value

    def get_item(self,r,c,d):
        return self.__data[d][r][c]

    def clearing(self, value):
        for d in range(self.__depth):
            for r in range(self.__rows):
                for c in range(self.__cols):
                    self.set_item(r,c,d,value)


    def to_string(self):
        print(self.__data)

'''
def main():
    a3d = Array3D(4,3,2)
    a3d.to_string()
    print(a3d.get_num_rows())
    a3d.clearing(0)
    a3d.to_string()
    print(a3d.get_item(0,0,0))

main()

'''