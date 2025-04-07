'''
@file server.py

@brief file with the Server class
'''
import socket

from .client import Client

class Server (Client):
    '''
    @brief the Server class deal with the socket connection as server
     
    @details it heritate from the Server class
    '''
    def _exchange_data(self, data_to_send):
        '''$
        @brief Internal method to handle data exchange with the client.

        @details Listen, accept a connection, receive data, and send a param as response.
        
        @param data_to_send: data to send to client (str)

        @return data received from client (str)
        '''
        self.socket.listen()
        conn, addr = self.socket.accept()

        with conn:
            while True:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    conn.send(data_to_send.encode('utf-8'))
                    return data

    def get_ip(self):
        '''
        @brief find server host
        
        @detail called once to retrieve the private IP of the host

        @note MacOs: https://stackoverflow.com/questions/69937085/socket-gethostbyname-fails-on-macos
        
        @return private IP
        '''
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            return ip
        except socket.gaierror:
            print("Erreur lors de la récupération de l'hôte, vérifiez votre connection et réessayez.")
               

    def first_connect(self, player_name):
        '''
        @brief initialise the server socket
        
        @details it is called only once and when the connection to the client is made,
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

    def is_server_running(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.get_ip(), self.port))
            s.close()
            return False
        except OSError:
            return True
        
    def close_socket(self):
        '''TODO use at the end of the game'''
        self.socket.close()

