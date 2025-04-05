'''execution module to test as a playground'''
import time
from enum import Enum
from gameplay import Player

    


if __name__ =="__main__":
    # 1) start of the game and setup
    name = input("enter your name:")
    player = Player(name)
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

        if result in ["win", "lose"]:
            break  # Fin du jeu
    
    # 5) TODO end of game // restart?
