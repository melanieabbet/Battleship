'''execution module to test as a playground'''
import time
from gameplay import Player




if __name__ =="__main__":
    player = Player("nom")
    player.set_boat()

    while True:
        # player.terminal.clear()
        # print(player.grid)
        # c = player.terminal.get_coordinate(player.grid)
        # player.terminal.clear()
        # player.shoot(player.grid, c)
        # print(player.grid)
        # time.sleep(5)
        player.terminal.clear()
        coor = player.shoot()
        player.aim(coor)
        time.sleep(5)

    
