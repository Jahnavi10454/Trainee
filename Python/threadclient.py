import threading
import socket
import tkinter as tkr

root = tkr.Tk()
root.title("CHATTING APPLICATION")
root.geometry("300x500")
message = ""

def sendMessage(clientSocket):
    global message
    sentMessage = entry.get()
    clientSocket.send(sentMessage.encode())
    message = message  + "\n" + "sent: " + sentMessage
    myLabel.configure(text = message)
    if sentMessage == 'bye':
        root.destroy()
        clientSocket.close()
    else:
        entry.delete(0, tkr.END)

def recvMessage(clientSocket):
    while True:
        global message
        try:
            recievedMessage = clientSocket.recv(1024).decode()
            message = message + "\n" + "recieved: " + recievedMessage
            myLabel.configure(text=message)
        except:
            clientSocket.close()
            root.destroy()
            break

clientSocket = socket.socket()
clientSocket.connect(('localhost', 1923))
recv = threading.Thread(target = recvMessage, args = (clientSocket, ))
recv.start()

myLabel = tkr.Label(root, width=500, height=25, background="lightblue", text = "let's communicate!")
myLabel.pack(padx=10, pady=20)

entry = tkr.Entry(root, width=200)
entry.pack(padx=10, pady=15)
entry.bind("<Return>", lambda event: sendMessage(clientSocket))

button = tkr.Button(root, text="send", command=lambda: sendMessage(clientSocket))
button.pack()
root.mainloop()




