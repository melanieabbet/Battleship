'''
@file boat.py

@brief file that hold the Boat Class

'''
from .coordinate import Coordinate


class Boat:

    def __init__(self, cell_array):
        #creat list of empty coordinate
        self.cells = cell_array

        for cell in self.cells:
            cell.set_boat()

        self.is_alive = False
    
    def __sizeof__(self):
        return len(self.cells)
    
    # def set_coordinate(self, a, b):
    #     if coor_list:= Coordinate.get_coordinate_array(a, b)== len(self):
    #         for index, coor in enumerate(coor_list):
    #             self.coordinates[index]=coor



