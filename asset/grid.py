'''
File with the grid Module

The grid is used as the game board
'''
from asset.cell import Cell, Address

class Grid:

    def __init__(self, size):
        self.size = size
        
        #empty list
        self.cells = []

        #creation of a squared grind of cell
        for c in range(size):
            for r in range(size):
                address = Address(c,r)
                self.cells.append(Cell(address))

    
    def __repr__(self):
        '''
        @brief override methode to print the grid
        
        @detail method that is used to print the grid with the cell content
                it call the __repr__ method of the Cell inside self.cells
        '''
        #TODO error of display if size >9
        
        return_string = "[\]"
        #Header
        return_string+= "".join([f"[{Address.set_column(i)}]" for i in range(self.size)])
        return_string+="\n"

        row =1
        for i, cell in enumerate(self.cells):
            #print row header
            if not i%self.size:
                return_string+=f"[{row}]"
                row +=1
            #print cell
            return_string+= str(cell)
            #new row
            if not (i+1)%self. size:
                return_string+="\n"
        return return_string
