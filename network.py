import socket

HOST = "127.0.0.1" 
PORT = 12345


# socket object: socket.AF_INET specifies the IP, socket.SOCK_STREAM indicates a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(0)
print(f"Listening on {HOST}:{PORT}")

