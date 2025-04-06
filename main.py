'''execution module to test as a playground'''
import time
from enum import Enum
from gameplay import Player

    


if __name__ =="__main__":
    # 1) start of the game and setup
    name = input("Enter your name:")
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
        time.sleep(2)

        if result in ["win", "lose"]:
            break  # Fin du jeu
    
    # 5) TODO end of game // restart?
