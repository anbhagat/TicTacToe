# Overview
This is a Python-shell-based game that you will initially be able to play on your own computer, but will extend so that you can play via the Internet by connecting to a central, shared server. 
Game moves are sent over from the client via TCP sockets to communicate across machines using threading.

# GUI
A 3x3 gameboard was created using Tkinter (the standard Python interface to the Tk GUI toolkit).
The game console will ask for user-input for the players names and whether they would like to play again after finishing a game.

# Back-end Context
Both player1 and player2 will create an instance of the BoardGame Class, which will represent the back-end logic for the Tic-Tac-Toe game. 
Both player1 and player2 will also create a boardUIPacker Class, which will create the physical GUI frame, buttons, and labels for both player interfaces.
This program is able to run multiple operations simultaneously with the implementation of threading, which will continuously run the player's turn and output its' statistics.
