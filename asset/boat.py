'''
@file boat.py

@brief file that hold the Boat Class

'''
from .coordinate import Coordinate
from.cell import Cell,Content
import random

class Boat:

    def __init__(self, size):
        self.size = size
        self.cells = [Cell(Content.BOAT)]*size
        self.is_alive = False
    
    def __sizeof__(self):
        return self.size
    
    def set_boat(self, coor_array, grid):
        '''
        @brief set the cells
        
        @details set the cell as the cell of the grid linked with the coordinate passed
        '''

        if len(coor_array)== self.size:
            self.corr_array = coor_array
            for index, coor in enumerate(coor_array):
                self.cells[index] = grid[coor]
                self.cells[index].content = Content.BOAT

            self.is_alive = True
    
    def health(self):
        '''
        @return the boat HP

        @note maybe redo with the lens of dictionary 
        and remove the cell each time it is hit
        '''
        hp = 0
        for cell in self.cells:
            if cell.content == Content.BOAT:
                hp +=1
        return hp
    
    def sink(self, grid):
        '''
        @brief call to kill the Boat

        @return the coordinates of the sinked boat (as a str)
        '''
        return_str =""
        for coor in self.corr_array:
            grid[coor].set_sink()
            return_str += f"{repr(coor)},"
        return_str = return_str[:-1] #remove lat coma
        return return_str
    
    def __lt__(self, other):
        '''
        @brief less than, so boat can be sorted

        @note the weakest (hp) is the biggest
                -> so it will be at the end of the list
        '''
        if not isinstance(other, Boat):
            return False
        else:
            if self.health()<other.health():
                return False
            else:
                return True



