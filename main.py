'''execution module to test as a playground'''
import time
from gameplay import Player, Terminal

class Game():
    '''
    @brief This Class is the game'''

    DISPLAY_DELAY = 2
    END_OF_ROUND_DELAY = 3
     
    def __init__(self):
        '''
        @brief creating an instance launch a game
        '''
        engine = Terminal()

        # 1) start of the game and setup
        name = engine.get_name()
        player = Player(name)

        #set role
        if role_message := player.set_role(engine.get_role()):
            engine.message(role_message)
            time.sleep(Game.DISPLAY_DELAY)

        # 2) whait for oponent
        if player.is_host():
            ip = player.get_own_ip()
            engine.message(f"Your IP is: {ip}")
            engine.message("Waiting for your opponent", clear=False)
        else:
            ip = engine.get_host_ip()

        enemy_name = player.lobby(ip)
        enemy = Player(enemy_name)
        engine.message(f"Your opponent is: {enemy_name}")
        time.sleep(2)

        # 3) set all the boat
        for boat in player:
            boat.set_boat(
                engine.get_coordinate_array(boat.size, player.grid),
                player.grid)
            
        #player.set_boat()

        # 4) game start

        #Keep Track
        enemy_result = None
        result = None
        last_enemy_shot = None
        last_player_shot = None

        while True:
            #print grids
            grids_disp = engine.print_named_grid(
                (player.name, player.grid),
                (enemy.name, enemy.grid))
            #If results exist print them
            if enemy_result is not None and result is not None and last_enemy_shot is not None and last_player_shot is not None:
                grids_disp += f"Enemy: {last_enemy_shot} - {enemy_result}, You: {last_player_shot} - {result}"
            #Player shoot
            coor = engine.get_coordinate(player.grid, message=grids_disp)

            #Shoot results
            enemy_result, result = player.round(coor)
            enemy.update_grid(coor, result)
            last_player_shot = coor
            last_enemy_shot = player.last_enemy_shot

            round_result = self.end_game(result, enemy_result)

            if round_result =="win":
                engine.message("YOU WIN!!!")
                time.sleep(Game.END_OF_ROUND_DELAY)
                break

            elif round_result == "lose":
                engine.message("YOU LOST! GAME OVER.")
                time.sleep(Game.END_OF_ROUND_DELAY)
                break
            # else:
            #     engine.message(f"Enemy: {enemy_result}, You: {result}")
            #     time.sleep(Game.END_OF_ROUND_DELAY)
         

    def end_game(self, player_result, enemy_result):
        '''
        @brief test end of game conditions
        '''
        if player_result == "Game over":
                #self.terminal.message("YOU WIN!")
                return "win"
        elif enemy_result == "Game over":
                #self.terminal.message("YOU LOST! GAME OVER.")
                return "lose"
        return "continue"


if __name__ =="__main__":
    game = Game()

    print("end of game")