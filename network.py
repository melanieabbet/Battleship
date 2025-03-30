import socket


class Server:
    '''
        The Server class handles network connections and message between players.
    '''
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        # socket object: socket.AF_INET specifies the IP, socket.SOCK_STREAM indicates a TCP socket
        #socket.AF_INET is for IPV4
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print(f"Listening on {self.host}:{self.port}")

        #Accept connection
        client_conn, client_addr = self.server.accept()
        with client_conn:
            print('Connection', client_addr)
            print(f"Connection {client_addr[0]}:{client_addr[1]}")
            #Communication loop
            while True:
                request = client_conn.recv(1024)
                request = request.decode("utf-8")

                #Closing
                if request.lower() == "close":
                    client_conn.send("closed".encode("utf-8"))
                    break

                print(f"Received: {request}")

                #Responding
                response = "accepted".encode("utf-8") # convert string to bytes
                client_conn.send(response)

            # on break close connection with the client
            client_conn.close()
            print("Connection to client closed")
            self.server.close()


class Client:
    '''
        The Client class represent users connecting to the server and communicating with other users
    '''
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def run(self):
        self.client.connect((self.host,self.port))

        while True:
            # input & send message
            message = input("Enter message: ")
            self.client.send(message.encode("utf-8")[:1024])
        
            # response
            response = self.client.recv(1024)
            response = response.decode("utf-8")

            # if server sent us "closed" in the payload, we break out of the loop and close our socket
            if response.lower() == "closed":
                break

        print(f"Received: {response}")
        # close client socket (connection to the server)
        self.client.close()
        print("Connection to server closed")


# Tests terminal 1:
# test_server = Server()
# test_server.run()

# Tests terminal 2:
# test_server = Server()
# test_server.run()