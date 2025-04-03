'''execution module to test as a playground'''
import time
from gameplay import Player




if __name__ =="__main__":
    name = input("enter your name:")
    player = Player("nom")
    player.set_role()
    player.lobby()

    player.set_boat()

    while True:
        
        player.terminal.clear()
        coor = player.shoot()
        player.aim(coor)
        time.sleep(5)

    
