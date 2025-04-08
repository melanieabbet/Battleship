'''execution module to test as a playground'''
import time
from gameplay import Player

if __name__ =="__main__":
    # 1) start of the game and setup
    name = input("Enter your name:")
    player = Player(name)
    player.set_role()

    # 2) whait for oponent
    player.lobby()
    time.sleep(2)

    # 3) set all the boat
    player.set_boat()

    # 4) game start
    while True:
        coor=player.shoot()
        result = player.round(coor)
        time.sleep(3)

        if result in ["win", "lose"]:
            break  # End of game
    
