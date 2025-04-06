#TDD
'''
#Instance creation
>>> a = Coordinate("a2")
>>> b = Coordinate("A2")
>>> c = Coordinate(0,1)
>>> d = Coordinate("#3") # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
CoordinateException: ('#3',) Can not creat a Coordinate with this input

>>> d = Coordinate("3a") # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
[...]
CoordinateException: ('#3',) Can not creat a Coordinate with this input

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

#convertion
>>> print(Coordinate.index_from_letter("B"))
1
>>> print(Coordinate.index_from_letter("AA"))
26
>>> print(Coordinate.letter_from_index(26))
AA

#test outofbound and navigate
e = Coordinate(0,0)
>>> print(e)
A1
>>> print(e.right())
B1
>>> print(e.down())
A2
>>> e.up()
Traceback (most recent call last):
[...]
CoordinateOutOfBound: Coordinate not in the Grid
>>> e.left()
Traceback (most recent call last):
[...]
CoordinateOutOfBound: Coordinate not in the Grid

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
        e = CoordinateException(f"{args} Can not creat a Coordinate with this input")

        if len(args)==1:
            #Args must be a string
            if out:= self.coordinate_from_string(args[0]):
                column, row = out #unpack
                self.column = column
                self.row = row
                self.check()
            else:
                raise e


        elif len(args)==2 and all(isinstance(i, int) for i in args):
            # Can be number
            column = args[0]
            row = args[1]

            self.column = column
            self.row = row
            self.check()
        else:
            raise e

    
    def coordinate_from_string(self,test_string):
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
                column = Coordinate.index_from_letter(column)
                row = int(match.group(2))
                return column, row-1
            
        return None
    
        
    def right(self):
        column = self.column+1
        row = self.row
        return Coordinate(column, row)
  
    def left(self):
        column = self.column-1
        row = self.row
        return Coordinate(column, row)
    
    def up(self):
        column = self.column
        row = self.row-1
        return Coordinate(column, row)
    
    def down(self):
        column = self.column
        row = self.row+1
        return Coordinate(column, row)
    
    def check(self):
        '''
        @brief check if the coordinate is valid
        '''
        if self.column<0 or self.row<0:
            raise CoordinateOutOfBound("Coordinate not in the Grid")

    # ---------------------------------------------
    # Special mehodes
    # ---------------------------------------------
    def __repr__(self):
        '''
        @ brief special methode to rpint the class instance
        '''
        return f"{Coordinate.letter_from_index(self.column)}{self.row+1}"
    

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
    def is_suite(*args):
        '''
        @brief return true if both coordinate ar aligned
        '''
        try:
            test_list = list(*args)
            test_list.sort()

            if test_list[0].right()==test_list[1]:
                #list is horizontaly aligned
                return all([test_list[i].right()==test_list[i+1] for i in range(len(test_list)-1)])
            
            elif test_list[0].down()==test_list[1]:
                return all([test_list[i].down()==test_list[i+1] for i in range(len(test_list)-1)])
            else:
                return False
        except:
            return False


    @staticmethod
    def letter_from_index(index):
        '''
        @brief method that give the column "name" from the column index

        @detail base 26 convertion of the index number

        @param column index

        @return string of column name
        '''
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        string = ""
        while index >= 0:
            string = alphabet[index % 26] + string 
            index = (index // 26) - 1
        
        return string
    
    
    @staticmethod
    def index_from_letter(string):

        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        total = 0
        for index, char in enumerate(reversed(string)):
            value = alphabet.index(char) +1
            total += value * (26 ** index)
        return total - 1

# ---------------------------------------------
# Specific Exception
# ---------------------------------------------
class CoordinateException(Exception):
    pass

class CoordinateOutOfBound(Exception):
    pass
    

if __name__ == '__main__':
    # a = Coordinate(0,0)
    # b = a.right()
    # c = a.down()
    # d = a.up()
    import doctest
    doctest.testmod()