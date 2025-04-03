import socket

class Client:
    '''
        Interface of communication: The user communicate through the interface to the server
    '''
    def __init__(self, host="127.0.0.1", port=12345, client_socket=None):
        self.host = host
        self.port = port
        self.client = client_socket if client_socket else socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        '''
            server connexion
        '''
        self.client.connect((self.host,self.port))

    def send_message(self, message):
        try:
            print(f"Sending: {message}")  # Debug
            self.client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error in send_message: {e}")

    def receive_message(self):
        try:
            message = self.client.recv(1024).decode('utf-8')
            print(f"Received: {message}")  # Debug
            return message
        except Exception as e:
            print(f"Error in receive_message: {e}")
            return ""

    def close(self):
        '''
            close server connexion
        '''
        self.client.close()
    
    def run(self):
        '''
            Run the client: connect to server and wait for communication
        '''
        self.connect()  # Connect to the server

        while True:
            # Receive the first message from the server
            message = self.receive_message()

            # If the server asks for a name, we provide it
            if "Please enter your name:" in message:
                name = input("Enter your name: ")
                self.send_message(name)

            # If the server says waiting for an opponent, we print the message
            elif "Waiting for an opponent..." in message:
                print("You are waiting for an opponent...")
                continue  # Exit the loop after receiving this message
            elif "Your opponent is" in message:
                print(message)  # Affiche le nom de l'adversaire

            # Additional conditions can be handled here, like starting the game etc.

        # Closing connection after loop
        self.close()

if __name__ == "__main__":
    user = Client()  # Create the client instance
    user.run()  # Run the client (connect and communicate with server)
