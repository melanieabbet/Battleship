from asset import Coordinate, CoordinateException, CoordinateOutOfBound, Content
import copy
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


    def get_coordinate(self, grid):
        while True:
            try:
                c = input("Entrez une coordonée de la grille:")
                if (b:=Coordinate(c)) and  grid[b]:
                    break
            except (CoordinateException,  CoordinateOutOfBound) as e:
                print(e)

        return b


    def get_coordinate_array(self, size, grid):
        #TODO cleanup + discution

        return_coor= []
        instruct = f"Entrez {size} coordonée qui ce suivent: {size-len(return_coor)} restantes"
        print(instruct) 
        i = 0
        while i<size:
            c = self.get_coordinate(grid)
            if grid[c].content==Content.BOAT:
                #restart
                return_coor= []
                i =0
                print(instruct)
            else:
                if return_coor:
                    test = copy.copy(return_coor)
                    test.append(c)
                    if Coordinate.is_suite(test):
                        return_coor.append(c)
                        i+=1
                    else:
                        #restart
                        return_coor= []
                        i =0
                        print(instruct)
                else:
                    return_coor.append(c)
                    i+=1

        return return_coor
    
    def clear(self):
        '''
        @brief function that clean the terminal
        '''
        os.system('cls' if os.name=='nt' else 'clear')
        print("")