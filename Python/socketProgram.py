# Client program

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.57'
port = 12345
client_socket.connect((host, port))
client_socket.send(input().encode())
data = client_socket.recv(1024).decode()
print(f"Received from server: {data}")
client_socket.close()

