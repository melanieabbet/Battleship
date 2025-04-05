from asset import Coordinate, CoordinateException, CoordinateOutOfBound, Content
import copy
import time
import os

class Terminal:

    def __init__(self):
        pass

    def get_role(self):
        while True:
            s = input("Role?:")
            if s in ["g", "h"]:
                return s
    
    def get_ip(self):
        while True:
            s = input("ip:")
            return s


    def get_coordinate(self, grid, message=None, print_grid = True):
        while True:
            try:
                c = input("Entrez une coordonée de la grille:")
                if (b:=Coordinate(c)) and  grid[b]:
                    break
            except (CoordinateException,  CoordinateOutOfBound) as e:
                self.message(e)
                time.sleep(2)
                if print_grid:
                    self.print_grid(grid)
                if message:
                    self.message(message, clear=False)

        return b


    def get_coordinate_array(self, size, grid):
        #TODO cleanup + discution

        return_coor= []
        i = 0
        while i<size:
            instruct = f"Entrez {size} coordonée qui ce suivent: {size-len(return_coor)} restantes"

            self.print_grid(grid)
            self.message(instruct, clear=False) 

            c = self.get_coordinate(grid, message=instruct)
            if grid[c].content==Content.BOAT:
                #restart
                return_coor= []
                i =0
                self.message(f"There is already a Boat at this ccordinate: {c}")
                time.sleep("1")
            else:
                if return_coor:
                    test = copy.copy(return_coor)
                    test.append(c)

                    if Coordinate.is_suite(test):
                        return_coor.append(c)
                        i+=1
                    else:
                        #restart
                        self.message(f"The cordinate, {c} is not alligned with {return_coor}")
                        time.sleep(2)
                        return_coor= []
                        i =0
                else:
                    return_coor.append(c)
                    i+=1

        return return_coor
    
    def message(self, string, clear=True):
        if clear:
            self.clear()
        print(string)

    def print_grid(self, grid, clear=True):
        if clear:
            self.clear()
        print(grid)
        
    
    def clear(self):
        '''
        @brief function that clean the terminal
        '''
        os.system('cls' if os.name=='nt' else 'clear')
        print("")