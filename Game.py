#gameType :         1 - Human VS Human
#                   2 - Human VS Computer
#                   3 - Computer VS Computer 

from Board import Board
from MinMaxAI import MinMaxAI
from Player import Player
import random

class Game():
    def __init__(self,gComplexity = 1,gameTy = 1 ,p1_name = 'P1',p2_name = 'P2',playAllFromFile = False, movesFromFile = [], noPrintMode = False):
        #self.__gameComplexity__ = gComplexity   
        self.__gameType__ = gameTy              
        self.__moveLog__ = []
        self.__board__ = Board()
        self.__gameOn__ = True
        self.__noPrintMode__ = noPrintMode
        self.__playAllFromFile__ = playAllFromFile
        self.__movesFromFile__ = movesFromFile
        self.__gameCount__ = 0

        p1_type = p2_type = p1_compLevel = p2_compLevel = 0

        #Set Player Types and Player Complexity based on the Input
        if gameTy == 1 :
            p1_type = 1
            p2_type = 1

        elif gameTy == 2 :
            p1_type = 1
            p2_type = 2

            p2_compLevel =  gComplexity
        elif gameTy == 3 :
            p1_type = 2
            p2_type = 2

            p1_compLevel = gComplexity
            p2_compLevel = gComplexity
        else:
            print("Invalid Game Type")
            exit(1)

        self.__player1__ = Player(1,p1_type,p1_compLevel,p1_name,1,'X')
        self.__player2__ = Player(2,p2_type,p2_compLevel,p2_name,0,'O')
        self.__currPlayer__ = self.__player1__

        if not self.__noPrintMode__:
            self.__board__.drawBoard()

    #Use this method to set Player complexity in between the game, ( Update player methods too )
    #def setGameComplexity(self,gComplexity):
    ##    self.__gameComplexity__ = gComplexity
    #
    #    #Set Player Complexity Level
    #    self.__player1__.setComlexityLevel(gComplexity)
    #    self.__player2__.setComlexityLevel(gComplexity)

    #Use this method to set Player Type in between the game, ( Update player methods too )
    #def setGameType(self,gameTy):
    #
    #    #Set Player Type
    #    if gameTy == 1 :
    #        self.__player1__.setPlayerType(1)
    #        self.__player1__.setPlayerType(1)
    #    elif gameTy == 2 :
    #        self.__player1__.setPlayerType(1)
    #        self.__player1__.setPlayerType(3)
    #    elif gameTy == 3 :
    #        self.__player1__.setPlayerType(2)
    #        self.__player1__.setPlayerType(2)
    #    else:
    #        print("Invalid Input")
    #        exit(1)
    #
    #    self.__gameType__ = gameTy

    def addMoveLog(self,playerID,position):
        boardStatusStr = ""
        for i in self.__board__.getBoard():
            boardStatusStr = boardStatusStr + i
        self.__moveLog__.append(str(playerID) + "-" + str(position) + "-" + boardStatusStr)

    #def getGameComplexity(self):
    #    return self.__gameComplexity__

    def getGameType(self):
        return self.__gameType__

    def getMoveLog(self):
        return self.__moveLog__

    def __addWinner__(self,playerID):
        self.__moveLog__.append(str(playerID))

    def getCurrPlayer(self):
        return {"PlayerID":self.__currPlayer__.getPlayerID(),"PlayerName":self.__currPlayer__.getName(),
                "PlayerType": self.__currPlayer__.getPlayerType()}

    def PerfomMove(self,position):

        if position == -1:
            if not self.__playAllFromFile__:
                #Perform player move for Computer and get a valid Postion of move
                position = self.__currPlayer__.performMove(self.__board__.getBoard())
                #Update the board using player move
                self.__board__.updateBoard(self.__currPlayer__.getPlayerSign(),position,self.__doesPrint__(self.__currPlayer__.getPlayerType()))
                    
            else:
                ####-----This part of the code is used to play all the games where moves are read from the text file-----####
                ####-----NOTE: All the moves must be valid in a file-----####

                #Perform player move for Computer and get a valid Postion of move
                position = int(self.__movesFromFile__[self.__gameCount__])
                #Update the board using player move
                self.__board__.updateBoard(self.__currPlayer__.getPlayerSign(),position,self.__doesPrint__(self.__currPlayer__.getPlayerType()))
        else:

            #Update the board using player move. return -1( Indicating invalid move )
            if self.__board__.updateBoard(self.__currPlayer__.getPlayerSign(),position,self.__doesPrint__(self.__currPlayer__.getPlayerType())) == -1:
                return -1

        #Increment the GameCount(Move count). This variable is useful while perfroming moves from the file
        self.__gameCount__ += 1

        #After each successful move Draw the board
        self.__board__.drawBoard()

        #Update Move Log
        self.addMoveLog(self.__currPlayer__.getPlayerID(), position)

        #After each successful move check if the game is over( either one of the player has won the game or no valid moves left )
        gameOverCheck = self.__board__.checkGameOver()

        #If the game over check is -1( no valid move), unset gameOn variable 
        if gameOverCheck == -1:
            self.__gameOn__ = False
            if not self.__noPrintMode__:
                print("No one wins")
        #If the game over check is any of the player sign ( one of the player has won the game ), unset gameOn variable 
        elif gameOverCheck == self.__player1__.getPlayerSign() or gameOverCheck == self.__player2__.getPlayerSign():
            if not self.__noPrintMode__:
                print(self.__currPlayer__.getName(), "Wins")
            
            #Update Move Log
            self.__addWinner__(self.__currPlayer__.getPlayerID())
            self.__gameOn__ = False

        #after each succesful move switch current player
        self.__switchCurrentPlayer__()

    def isGameOn(self):
        return  self.__gameOn__

    def __switchCurrentPlayer__(self):
        if self.__currPlayer__ == self.__player1__:
            self.__currPlayer__ = self.__player2__
        else:
            self.__currPlayer__ = self.__player1__

    def __doesPrint__(self,player_type):
        if  player_type == 1:
            return 1
        else:
            return 0
    
    #Deprecated
    #def setMovesFromFile(self, movesFromFile):
    #    self.__movesFromFile__ = movesFromFile


    

                
