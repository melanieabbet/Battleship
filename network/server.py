import socket
import threading
import time
from network.client import Client
from player import Player
from game import GameSession

class Server:
    '''
        The Server class handles threads and message between players.
    '''
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        # socket object: socket.AF_INET specifies the IP, socket.SOCK_STREAM indicates a TCP socket
        # socket.AF_INET is for IPV4
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.waiting_client = None

    def handle_client(self, client_conn, client_addr):
        '''
            Handle a client connection, create a player and wait for a match 
        '''
        print(f"Handling client from {client_addr[0]}:{client_addr[1]}")

        try:
            print(f"01")
            client = Client(client_socket=client_conn)
            player = Player(client)  # link a player with a client
            client.send_message("Please enter your name:")
            player.set_name(client.receive_message())
            print(f"Player {player.name} connected.")

            if self.waiting_client is None:
                self.waiting_client = player
                client.send_message("Waiting for an opponent...")
            else:
                # match players
                player1 = self.waiting_client
                player2 = player
                self.waiting_client = None # reset waiting list

                self.create_game_session(player1, player2)
            while True:
                time.sleep(1)  # Empêche une boucle infinie trop rapide
                pass
        except Exception as e:
            print(f"Error when handling client: {e}")
        finally:

            print(f"Connection with {client_addr[0]}:{client_addr[1]} closed")

    def create_game_session(self, player1, player2):

        '''
            Create and start a game session.
        '''
        # Inform each player of their opponent's name
        player1.client.send_message(f"Your opponent is {player2.name}")
        player2.client.send_message(f"Your opponent is {player1.name}")
        game_session = GameSession(player1, player2)
        game_thread = threading.Thread(target=game_session.init_game) # TODO init_game() dans GameSession
        game_thread.start() 

    def run(self):
        '''
            Start the server and listen for connections.
        '''
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(0)
            print(f"Listening on {self.host}:{self.port}")

            while True:
                # Accept new Client connection
                client_conn, client_addr = self.server.accept()
                print(f"Connection {client_addr[0]}:{client_addr[1]}")

                connection_thread = threading.Thread(target=self.handle_client, args=(client_conn, client_addr))
                connection_thread.start()

        except OSError:
            print("Server is already running.")
        except Exception as e:
            print(f"Error: {e}")
        # finally:
        #     self.server.close()

if __name__ == "__main__":
    serv = Server()  # Création de l'instance du serveur
    serv.run()  # Lancement du serveur

