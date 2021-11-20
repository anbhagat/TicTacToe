#Import modules (rename tkinter to tk and threading to allow continuous sending/receiving of moves)
import tkinter as tk
import threading

#Create BoardClass, will be imported by both player1 and player2 modules and an instance created in GUI class
class BoardClass():
    #Define constructor, passing player name
    def __init__(self, sock, title_name):
        #Initialize class variables
        self.username = ''
        self.title_name = title_name
        self.opponent = ''
        self.lastPlayer = ''
        self.games = 0
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.board = [ ['','',''], ['','',''], ['','',''] ]
        self.sock = sock
    #Define Class Methods:
    #Define set & get methods:
    def getGames(self):
        return self.games
    def setGames(self, num):
        self.games = num

    #Define game code methods
    def updateGamesPlayed(self): 
        self.setGames(self.getGames()+ 1)

    def resetGameBoard(self):
        self.board = [ ['','',''], ['','',''], ['','',''] ]
        self.lastPlayer = ''

    #Function ensures that player doesn't add to an already clicked button
    def isEmpty(self,loc):
        if loc == 'A' and self.board[0][0] != '':
            return False
        if loc == 'B' and self.board[0][1] != '':
            return False
        if loc == 'C' and self.board[0][2] != '':
            return False
        if loc == 'D' and self.board[1][0] != '':
            return False
        if loc == 'E' and self.board[1][1] != '':
            return False
        if loc == 'F' and self.board[1][2] != '':
            return False
        if loc == 'G' and self.board[2][0] != '':
            return False
        if loc == 'H' and self.board[2][1] != '':
            return False
        if loc == 'I' and self.board[2][2] != '':
            return False
        return True
    #Function checks if the game board location is empty
    #Function assigns player 1(!= player2) to X's, else O's for player2 at that location on the board
    #Buttons positions 1-9 correspond to letters A-I
    def updateGameBoard(self, loc):
        if self.isEmpty(loc) == True:
            if self.lastPlayer != 'player2':
                #Assign player 1 as an 'X' to the loc
                if loc == 'A':
                    self.board[0][0] = 'X'
                elif loc == 'B':
                    self.board[0][1] = 'X'
                elif loc == 'C':
                    self.board[0][2] = 'X'
                elif loc == 'D':
                    self.board[1][0] = 'X'
                elif loc == 'E':
                    self.board[1][1] = 'X'
                elif loc == 'F':
                    self.board[1][2] = 'X'
                elif loc == 'G':
                    self.board[2][0] = 'X'
                elif loc == 'H':
                    self.board[2][1] = 'X'
                elif loc == 'I':
                    self.board[2][2] = 'X'
                #Switch player to player2 
                self.lastPlayer = 'player2'
                
            else:
                #Assign player2 as an 'O' to the loc
                if loc == 'A':
                    self.board[0][0] = 'O'
                elif loc == 'B':
                    self.board[0][1] = 'O'
                elif loc == 'C':
                    self.board[0][2] = 'O'
                elif loc == 'D':
                    self.board[1][0] = 'O'
                elif loc == 'E':
                    self.board[1][1] = 'O'
                elif loc == 'F':
                    self.board[1][2] = 'O'
                elif loc == 'G':
                    self.board[2][0] = 'O'
                elif loc == 'H':
                    self.board[2][1] = 'O'
                elif loc == 'I':
                    self.board[2][2] = 'O'
                #Switch lastPlayer value to anything
                self.lastPlayer = 'anjali'
    #Function takes in a string and initializes username var
    #Function sends username for the GUI display            
    def setPlayer(self, player):
        self.username = player
        print("USER NAME IS", player)
        sendData = player.encode()
        self.sock.send(sendData)
    
    def getPlayer(self):
        return self.username
    
    def setUsername(self, name):
        self.username = name
    
    def setOpponent(self, opponent):
        self.opponent = opponent
    
    def getOpponent(self):
        return self.opponent

    #8 combinations for a player to win (3 combinations aross, down, and 2 diagonals)  
    #Function takes these space combinations and if they're all equal to either X or O: 
        #Function checks if player1 sees X and updates their wins, else player 1 sees O and updates losses
    #Function repeats ^ for player2
    def isWinner(self):
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[0][0] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[0][0] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[0][0] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[0][0] == 'X':
                self.losses += 1
            self.games += 1
            return True 
        if (self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[1][0] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[1][0] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[1][0] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[1][0] == 'X':
                self.losses += 1
            self.games += 1 
            return True
        if (self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[2][0] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[2][0] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[2][0] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[2][0] == 'X':
                self.losses += 1
            self.games += 1
            return True
        if (self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[2][0] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[2][0] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[2][0] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[2][0] == 'X':
                self.losses += 1
            self.games += 1 
            return True
        if (self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[2][1] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[2][1] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[2][1] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[2][1] == 'X':
                self.losses += 1
            self.games += 1 
            return True
        if (self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] in ['X', 'O']):
            if self.title_name == 'player1' and self.board[2][2] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[2][2] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[2][2] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[2][2] == 'X':
                self.losses += 1
            self.games += 1 
            return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ['X', 'O']): 
            if self.title_name == 'player1' and self.board[1][1] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[1][1] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[1][1] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[1][1] == 'X':
                self.losses += 1
            self.games += 1
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ['X', 'O']): 
            if self.title_name == 'player1' and self.board[2][0] == 'X':
                self.wins += 1
            elif self.title_name == 'player1' and self.board[2][0] == 'O':
                self.losses += 1
            if self.title_name == 'player2' and self.board[2][0] == 'O':
                self.wins += 1
            elif self.title_name == 'player2' and self.board[2][0] == 'X':
                self.losses += 1
            self.games += 1
            return True
        return False
    #Function checks every space in the board if it's not blank (all clicked)
    #If all 9 buttons clicked, update ties and game count
    def boardIsFull(self):
        count = 0
        for row in range(3): 
            for col in range(3): 
                if self.board[row][col] != '': 
                    count += 1
        if count == 9: 
            self.ties += 1
            self.games += 1
            return True
        return False

    #Return statistics string of username, opponent username, game/wins/losses/ties count
    def printStats(self): 
        displayString = 'Your player user: '+ self.username + '\n Opponent user: ' + self.opponent + '\n Games played: ' + str(self.games) + '\n Games won: ' + str(self.wins) + '\n Games lost: ' + str(self.losses) + '\nGames tied: ' + str(self.ties)
        print(self.board)
        return displayString
    
#Create boardUIPacker, will be imported by both player1 and player2 modules and creates the whole GUI 
class boardUIPacker():
    #Defining a class variable of Board Game type
    myBoard = 0
    #Define class variable to store tkinter window
    master = 0
    #Define tkinter class variables
    player2= ''
    player1 = ''
    name = ''

    #Define my class constructor, passing in the client socket and the player name
    def __init__(self, sock, title_name):
        #Initializing my board game variable
        self.title_name = title_name
        self.myBoard = BoardClass(sock, title_name)
        self.sock = sock
        self.current_player = ''
        #Call my methods to create my canvas and add my widgets
        #Start thread to continuously run the GUI board
        threading.Thread(target=self.setupBoard).start()
        self.exchangeNames()
        self.current_player = self.myBoard.username
        if title_name == 'player2':
            self.current_player = self.myBoard.opponent
            self.myBoard.setUsername("player2")
        #Start thread to continuously run the player's turn and statistics
        threading.Thread(target=self.createUsernameLabel).start()
        threading.Thread(target=self.updateCurrentPlayer).start()
        print("My name:", self.myBoard.getPlayer())
        print("Opponent name:", self.myBoard.getOpponent())
        self.receiveData(sock)

    #Initialize variables   
    def initTKVariables(self):
        self.name = tk.StringVar()
    #Create a label that has the current player's turn displayed
    def updateCurrentPlayer(self):
        tk.Label(self.master, text= "   Player's Turn: " + self.current_player + "      ").grid(row = 350, column = 0)
    
    #Method updates player names 
    def exchangeNames(self):
        self.data = self.sock.recvfrom(1024)
        print(self.data)
        self.data = self.data[0].decode('ascii')
        self.myBoard.setOpponent(self.data)

    #Method defines the base GUI window 
    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title('Tic Tac Toe Game: ' + self.title_name) #sets the window title
        self.master.geometry('900x550') #Sets default size of window
        self.master.configure(background='pale violet red')
        self.master.resizable(1,1)

    #Define a method that creates a quit button that closes the GUI windows
    def quitButtons(self):
        self.quitButton = tk.Button(self.master, text= "Quit Game", command = self.master.destroy)
        self.quitButton.grid(row = 200, column = 20)
        
    #Define a method that creates the text input area for the players name
    def usernameEntry(self):
        tk.Entry(self.master, textvariable=self.name).grid(row=100, column=20)
        tk.Button(self.master,text="Submit",command= lambda: self.myBoard.setPlayer(self.name.get())).grid(row=100, column=21)
    
    #Create label that displays all statistics (usernames, games/wins/ties/losses)
    def createUsernameLabel(self):
        tk.Label(self.master, text= self.myBoard.printStats()).grid(row = 0, column = 19)
    
    #Creates label that directs user where to submit username
    def createPlayerLabel(self):
        tk.Label(self.master, text= 'Enter & Submit your username:').grid(row = 99, column = 20)
    
    #Method sends 'Play Again' or 'Fun Times' to player2, when player1 says [y/n] to playing again
    def sendResponse(self, response):
        if response in ['y', 'Y']:
            sendData = 'Play Again'.encode()
            self.sock.send(sendData)
        elif response in ['n', 'N']:
            sendData = 'Fun Times'.encode()
            self.sock.send(sendData)
            self.master.quit()
    
    #Method invoked when game is over and asks player1 (using the 3 widgets) Play Again?
    def askToPlayAgain(self):
        response = tk.StringVar()
        tk.Entry(self.master, textvariable=response).grid(row=102, column=20)
        tk.Button(self.master,text="Submit Response",command= lambda: self.sendResponse(response.get())).grid(row=102, column=21)
        tk.Label(self.master, text= 'Play again? (y/n)').grid(row = 102, column = 16)

    #Create 9 click commands that send data across sockets after a player clicks the button
    #
    def click1(self):
        #For server/player2 turn
        if self.button1["text"] == " " and self.myBoard.isEmpty('A'):
            if self.myBoard.lastPlayer != 'player2':
                self.button1["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button1["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('A')
            if self.current_player == self.myBoard.opponent:
                sendData = 'A'.encode()
                self.sock.send(sendData)
            #After every move, check if that player is the winner (isWinner returns boolean value)
            winner = self.myBoard.isWinner()
            #If the player isn't the winner, check if the board is full (boardIsFull returns boolean value)
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            #If player is the winner, reset the backend gameboard and the user interface buttons
            if winner:
                #Reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                #If the player is player1, invoke askToPlayAgain method (player1 chooses y/n)
                #Player1 plays first, set current_player to be player1's username
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            #If player is not the winner and the board is full
            elif not winner and board_is_full:
                #Reset the gameboard and GUI buttons
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            #Always display the statistics
            self.createUsernameLabel()
            #Switch player after sending data
            self.updateCurrentPlayer()
    def click2(self):
        #For server/player2 turn
        if self.button2["text"] == " " and self.myBoard.isEmpty('B'):
            if self.myBoard.lastPlayer != 'player2':
                self.button2["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button2["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('B')
            if self.current_player == self.myBoard.opponent:
                sendData = 'B'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
    
    def click3(self):
        if self.button3["text"] == " " and self.myBoard.isEmpty('C'):
            
            if self.myBoard.lastPlayer != 'player2':
                self.button3["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button3["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('C')
            if self.current_player == self.myBoard.opponent:
                sendData = 'C'.encode()
                print("sending NOW A")
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
    
    def click4(self):
        if self.button4["text"] == " " and self.myBoard.isEmpty('D'):
            
            if self.myBoard.lastPlayer != 'player2':
                self.button4["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button4["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('D')
            if self.current_player == self.myBoard.opponent:
                sendData = 'D'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
         
    def click5(self):
        if self.button5["text"] == " " and self.myBoard.isEmpty('E'):
            
            if self.myBoard.lastPlayer != 'player2':
                self.button5["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button5["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('E')
            if self.current_player == self.myBoard.opponent:
                sendData = 'E'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
        
    def click6(self):
        if self.button6["text"] == " " and self.myBoard.isEmpty('F'):
            if self.myBoard.lastPlayer != 'player2':
                self.button6["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button6["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('F')
            if self.current_player == self.myBoard.opponent:
                sendData = 'F'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
    def click7(self):
        if self.button7["text"] == " " and self.myBoard.isEmpty('G'):
            
            if self.myBoard.lastPlayer != 'player2':
                self.button7["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button7["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('G')
            if self.current_player == self.myBoard.opponent:
                sendData = 'G'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
    def click8(self):
        if self.button8["text"] == " " and self.myBoard.isEmpty('H'):
    
            if self.myBoard.lastPlayer != 'player2':
                self.button8["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button8["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('H')
            if self.current_player == self.myBoard.opponent:
                sendData = 'H'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
    def click9(self):
        if self.button9["text"] == " " and self.myBoard.isEmpty('I'):
            if self.myBoard.lastPlayer != 'player2':
                self.button9["text"] = "X"
                if self.title_name == "player2":
                    self.current_player = "player2"
                else:
                    self.current_player = self.myBoard.opponent
            else:
                self.button9["text"] = "O"
                if self.title_name == "player1":
                    self.current_player = self.myBoard.username
                else:
                    self.current_player = self.myBoard.opponent
            self.myBoard.updateGameBoard('I')
            if self.current_player == self.myBoard.opponent:
                sendData = 'I'.encode()
                self.sock.send(sendData)
            winner = self.myBoard.isWinner()
            if not winner:    
                board_is_full = self.myBoard.boardIsFull()
            if winner:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            elif not winner and board_is_full:
                #reset the GUI
                self.myBoard.resetGameBoard()
                self.resetButtons()
                if self.title_name == 'player1':    
                    self.askToPlayAgain()
                    self.current_player = self.myBoard.username
                if self.title_name == 'player2':
                    self.current_player = self.myBoard.opponent
            self.createUsernameLabel()
            self.updateCurrentPlayer()
        
    #Method creates 9 buttons in a 3x3 grid
    def boardSquare(self):
        #Buttons 1,2,3 in row1
        #Button  1
        self.button1 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click1)
        self.button1.grid(row = 1, column = 1)
        #Button 2
        self.button2 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click2)
        self.button2.grid(row = 1, column = 2)
        #Button 3
        self.button3 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click3)
        self.button3.grid(row = 1, column = 3)
        #Buttons 4,5,6 in row 2
        #Button 4
        self.button4 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click4)
        self.button4.grid(row = 2, column = 1)
        #Button 5
        self.button5 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click5)
        self.button5.grid(row = 2, column = 2)
        #Button 6
        self.button6 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click6)
        self.button6.grid(row = 2, column = 3)
        #Buttons 7,8,9 in row 3
        #Button 7
        self.button7 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click7)
        self.button7.grid(row = 3, column = 1)
        #Button 8
        self.button8 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click8)
        self.button8.grid(row = 3, column = 2)
        #Button 9
        self.button9 = tk.Button(self.master, text = " ", fg = "DodgerBlue4", bg = "white", width = 10, height= 6, command = self.click9)
        self.button9.grid(row = 3, column = 3)

    #Reset Board Buttons to blank
    def resetButtons(self):
        self.button1.configure(text = ' ')
        self.button2.configure(text = ' ')
        self.button3.configure(text = ' ')
        self.button4.configure(text = ' ')
        self.button5.configure(text = ' ')
        self.button6.configure(text = ' ')
        self.button7.configure(text = ' ')
        self.button8.configure(text = ' ')
        self.button9.configure(text = ' ')

    #Method that clicks button for other board after receiving command 
    def change(self, command):
        if command == 'A':
            self.click1()
        elif command == 'B':
            self.click2()
        elif command == 'C':
            self.click3()
        elif command == 'D':
            self.click4()
        elif command == 'E':
            self.click5()
        elif command == 'F':
            self.click6()
        elif command == 'G':
            self.click7()
        elif command == 'H':
            self.click8()
        elif command == 'I':
            self.click9()
        else:
            pass
             
    #Method to receieve data from the sockets
    def receiveData(self,sock):
        while True:
            self.data = sock.recvfrom(1024)
            self.data = self.data[0].decode('ascii')
            #If receiving a Play Again (player1 sends decision once game is over), display message on player2 GUI
            if self.data == 'Play Again':
                if self.title_name == 'player2':
                    tk.Label(self.master, text= 'Play Again').grid(row = 102, column = 16)
                self.resetButtons()
                self.myBoard.resetGameBoard()
            #If receiving Fun Times (player1 doesn't want to play another game), display message on player2 GUI
            elif self.data == 'Fun Times':
                tk.Label(self.master, text= 'Fun Times').grid(row = 102, column = 16)
            else:
                self.change(self.data)
    
    #Method starts my UI, event handler
    def runUI(self):
        self.master.mainloop()
    #Method invokes all GUI methods in proper order
    def setupBoard(self):
        self.canvasSetup()
        self.initTKVariables()
        self.boardSquare()
        self.createPlayerLabel()
        self.createUsernameLabel()
        self.usernameEntry()
        self.quitButtons()
        self.runUI()



        
