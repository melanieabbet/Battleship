'''
File with the grid Module

The grid is used as the game board
'''
from asset.cell import Cell
from asset.coordinate import Coordinate

class Grid:

    def __init__(self, size):
        self.size = size

        '''A grid is a dictionary with Coordinate paired with the maching Cell'''
        self.grid = {}
        for c in range(size):
            for r in range(size):
                address = Coordinate(c,r)
                cell = Cell()
                self.grid.update({address:cell})
    
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        '''key should be an address'''
        #TODO should check isinstance
        try:    
            return self.dic[key]
        except:
            raise ValueError("Item not found")
    
    def __iter__(self):
        #creat sorted list of cell from address
        self.dic.sorted()


    
    def __repr__(self):
        '''
        @brief override methode to print the grid
        
        @detail method that is used to print the grid with the cell content
                it call the __repr__ method of the Cell inside self.cells
        '''
        #TODO error of display if size >9

        return_string = "[\]"
        #Header
        return_string+= "".join([f"[{Coordinate.set_column(i)}]" for i in range(self.size)])
        return_string+="\n"

        row =1
        #iterate inside the self.grid dictionary
        for i, key in enumerate(self.grid):
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
