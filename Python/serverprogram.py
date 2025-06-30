# server program which handles multiple clients

import socket
import threading

clients = []

def handleClient(connection):
    while True:   
        global clients
        try:
            message = connection.recv(1024).decode()
            # hostname = socket.gethostbyaddr(addr)
            broadcast(connection, message)
            messages = message.split(" ")
            print(messages[1])
            if messages[1] == 'bye':
                print(len(clients))
                connection.send("bye".encode())
                clients.remove(connection)
                print("Client removed...")
                print(len(clients))
                break
        except:
            break     

def broadcast(connection, message):
    global clients
    for client in clients:
        if client != connection:
            client.send(message.encode())

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('0.0.0.0', 1923))
serverSocket.listen()
print("waiting for connections...")
while True:
    connection, addr = serverSocket.accept()
    clients.append(connection) 
    print(f"connected to the {addr}")
    client = threading.Thread(target=handleClient, args=(connection, ))
    client.start()
    

