#TDD
'''
#Instance creation
>>> a = Coordinate("a2")
>>> b = Coordinate("A2")
>>> c = Coordinate(0,1)
>>> d = Coordinate("#3") # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
Exception: ('#3',) can not creat a Coordinate

>>> d = Coordinate("3a") # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
Exception: ('#3',) can not creat a Coordinate

#repr
>>> print(a)
A2

#Comparaison
>>> a==b==c
True
>>> e = Coordinate(0,0)
>>> print(e)
A1
>>> a==e
False
>>> a<e
False
>>> e<a
True

#test of sorting and key
>>> a = Coordinate("G5")
>>> b = Coordinate("H5")
>>> c = Coordinate("B7")
>>> test_list = [c,a,b]
>>> print(test_list)
[B7, G5, H5]
>>> test_list.sort()
>>> print(test_list)
[G5, H5, B7]

'''

import re

class Coordinate:

    def __init__(self, *args):
        '''
        @brief constructor of coordinate class

        @detail the constructor only accept a string or two init number
                Otherwise it raise an Exception Error
                If a string is passed, it is test if valid.
                    -> if not it rais an error
                If two number ar passed they are converted (row 0 = row 1)

        @param can be a string or two number
        '''
        e = Exception(f"{args} can not creat a Coordinate")

        if len(args)==1:
            #Args must be a string
            if out:= Coordinate.coordinate_from_string(args[0]):
                column, row = out #unpack
                self.column = column
                self.row = row
            else:
                raise e


        elif len(args)==2 and all(isinstance(i, int) for i in args):
            # Can be number
            column = args[0]
            row = args[1]

            self.column = Coordinate.set_column(column)
            self.row = row+1
        else:
            raise e

    # ---------------------------------------------
    # Special mehodes
    # ---------------------------------------------

    def __repr__(self):
        '''
        @ brief special methode to rpint the class instance
        '''
        return f"{self.column}{self.row}"
    

    def __hash__(self):
        '''
        @brief define so the class can be a dictionary key
        '''
        return hash((self.column, self.row))
    
    
    def __lt__(self, other):
        '''
        @brief comparaison methode to sort
        '''
        if self.row == other.row:
            return self.column<other.column
        else:
            return self.row<other.row
        

    def __eq__(self, coordinate):
        '''
        @brief special methode to test the equality between two instance
        '''
        return self.column == coordinate.column and self.row == coordinate.row
    

    
    @staticmethod
    def is_aligned(a, b):
        '''
        @brief return true if both coordinate ar aligned
        '''
        if isinstance(a, Coordinate) and isinstance(b, Coordinate):
            if a.column==b.column or a.row == b.row:
                return True
        return False

    
    @staticmethod
    def coordinate_from_string(test_string):
        '''
        @brief return the column and row if the string respect the format

        @detail convert with regex the input string as a column and row formated for the class creation
                If the string do not mach an expected format (lettre+number)
                    -> The value None is returned
        '''
        if isinstance(test_string, str):
            pattern = r"^([A-Za-z]+)(\d+)$" #made with chatGpt
            match = re.match(pattern, test_string)
            if match:
                column = match.group(1).upper()
                row = int(match.group(2))
                return column, row
            
        return None


    @staticmethod
    def set_column(index):
        '''
        @brief method that give the column "name" from the column index

        @detail base 26 convertion of the index number

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




if __name__ == '__main__':

    import doctest
    doctest.testmod()