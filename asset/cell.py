'''
@file cell.py 

@brief This file deal with the cell assset
'''

from enum import Enum

class Content(Enum):
    '''
    @brief enum class for the cell content
    
    @details A cell can have:
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
    '''
    @brief the Cell asset is the base componenet of the Grid
    '''
    def __init__(self, content=Content.EMPTY):
        '''
        @brief class constructo'''
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
        '''
        @brief Set the cell content as a boat
        '''
        self.content = Content.BOAT

    def set_hit(self):
        '''
        @brief Set the cell content as a hit boat
        '''
        self.content = Content.HIT

        
    
    
    
