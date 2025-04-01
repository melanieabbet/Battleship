'''execution module to test as a playground'''

from asset import Grid
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
    print(grid)