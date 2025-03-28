'''
This file deal with the cell assset

the Cell asset is the base componenet of the Grid

The cell has an adddress and a content

The adress is the location of the cell inside the Grid

the content is what's inside the Cell

Both of thos concept are a class
'''

from enum import Enum

class Content(Enum):
    '''
    @brief enum class for the cell content
    
    @detail A cell can have:
        Water -> EMPTY
        Boat -> BOAT
        Damaged boat (localy)-> HIT
        Missed previous try -> MISS
    '''
    EMPTY = 1
    BOAT = 2
    HIT = 3
    MISS = 4




class Cell:
    def __init__(self, address, content=Content.EMPTY):
        self.address = address
        self.content = content


    def __str__(self):
        '''override methode to print a cell'''
        if self.content == Content.EMPTY:
            return f"[ ]"
        elif self.content == Content.BOAT:
            return f"[B]"
        elif self.content == Content.HIT:
            return f"[X]"
        elif self.content == Content.MISS:
            return f"[O]"


class Address:

    def __init__(self, column, row):
        '''The adress is a grid coordinate

        '''
        self.column = Address.set_column(column)
        self.row = row+1
        
    @staticmethod
    def set_column(index):
        '''
        @brief method that give the column "name" from the column index

        @detail static method that generate a column name from the index number

        @param column index

        @return string of column name
        '''
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #TODO error for size too large
        
        if mult:=index//26:
            index -= 26*mult
            column = alphabet[mult]+alphabet[index%26]
        else:
            column= alphabet[index%26]

        return column
    
    
    
