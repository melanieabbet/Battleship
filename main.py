'''execution module to test as a playground'''
import time
from enum import Enum
from gameplay import Player

    


if __name__ =="__main__":
    # 1) start of the game and setup
    name = input("enter your name:")
    player = Player(name)
    # enemy = Player("enemy")

    # player.terminal.print_grid(player.grid, enemy.grid)
    
    player.set_role()

    # 2) whait for oponent
    player.lobby()

    time.sleep(2)

    # 3) place all the boat
    player.set_boat()

    # 4) game start
    while True:
        coor=player.shoot()
        result = player.round(coor)
    
    # 5) TODO end of game
