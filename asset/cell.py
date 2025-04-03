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
    def __init__(self, content=Content.EMPTY):
        # self.address = address
        self.content = content


    def __str__(self):
        '''override methode to print a cell'''
        if self.content == Content.EMPTY:
            return f" · "
        elif self.content == Content.BOAT:
            return f" □ "
        elif self.content == Content.HIT:
            return f" X "
        elif self.content == Content.MISS:
            return f" O "
    
    def set_boat(self):
        self.content = Content.BOAT

    def set_hit(self):
        self.content = Content.HIT

        
    
    
    
