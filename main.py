'''execution module to test as a playground'''

from asset import Grid
from asset import Boat
from asset import Coordinate
import os

def cls():
    '''
    @brief function that clean the terminal
    '''
    os.system('cls' if os.name=='nt' else 'clear')
    print("")




if __name__ =="__main__":

    cls()
    
    grid = Grid(9)
    # print(grid)
    boat = Boat([grid[Coordinate("G5")], grid[Coordinate("F5")], grid[Coordinate("E5")]])
    cls()
    print(grid)

    grid.shoot_at(Coordinate("B1"))
    
    cls()
    print(grid)
    
