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

        if len(coor_array)== self.size:
            for index, coor in enumerate(coor_array):
                self.cells[index] = grid[coor]
                self.cells[index].content = Content.BOAT

            self.is_alive = True
    
    # def set_coordinate(self, a, b):
    #     if coor_list:= Coordinate.get_coordinate_array(a, b)== len(self):
    #         for index, coor in enumerate(coor_list):
    #             self.coordinates[index]=coor



