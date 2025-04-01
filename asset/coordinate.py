class Coordinate:

    def __init__(self, column, row):
        '''
        @brief constructor of coordinate class

        @detail this class with the adressing of cell inside the Grid
        '''
        #TODO should accept number or letter as column
        self.column = Coordinate.set_column(column)
        self.row = row
        
    @staticmethod
    def set_column(index):
        '''
        @brief method that give the column "name" from the column index

        @detail static method that generate a column name from the index number

        @param column index

        @return string of column name
        '''
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #get the size of the string
        size = 1
        while 26**size<index:
            size+=1
        column =""

        #base convertion
        while(size):
            column+=(alphabet[index%(26**size)])
            size -=1

        return column



    def __hash__(self):
        '''method that return an id '''
        return hash((self.column, self.row))



    def __eq__(self, coordinate):
        '''
        @override methode that can test if two Coordinate are the same'''

        return self.column == coordinate.column and self.row == coordinate.row