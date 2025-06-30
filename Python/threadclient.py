import threading
import socket
import tkinter as tkr

root = tkr.Tk()
root.title("CHATTING APPLICATION")
root.geometry("300x500")
message = ""
clientName = ""

userFrame = tkr.Frame(root)
chatFrame = tkr.Frame(root)

userFrame.pack(expand=True)
tkr.Label(userFrame, width=250, height=1, text = "Enter user name").pack(padx=10, pady=20)
userName = tkr.Entry(userFrame, width=200)
userName.pack(padx=35, pady=25)
userName.bind("<Return>", lambda event: startChatting())
saveButton = tkr.Button(userFrame, text="SAVE", command=lambda: startChatting())
saveButton.pack()

def startChatting():
    global clientName
    clientName = userName.get()
    if clientName:
        userFrame.destroy()
        chatFrame.pack()

def sendMessage(clientSocket):
    global message
    sentMessage = entry.get()
    clientSocket.send(f"{clientName}: {sentMessage}".encode())
    message = message  + "\n" + "sent: " + sentMessage
    text.configure(state="normal")
    text.delete("1.0", tkr.END)
    text.insert(tkr.END, message)
    text.configure(state="disabled")
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
            message = message + "\n" + recievedMessage
            text.configure(state="normal")
            text.delete("1.0", tkr.END)
            text.insert(tkr.END, message)
            text.configure(state="disabled")
        except:
            break

clientSocket = socket.socket()
clientSocket.connect(('localhost', 1923))
recv = threading.Thread(target = recvMessage, args = (clientSocket, ))
recv.start()

textFrame = tkr.Frame(chatFrame)
textFrame.pack(padx=10, pady=20)

scrollbar = tkr.Scrollbar(textFrame, orient='vertical')
scrollbar.pack(side="right", fill="y")

text = tkr.Text(textFrame, width=50, height=25, background="lightblue", yscrollcommand=scrollbar.set)
text.pack(side='left', expand=True)

scrollbar.configure(command=text.yview)

text.insert(tkr.END, "Let's communicate!")
text.config(state="disabled")

entry = tkr.Entry(chatFrame, width=200)
entry.pack(padx=10, pady=15)
entry.bind("<Return>", lambda event: sendMessage(clientSocket))

button = tkr.Button(chatFrame, text="send", command=lambda: sendMessage(clientSocket))
button.pack()
root.mainloop()




