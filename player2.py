#Import modules (socket for communicating between machines, tkinter for GUI, boardgame for game code/GUIs)
import socket
import tkinter as tk
import boardgame as bg

if __name__ == '__main__':
    #Set up server socket (TCP sockets using loopback address)
    #Player 2 is the server: 
        #Server socket needs to bind with a tuple of hostAddress and port #
        #Server socket listens for a connection and accepts
    hostAddress = '127.0.0.1'
    port = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((hostAddress, port))
    #Maximum 1 connection
    serverSocket.listen(1)
    #Accept incoming connection request from player1
    clientSocket,clientAddress = serverSocket.accept()
    #Create instance of boardUIPacker for player2 
    player2board = bg.boardUIPacker(clientSocket, "player2")
    #Close the socket to refuse additional connections
    serverSocket.close()