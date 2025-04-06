

from asset import Coordinate, CoordinateException, CoordinateOutOfBound, Content
from network import NetRole

import copy
import time
import os
import socket

class Terminal:

    TIME_ERROR = 2 

    def __init__(self):
        pass

    def get_role(self):
        '''
        @brief input function for player role

        @details player role can only be "host" or "join"
        '''
        while True:
            self.message("Join Game")
            self.message("Host Game", clear=False)


            s = input("Select: ")
            s = s.casefold()
            if s == "join":
                return NetRole.GUEST
            elif s == "host":
                return NetRole.HOST
            else:
                self.message("Enter Join or Host")
                time.sleep(self.TIME_ERROR) 

    
        
    def get_host_ip(self):
        while True:
            s = input("Entrez l'IP de l'hôte (ex: 192.168.1.42): ").strip()
            try:
                socket.inet_aton(s)  # Vérifie si c'est format IPv4
                return s
            except socket.error:
                print("IP invalide. Veuillez réessayer.")


    def get_coordinate(self, *grids, message=None, print_grid = True):
        '''
        @brief input method to get a grid coordinate
        
        @details Ask for a coordinate and can print the grid on top

        @param grid Grid object where the enter coordinate must exist

        @param message message to print befor the input (Default None)

        @param print_grid if enabled the passed grid will be print before the input
        '''
        while True:

            self.clear()
            if print_grid:
                grid_string = self.print_grid(grids)
                self.message(grid_string)
            if message:
                self.message(message, clear=False)
            
            try:
                c = input("Entrez une coordonée de la grille:")
                if (coor:=Coordinate(c)) and  grids[0][coor]:
                    break
            except (CoordinateException,  CoordinateOutOfBound) as e:
                if type(e)==CoordinateException:
                    self.message("Coordinate are written as the following example: A2")
                else:
                    self.clear()
                self.message(e, clear=False)
                time.sleep(2)           
        return coor


    def get_coordinate_array(self, size, grid):
        '''
        @brief input method to get a list of coordinates that follow

        @details method use to place the boat on the grid
                the boat can not be placed on top of other boat
                the boat can not go beyond the grid
                the boat must be aligned vertically or horizontally
        
        @param expect size of the list
        
        @param grid Grid object where the enter coordinate must exist
        '''

        return_coor= []
        i = 0
        while i<size:
            instruct = f"Enter {size} coordinates that folow: {size-len(return_coor)} remaining"
            grid_string = self.print_grid(grid)
            message = grid_string + "\n" + instruct
            if return_coor:
                return_coor.sort()
                message = message + "\n" + repr(return_coor)

            #entry for one coordinate
            c = self.get_coordinate(grid, message=message, print_grid=False)

            #test entry
            if grid[c].content==Content.BOAT:
                #restart
                return_coor= []
                i =0
                self.message(f"There is already a Boat at this ccordinate: {c}")
                time.sleep(self.TIME_ERROR)
            else:
                if return_coor:
                    #test if alligned and following
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
                    #first coordinate
                    return_coor.append(c)
                    i+=1

        return return_coor
    
    def message(self, string, clear=True):
        '''
        @breif output method to print a string in the terminal
        
        @param string string to print
        
        @param clear if enabled will clear the terminal befor ptint
        '''
        if clear:
            self.clear()
        print(string)

    def print_grid(self, *grid_list):
        '''
        @brief output method used to print grid side by side

        @details do not print in terminal but return a string ready to be printed

        @note   TODO probably a better way to do it (too much loop)
                TODO add name of player on top
        '''
        SPACING = 5
        space_string =" "*SPACING



        nb_of_grid = len(grid_list)
        if nb_of_grid>1:
            grids = [None] * nb_of_grid

            for index,grid in enumerate(grid_list):
                grids[index] = repr(grid).split("\n")

            return_string=""
            i =0
            while i<len(grids[0]):
                for grid  in grids:
                    #get same line in each grid
                    line = grid[i]
                    return_string+=line
                    return_string += space_string
                #remove last spacing and add back line
                return_string = return_string[:-SPACING]
                return_string+= "\n"
                i+=1

            #self.message(return_string, clear=False)
            return return_string

        else:
            grid = grid_list[0]
            #self.message(repr(grid), clear=False)
            return repr(grid)

        
    
    def clear(self):
        '''
        @brief method that clean the terminal

        @note source: https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
        '''
        os.system('cls' if os.name=='nt' else 'clear')
        print("")



if __name__ == "__main__":
    import doctest
    doctest.testmod()