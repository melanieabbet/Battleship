'''
@file player.py

@brief file that hold the player class and all the logic attached
'''
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
        self.grid = Grid(9)

        #boat init
        # a = Boat(2)
        b = Boat(3)
        # c = Boat(4)
        # d = Boat(5)

        self.fleet = [b]
    
    def __iter__(self):
        ''' 
        @brief an iteration inside player will get
            the boat one after the other
        '''
        return iter(self.fleet)
    
    def set_role(self, role):
        '''
        @brief set the role of the player
        
        @details can be Host or Guest
        '''
        self.role = role

        if self.is_host():
            self.connect = Server()
            
            # Is Server role free ?
            if self.connect.is_server_running():
                self.connect = Client()  # Change to client
                self.role = NetRole.GUEST
                return "Error while trying to host, be guest" #raise error

        else:
            self.connect = Client()
      

    def is_host(self):
        '''
        @brief return True if the player is the game host
        '''
        if self.role == NetRole.HOST:
            return True
        else:
            return False
        
    def get_own_ip(self):
        '''
        @brief return the ip address of the host as a string
        '''
        if self.is_host():
            return self.connect.get_ip()
        else:
            return False

        
    def lobby(self, connection_ip):
        '''
        @brief when the player is waiting for opponent
        '''
        if self.role == NetRole.HOST:
            self.connect.set_host(connection_ip)
        else:
            self.connect.set_host(connection_ip)

        return self.connect.first_connect(self.name)
   

    def round(self, coor):
        '''
        @brief round management for the player class
        
        @details connection method to send an recive he result from the other player
        
        @param coor Coordinate where the play is shooting at

        @return the enemy result and the player result as string
        '''
        #Coordinate to string
        str_coor = str(coor)
        enemy_shoot = self.connect.open_fire(str_coor)

        #String to Coordinate
        enemy_shoot = Coordinate(enemy_shoot)
        enemy_result = self.get_hit(enemy_shoot)
        
        #Get results of our shot
        result = self.connect.round_result(enemy_result)
        return enemy_result, result     

    def update_grid(self, coor, result):
        '''
        @brief Update the player's grid with the result of a shot.
        
        @param coordinate The coordinate where the shot was made.

        @param result The result of the shot (Hit/Miss).
        
        @details This will mark the cell on the opponent's grid with the result of the shot.
        '''
        if result == "Hit" or  result == "Hit and sunk !" or result == "Game over":
            self.grid[coor].content = Content.HIT
        elif result == "Missed":
            self.grid[coor].content = Content.MISS    
        
    def get_hit(self, coordinate):
        '''
        @brief result of a shoot at the player grid

        @param coordinate Coordinate where the shoot aim at

        @return result of the shoot
        '''
        cell = self.grid[coordinate]
        
        if cell.content == Content.BOAT:
            cell.content = Content.HIT
            if len(self.fleet)!= self.check_fleet():

                if self.gameover():
                    message = "Game over"
                else:
                    message ="Hit and sunk!"
                
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
         
    def gameover(self):
        '''
        @brief test the gameover condition
        
        @return True if game Over
        '''
        return not bool(len(self.fleet))