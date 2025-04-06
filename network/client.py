import socket 
import time

class Client:
    '''
    @brief the clien class deal with the socket connection as client
    '''


    def __init__(self, host_ip="127.0.0.1"):
        '''
        @brief constructor
        
        @param host_ip by default the value is the local address
        '''
        self.host = host_ip
        self.port = 12345
    
<<<<<<< HEAD
=======
    def _exchange_data(self, data_to_send):
        '''
        @brief Internal method to handle data exchange with the server.

        @details Connects, sends data, receives a response, and closes the connection.

        @param data_to_send: Data to send to server (str)
        
        @return: Data received from server (str)
        '''
        s = self.connect()
        if s:
            try:
                s.send(data_to_send.encode('utf-8'))
                response = s.recv(1024).decode('utf-8')
                return response
            finally:
                s.close()
    
>>>>>>> main
    def set_host(self, host_ip):
        self.host = host_ip

    def connect(self):
        '''
        @brief connect a new socket to the server
        
        @details is called at every start of discution
        
        @return socket connected to the host
        '''
        while True:
            #infint loop until conection to server
            #the socket must be created each time
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                return s
            except:
                time.sleep(0.5)
                #TODO timout function
                pass



    def first_connect(self, player_name):
        '''
        @brief Nametag exchange
        
        @return name of enemy
        '''
        return self._exchange_data(player_name)
    

    def open_fire(self, coor_string):
        '''
        @brief Exchange coordinates
        
        @return coordinate of the enemy shoot (as a string)
        '''
        return self._exchange_data(coor_string)
    
    
    def round_result(self, enemy_result):
        '''
        @brief Exchange results
        
        @return the result of the shoot from ennemi (as a string)
        '''
        return self._exchange_data(enemy_result)
    
