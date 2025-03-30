import socket
import threading

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

    def handle_client(self, client_conn, client_addr):
        try:
            #Communication loop
            while True:
                request = client_conn.recv(1024)
                request = request.decode("utf-8")

                #Closing
                if request.lower() == "close":
                    client_conn.send("closed".encode("utf-8"))
                    break
                #Not closing - get request
                print(f"Received: {request}")

                #Responding
                response = "accepted".encode("utf-8") # convert string to bytes
                client_conn.send(response)
        except Exception as e:
            print(f"Error when hanlding client: {e}")
        finally:
            # on break close connection with the client
            client_conn.close()
            print(f"Connection to client ({client_addr[0]}:{client_addr[1]}) closed")
    
    def run(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(0)
            print(f"Listening on {self.host}:{self.port}")

            while True:
                #Accept connection
                client_conn, client_addr = self.server.accept()
                print(f"Connection {client_addr[0]}:{client_addr[1]}")
                thread = threading.Thread(target=self.handle_client, args=(client_conn, client_addr,))
                thread.start()
        except Exception as e:
            print(f"Error: {e}")
        finally:
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

        try:
            while True:
                # input & send message
                message = input("Enter message: ")
                self.client.send(message.encode("utf-8")[:1024])
            
                # response server
                response = self.client.recv(1024)
                response = response.decode("utf-8")

                # if server sent us "closed" in the payload, we break out of the loop and close our socket
                if response.lower() == "closed":
                    break

                print(f"Received: {response}")
        except Exception as e:
            print(f"Error: {e}")
        finally:       
            # close client socket (connection to the server)
            self.client.close()
            print("Connection to server closed")


# Tests terminal 1:
# test_server = Server()
# test_server.run()

# Tests terminal 2:
# test_client1 = Client()
# test_client1.run()