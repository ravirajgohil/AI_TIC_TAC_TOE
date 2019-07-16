#playerType -   1 - Manual
#               2 - Computer
#compLevel -    1 - Auto
#               2 - From Existing Stratergy
#               3 - MiniMax
#moveCount -    Integer which keeps track on moveCount of a player,
#                   and gets incremented with each move of that player
#playerID -     PlayerID stores the id of a player
#pname -        pname stores the player name
#sign -         sign chose for player
#                   it can be 'O' or 'X' 
#playerMoveStratergyOriginal - Stratergy loaded from file for Player
#playerMoveStratergyCurrent - Copiled from original stragergy, which is later modified
#


import random
from MinMaxAI import MinMaxAI

class Player():
    def __init__(self, playerID, playerType, compLevel, name, playerSign):
        self.__playerType__ = playerType
        self.__moveCount__ = 0
        self.__complexityLevel__ = compLevel
        self.__playerID__ = playerID
        self.__pname__ = name
        self.__sign__ = playerSign
        self.__playerMoveStratergyOriginal__ = []
        self.__playerMoveStratergyCurrent__ = []
        self.__invalidMoveVal__ = -99.999

        if self.__complexityLevel__ == 2:
            self.__loadPlayerStratergy__()


    def __loadPlayerStratergy__(self):
        if self.__playerID__ == 1:
            playerStratergyFile = open("attackStrategy1.txt", "r")
        else:
            playerStratergyFile = open("attackStrategy2.txt", "r")

        playerStratergyData = playerStratergyFile.readlines()
        
        for playerStratergyMoveRaw in playerStratergyData:
            self.__playerMoveStratergyOriginal__.append([])             #Append empty row for startegry which will be filled in next steps
            playerStratergyMove = playerStratergyMoveRaw[2:]            #Convert Raw format to consumable format
            movesStr = playerStratergyMove.split(',')
            movesStr.pop()                                              #Pop the last element as this is not a valid stategy num

            for move in movesStr:
                self.__playerMoveStratergyOriginal__[-1].append(float(move))
        
        self.__playerMoveStratergyCurrent__ = self.__playerMoveStratergyOriginal__.copy()


    def getPlayerType(self):
        return self.__playerType__


    def getMoveCount(self):
        return self.__moveCount__


    def getComlexityLevel(self):
        return self.__complexityLevel__


    def getName(self):
        return self.__pname__


    def setPlayerType(self, playerType):
        self.__playerType__ = playerType


    def incrementMoveCount(self):
        self.__moveCount__ += 1


    def setComlexityLevel(self, compLevel):
        self.__complexityLevel__ = compLevel


    def setName(self, name):
        self.__pname__ = name


    def getPlayerSign(self):
        return self.__sign__


    def setPlayerSign(self, sign):
        self.__sign__ = sign


    def getPlayerID(self):
        return self.__playerID__


    # This method performs move for player
    # Input
    #   1. Current board status
    # Output
    #
    def performMove(self, boardStatus):
        #For complexity level 1( Random Moves )
        if self.__complexityLevel__ == 1:
            return self.__getNextMoveBasedOnRandMoves__(boardStatus)
        #For complexity level 2( Moves based on stratergy )
        elif self.__complexityLevel__ == 2:
            return self.__getNextMoveBasedOnStratergy__(boardStatus)
        #For complexity level 3( Moves based on MinMax AI )
        elif self.__complexityLevel__ == 3:
            return self.__getNextMoveBasedOnMinMaxAI__(boardStatus)


    # This method returns the next move for the user based on startergy
    # Input
    #   1. Current board status
    # Output
    #   1. move for the player
    def __getNextMoveBasedOnStratergy__(self, boardStatus):
        #Perform a valid move from the stratergy
        while self.__playerMoveStratergyCurrent__ and len(self.__playerMoveStratergyCurrent__[self.__moveCount__]) != 0:
            tempPosition = self.__playerMoveStratergyCurrent__[self.__moveCount__].index(max(self.__playerMoveStratergyCurrent__[self.__moveCount__]))
            
            #If no possoble move availabe( all moves with value -99.999) break and goto random move( This in ideal case should not happen).
            if self.__playerMoveStratergyCurrent__[self.__moveCount__][tempPosition] == self.__invalidMoveVal__:
                break
            #Set the move which is already considered to invalidMoveVal to avoid future cosideration
            self.__playerMoveStratergyCurrent__[self.__moveCount__][tempPosition] = self.__invalidMoveVal__
            if boardStatus[tempPosition] == " ":
                return tempPosition

        #Control will come here only if no vaild move can be performed using stratergy. If it does perform random moves
        return self.__getNextMoveBasedOnRandMoves__(boardStatus)


    # This method returns the next move for the user Randomly
    # Input
    #   1. Current board status
    # Output
    #   1. move for the player
    def __getNextMoveBasedOnRandMoves__(self, boardStatus):
        #Perform random moves until you find a valid move
        while True:
            tempPosition = random.randint(0, 8)
            if boardStatus[tempPosition] == " ":
                return tempPosition


    # This method returns the next move for the user based on MinMax AI
    # Input
    #   1. Current board status
    # Output
    #   1. move for the player
    def __getNextMoveBasedOnMinMaxAI__(self, boardStatus):
        #Perform a valid move using MiniMaxAI
        result = MinMaxAI.__getMoveAlphaBeta__(boardStatus, self.__sign__, True)
        return result['index']
