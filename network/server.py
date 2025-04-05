import socket
import time

from .client import Client

class Server (Client):
    '''
    @brief the Server class deal with the socket connection as server
     
    @details it heritate from the Server class
    '''

    def get_ip(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip    

    def first_connect(self, player_name):
        '''
        @brief initialise the server socket
        
        @detail it is called only once and when the connection to the client is made,
            the socket is saved inside the instance
        
        @return enemy name
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()
        conn, addr  = s.accept() #wait until accept
        self.socket = s

        with conn:
            while True:
                opponent_name =conn.recv(1024).decode('utf-8')
                if opponent_name:
                    conn.send(player_name.encode('utf-8'))
                    break
            
        return opponent_name
    
    def open_fire(self, coor_string):
        '''
        @breif discution with client
        
        @details send the shoot coordinate and recive the one from the enemy
        
        @return coordinate of the enemy shoot (as a string)
        '''
        self.socket.listen()
        conn, addr = self.socket.accept()

        with conn:
            while True:
                opponent_shoot = conn.recv(1024).decode('utf-8')
                if opponent_shoot:
                    conn.send(coor_string.encode('utf-8'))
                    break
            
        return opponent_shoot
    
    def round_result(self, enemy_result):
        '''
        @breif discution with client
        
        @details send the result of his shoot to the enemy get the player result
        
        @return the result of the shoot from the player
        '''
        self.socket.listen()
        conn, addr  = self.socket.accept() #wait until accept

        with conn:
            while True:
                result = conn.recv(1024).decode('utf-8')
                if result:
                    conn.send(enemy_result.encode('utf-8'))
                    break
                
        return result
    

    def close_socket(self):
        '''TODO use at the end of the game'''
        self.socket.close()







# import socket
# import threading
# import time
# from network.client import Client
# #from player import Player
# from game import GameSession

# class Server:
#     '''
#         The Server class handles threads and message between players.
#     '''
#     def __init__(self, host="127.0.0.1", port=12345):
#         self.host = host
#         self.port = port
#         # socket object: socket.AF_INET specifies the IP, socket.SOCK_STREAM indicates a TCP socket
#         # socket.AF_INET is for IPV4
#         self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.waiting_client = None

#     # def handle_client(self, client_conn, client_addr):
#     #     '''
#     #         Handle a client connection, create a player and wait for a match 
#     #     '''
#     #     print(f"Handling client from {client_addr[0]}:{client_addr[1]}")

#     #     try:
#     #         print(f"01")
#     #         client = Client(client_socket=client_conn)
#     #         player = Player(client)  # link a player with a client
#     #         client.send_message("Please enter your name:")
#     #         player.set_name(client.receive_message())
#     #         print(f"Player {player.name} connected.")

#     #         if self.waiting_client is None:
#     #             self.waiting_client = player
#     #             client.send_message("Waiting for an opponent...")
#     #         else:
#     #             # match players
#     #             player1 = self.waiting_client
#     #             player2 = player
#     #             self.waiting_client = None # reset waiting list

#     #             self.create_game_session(player1, player2)
#     #         while True:
#     #             time.sleep(1)  # Empêche une boucle infinie trop rapide
#     #             pass
#     #     except Exception as e:
#     #         print(f"Error when handling client: {e}")
#     #     finally:

#     #         print(f"Connection with {client_addr[0]}:{client_addr[1]} closed")

#     # def create_game_session(self, player1, player2):

#     #     '''
#     #         Create and start a game session.
#     #     '''
#     #     # Inform each player of their opponent's name
#     #     player1.client.send_message(f"Your opponent is {player2.name}")
#     #     player2.client.send_message(f"Your opponent is {player1.name}")
#     #     game_session = GameSession(player1, player2)
#     #     game_thread = threading.Thread(target=game_session.init_game) # TODO init_game() dans GameSession
#     #     game_thread.start() 

#     def run(self, ip):
#         '''
#             Start the server and listen for connections.
#         '''
#         try:
#             self.host = ip
#             self.server.bind((self.host, self.port))
#             self.server.listen(0)
#             print(f"Listening on {self.host}:{self.port}")

#             client_conn, client_addr  = self.server.accept() #wait until accept
#             self.conn = client_conn

#             print(f"Connection {client_addr[0]}:{client_addr[1]}")


#         except OSError:
#             print("Server is already running.")

#         except Exception as e:
#             print(f"Error: {e}")
#         # finally:
#         #     self.server.close()




#     # def get_ip(self):
#     #     hostname = socket.gethostname()
#     #     local_ip = socket.gethostbyname(hostname)
#     #     print(local_ip)
#     #     return local_ip

# if __name__ == "__main__":
#     serv = Server()  # Création de l'instance du serveur
#     serv.run()  # Lancement du serveur

