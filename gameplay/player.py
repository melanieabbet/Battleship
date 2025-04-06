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

        #boat init
        a = Boat(2)
        b = Boat(3)
        # c = Boat(4)
        # d = Boat(5)

        self.fleet = [a, b]
    

    def set_role(self):

        role = self.terminal.get_role()
        if role == NetRole.HOST:
            self.connect = Server()
            self.role= NetRole.HOST
        elif NetRole.GUEST:
            self.connect = Client()
            self.role= NetRole.GUEST
        
    def lobby(self):
        #if self.role == NetRole.HOST:
            
        # ip =self.terminal.get_ip()
        opponent = self.connect.first_connect(self.name)
        self. opponent = opponent
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
        coor = str(coor)
        enemy_shoot = self.connect.open_fire(coor)

        #String to Coordinate
        enemy_shoot = Coordinate(enemy_shoot)
        enemy_result = self.get_hit(enemy_shoot)

        result = self.connect.round_result(enemy_result)
        print(f"enemy: {enemy_result} you: {result}")
        
    
    def get_hit(self, coordinate):
        '''
        @brief result of a shoot at the player grid

        @param coordinate Coordinate where the shoot aim at

        @return result of the shoot

        @TODO the result is returned as a string, there is something better to do

        '''
        cell = self.grid[coordinate]
        if cell.content == Content.BOAT:
            cell.content=Content.HIT
            if len(self.fleet)!= self.check_fleet():

                if self.gameover():
                    return "game over"
                else:
                    return "Boat is sinking"
                
            else:
                return "Hit"

        elif cell.content == Content.EMPTY:
            cell.content=Content.MISS
            return "Missed"

        elif cell.content == Content.MISS:
            return "Still nothing"
        
        elif cell.content == Content.HIT:
            return "better safe than sorry..."

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
    

        
    def gameover(self):
        '''
        @brief test the gameover condition
        
        @return True if game Over
        '''
        return not bool(len(self.fleet))