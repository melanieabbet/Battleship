'''
File with the grid Module

The grid is used as the game board
'''
from .cell import Cell, Content
from .coordinate import Coordinate, CoordinateOutOfBound

class Grid:

    def __init__(self, size):
        self.size = size

        '''A grid is a dictionary with Coordinate paired with the maching Cell'''
        self.grid = {}
        for c in range(size):
            for r in range(size):
                coor = Coordinate(c,r)
                cell = Cell()
                self.grid.update({coor:cell})
    
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, key):

        if key in self.grid.keys():   
            return self.grid[key]
        else:
            raise CoordinateOutOfBound("Item not in grid")

    
    def __iter__(self):
        #creat sorted list of cell from address
        self.grid.sorted()


    
    def __repr__(self):
        '''
        @brief override methode to print the grid
        
        @detail method that is used to print the grid with the cell content
                it call the __repr__ method of the Cell inside self.cells
        '''
        #TODO error of display if size >9

        return_string = "[\]"
        #Header
        return_string+= "".join([f"[{Coordinate.letter_from_index(i)}]" for i in range(self.size)])
        return_string+="\n"

        row =1
        #iterate inside the self.grid dictionary sorted by coordinate
        for i, key in enumerate(sorted(self.grid.keys())):
            #row labels
            if not i%self.size:
                return_string+=f"[{row}]"
                row +=1
            #print cell
            return_string+= str(self.grid[key])

            #end of row
            if not (i+1)%self. size:
                return_string+="\n"
        
        return return_string
    
    def shoot_at(self, coor):
        if cell :=self.grid[coor]:
            if cell.content == Content.BOAT:
                cell.set_hit()
                return True
