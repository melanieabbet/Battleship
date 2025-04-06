'''
@file player.py

@brief file that hold the player class and all the logic attached
'''
import os
from asset import Grid, Boat, Content, Coordinate
from gameplay.terminalHandler import Terminal
from network import Server, Client, NetRole

class Player:
    '''
    @brief class that deal with the player
    
    @details Each player will have an instance of this game
            It hold all the method needed to play the game
    '''

    def __init__(self, name):
        '''
        @brief class constructor
        '''

        self.name = name
        self.role = NetRole.NONE
        self.terminal = Terminal()
        self.grid = Grid(9)
        self.opponent_grid = Grid(9)

        #boat init
        a = Boat(2)
        b = Boat(3)
        # c = Boat(4)
        # d = Boat(5)

        self.fleet = [a, b]
    

    def set_role(self):

        role = self.terminal.get_role()
        if role == "h":
            self.connect = Server()
            self.role= NetRole.HOST
        else:
            self.connect = Client()
            self.role= NetRole.GUESS
        
    def lobby(self):

        if self.role == NetRole.HOST:
            ip = self.connect.get_ip()
            self.connect.set_host(ip)
            self.terminal.message(f"Your IP is: {ip}")
        else:
            host_ip = self.terminal.get_host_ip()
            self.connect.set_host(host_ip)
        opponent = self.connect.first_connect(self.name)
        self.opponent = opponent
        self.terminal.message(f"Your opponent is: {opponent}")


    def set_boat(self):
        '''
        @brief Use to put all the fleet on the Grid
        
        @details at the start of the game, each player have to put there boat on the Grid
                This metode deal with it and return True when done
        @return True
        '''

        for boat in self.fleet:
            boat.set_boat(self.terminal.get_coordinate_array(boat.size, self.grid), self.grid)

        self.fleet.sort() # so the weakest boat is at the end
        self.terminal.clear()
        print(self.grid)

        return True
    
    def shoot(self):
        '''
        @brief set shoot by the player
        
        @return Coordinate
        '''
        # self.terminal.message("C'est parti, lançons les hostilités !")
        # self.terminal.message("Quel sera votre prochain tire?")
        # self.terminal.print_grid(self.opponent_grid, False)
        return self.terminal.get_coordinate(self.grid)
    

    def round(self, coor):
        '''
        @brief round management for the player class
        
        @details at each round of the game this method is called to deal
                with the round data and the game status
        
        @param coor Coordinate where the play is shooting at
        
        @TODO the result is printed inside the methode
                -> a terminal method should be called
        '''
        #Coordinate to string
        str_coor = str(coor)
        enemy_shoot = self.connect.open_fire(str_coor)

        #String to Coordinate
        enemy_shoot = Coordinate(enemy_shoot)
        enemy_result = self.get_hit(enemy_shoot)
        
        #Get results of our shot
        result = self.connect.round_result(enemy_result)
        self.update_opponent_grid(coor, result)

        #Display updated fields
        self.display_grids()
        print(f"Enemy: {enemy_result}, You: {result}")

        # Vérifie si quelqu’un a gagné
        if result == "Game over":
            self.terminal.message("YOU WIN!")
            return "win"
        elif enemy_result == "Game over":
            self.terminal.message("YOU LOST! GAME OVER.")
            return "lose"
        return "continue"

    def update_opponent_grid(self, coor, result):
        '''
        @brief Update the opponent's grid with the result of our shot.
        
        @param coordinate The coordinate where the shot was made.
        @param result The result of the shot (Hit/Miss).
        
        @details This will mark the cell on the opponent's grid with the result of the shot.
        '''
        if result == "Hit" or  result == "Boat is sinking" or result == "Game over":
            self.opponent_grid[coor].content = Content.HIT
        elif result == "Missed":
            self.opponent_grid[coor].content = Content.MISS    
        
    def get_hit(self, coordinate):
        '''
        @brief result of a shoot at the player grid

        @param coordinate Coordinate where the shoot aim at

        @return result of the shoot

        @TODO the result is returned as a string, there is something better to do

        '''
        cell = self.grid[coordinate]
        
        if cell.content == Content.BOAT:
            cell.content = Content.HIT
            if len(self.fleet)!= self.check_fleet():

                if self.gameover():
                    message = "Game over"
                else:
                    message ="Hit and sunk !"
                
            else:
                message = "Hit"

        elif cell.content == Content.EMPTY:
            cell.content = Content.MISS
            message = "Missed"

        elif cell.content == Content.MISS:
            message = "Still nothing"
        
        elif cell.content == Content.HIT:
            message = "better safe than sorry..."
        return message

    def check_fleet(self):
        '''
        @check the fleet health

        @details check the weakest boat -> at the end of the list "fleet" 
        
        @return the number of boat
        '''
        self.fleet.sort()

        boat = self.fleet[-1]
        if boat.is_alive and not boat.health():
            #boat is sinking
            self.fleet.pop() #remove last boat
        
        return len(self.fleet)
    
    def display_grids(self):
        self.terminal.clear()
        self.terminal.message("Your grid:", False)
        self.terminal.print_grid(self.grid, False)
        self.terminal.message("Your opponent field:", False)
        self.terminal.print_grid(self.opponent_grid, False)
        
    def gameover(self):
        '''
        @brief test the gameover condition
        
        @return True if game Over
        '''
        return not bool(len(self.fleet))