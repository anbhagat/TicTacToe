#Import socket, tkinter, and boardgame modules
import socket
import tkinter as tk
import boardgame as bg

if __name__ == '__main__':
    #Define my socket address information
    clientAddress = '127.0.0.1'
    clientPort = 12000
    #Create a socket object on my server
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Attempt to connect to the server
    connectionSocket.connect((clientAddress,clientPort))
    #Create player1 instance of boardUIPacker (which is an instance of BoardClass) for their GUI
    #Pass connection socket into GUI
    player1board = bg.boardUIPacker(connectionSocket, "player1")
    #Close socket
    connectionSocket.close()

    
    


