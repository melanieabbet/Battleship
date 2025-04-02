'''
@file player.py
'''
from asset import Grid, Boat, Content
from gameplay.terminalHandler import Terminal

class Player:

    def __init__(self, name):
        self.name = name
        self.terminal = Terminal()
        self.grid = Grid(9)

        a = Boat(2)
        b = Boat(3)
        c = Boat(4)
        d = Boat(5)
        self.fleet = [a, b, c ,d]

    def set_boat(self):

        for boat in self.fleet:
            self.terminal.clear()
            print(self.grid)
            boat.set_boat(self.terminal.get_coordinate_array(boat.size, self.grid), self.grid)
        
        self.terminal.clear()
        print(self.grid)
    
    def shoot(self, grid, coordinate):
        cell = grid[coordinate]
        if cell.content == Content.BOAT:
            cell.content=Content.HIT
            print("touché")

        elif cell.content == Content.EMPTY:
            cell.content=Content.MISS
            print("Raté")

        elif cell.content == Content.MISS:
            print("Toujours pas")
        
        elif cell.content == Content.MISS:
            print("Hum...")