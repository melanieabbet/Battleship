'''
@file terminalHandler.py

@brief file that hold the Terminal class and all the logic attached
'''

from asset import Coordinate, CoordinateException, CoordinateOutOfBound, Content
from network import NetRole

import copy
import time
import os
import socket

class Terminal:
    '''
    @brief class that is used to get and diplay the informations inside the user terminal
    '''

    TIME_ERROR = 2 

    def __init__(self):
        pass

    def get_role(self):
        '''
        @brief input function for player role

        @details player role can only be "host" or "join"

        @return NetRole with the role selcted by the user
        '''
        while True:
            s = input("Enter your role (Join or Host): ")
            s = s.casefold()
            if s == "join":
                return NetRole.GUEST
            elif s == "host":
                return NetRole.HOST
            else:
                self.message("Enter Join or Host")
                time.sleep(self.TIME_ERROR) 

    
        
    def get_host_ip(self):
        '''
        @brief input method to get the IP address of the host
        
        @details only used by a "Client" role to be able to join the Host
                check if the input complied with the ipv4 address format

        @return string with ipv4 format
        '''
        while True:
            self.clear()
            s = input("Enter the host IP Address (ex: 192.168.1.42): ").strip()
            try:
                socket.inet_aton(s)  # Check if it's an IPv4
                return s
            except socket.error:
                print("Invalid IP address. Please try again.")


    def get_coordinate(self, *grids, message=None):
        '''
        @brief input method to get a grid coordinate
        
        @details Ask for a coordinate and can display the grid and some passed string on top

        @param grid Grid object where the enter coordinate must exist

        @param message message to display in terminal before the input (Default None)

        @param print_grid if enabled the passed grid will be print before the input
        '''
        while True:

            self.clear()
            if message:
                self.message(message, clear=False)
            try:
                c = input("Enter a grid coordinate:")
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
            instruct = f"Enter {size} coordinates that follow: {size-len(return_coor)} remaining"
            grid_string = self.print_named_grid(("Set your boat",grid))
            message = grid_string + "\n" + instruct
            if return_coor:
                return_coor.sort()
                message = message + "\n" + repr(return_coor)

            #entry for one coordinate
            c = self.get_coordinate(grid, message=message)

            #test entry
            if grid[c].content==Content.BOAT:
                #restart
                return_coor= []
                i =0
                self.message(f"There is already a boat at this coordinate: {c}")
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
                        self.message(f"The coordinate, {c} is not alligned with {return_coor}")
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
        @brief output method to print a string in the terminal
        
        @param string string to display in terminal
        
        @param clear if enabled will clear the terminal before print
        '''
        if clear:
            self.clear()
        print(string)

    def print_named_grid(self, *named_grids):
        '''
        @brief output method used to print grid side by side

        @details do not print in terminal but return a string ready to be printed

        @note centrer un text: https://www.w3schools.com/python/ref_string_center.asp
   
        '''
        SPACING = 5
        space_string = " " * SPACING

        # use repr(grid) and split each grid in line
        lines_per_grid = [repr(grid).split("\n") for _, grid in named_grids]
        grid_widths = len(lines_per_grid[0][0]) # Same grids so same lenght

        # Add name
        header = space_string.join(name.center(grid_widths) for name, _ in named_grids)
        output = header + "\n"

        # Construct final text
        i = 0
        while i < len(lines_per_grid[0]):  # Same grids so same height
            line = space_string.join(grid[i] for grid in lines_per_grid) # join different grids line together
            output += line + "\n"
            i += 1 

        return output    
    
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