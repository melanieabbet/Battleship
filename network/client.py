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
    







# import socket
# import time

# class Client:
#     '''
#         Interface of communication: The user communicate through the interface to the server
#     '''
#     def __init__(self, host="127.0.0.1", port=12345, client_socket=None):
#         self.host = host
#         self.port = port
#         self.client = client_socket if client_socket else socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     def connect(self):
#         '''
#             server connexion
#         '''
#         while True:
#             try:
#                 connection = self.client.connect((self.host,self.port))
#             except:
#                 time.sleep(1)

#     def tour(coordinate):
#         '''sending'''

#         while True:
#             self.con




#     def send_message(self, message):
#         try:
#             print(f"Sending: {message}")  # Debug
#             self.client.send(message.encode('utf-8'))
#         except Exception as e:
#             print(f"Error in send_message: {e}")

#     def receive_message(self):
#         try:
#             message = self.client.recv(1024).decode('utf-8')
#             print(f"Received: {message}")  # Debug
#             return message
#         except Exception as e:
#             print(f"Error in receive_message: {e}")
#             return ""

#     def close(self):
#         '''
#             close server connexion
#         '''
#         self.client.close()
    
#     def run(self, ip):
#         '''
#             Run the client: connect to server and wait for communication
#         '''
#         self.host = ip
#         self.connect()  # Connect to the server

#         while True:
#             # Receive the first message from the server
#             message = self.receive_message()

#             # If the server asks for a name, we provide it
#             if "Please enter your name:" in message:
#                 name = input("Enter your name: ")
#                 self.send_message(name)

#             # If the server says waiting for an opponent, we print the message
#             elif "Waiting for an opponent..." in message:
#                 print("You are waiting for an opponent...")
#                 continue  # Exit the loop after receiving this message
#             elif "Your opponent is" in message:
#                 print(message)  # Affiche le nom de l'adversaire

#             # Additional conditions can be handled here, like starting the game etc.

#         # Closing connection after loop
#         self.close()

# if __name__ == "__main__":
#     user = Client()  # Create the client instance
#     user.run()  # Run the client (connect and communicate with server)
