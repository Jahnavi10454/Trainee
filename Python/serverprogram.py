# server program which handles multiple clients

import socket
import threading

clients = []

def handleClient(connection):
    while True:   
        try:
            message = connection.recv(1024).decode()
            broadcast(connection, message)
            if message == 'bye':
                connection.close()
                client.remove(connection)
                break
        except:
            break     

def broadcast(connection, message):
    for client in clients:
        if client != connection:
            client.send(message.encode())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('0.0.0.0', 1923))
serverSocket.listen()
print("waiting for connections....")
while True:
    connection, addr = serverSocket.accept()
    print(f"connected to the {addr}")
    client = threading.Thread(target=handleClient, args=(connection,))
    client.start()
    clients.append(connection) 
