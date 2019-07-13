#playerType :   1 - Manual
#               2 - Computer

#compLevel :    1 - Auto
#               2 - From Existing Stratergy
#               3 - MiniMax

import random
from MinMaxAI import MinMaxAI

class Player():
    def __init__(self,playerID,playerType,compLevel,name,isCurrPlayer,playerSign):
        self.__playerType__ = playerType
        self.__moveCount__ = 0
        self.__complexityLevel__ = compLevel
        self.__playerID__ = playerID
        self.__pname__ = name
        self.__sign__ = playerSign
        self.__playerMoveStratergyOriginal__ = []
        self.__playerMoveStratergyCurrent__ = []

        if self.__complexityLevel__ == 1:
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

    def setPlayerType(self,playerType):
        self.__playerType__ = playerType

    def setMoveCount(self,moveCount):
        self.__moveCount__ += 1

    def setComlexityLevel(self,compLevel):
        self.__complexityLevel__ = compLevel

    def setName(self,name):
        self.__pname__ = name

    def getPlayerSign(self):
        return self.__sign__

    def setPlayerSign(self,sign):
        self.__sign__ = sign

    def getPlayerID(self):
        return self.__playerID__
    
    def performMove(self,boardStatus):
        #For complexity level 1( Random Moves )
        if self.__complexityLevel__ == 1:
            return self.__getNextMoveBasedOnRandMoves__(boardStatus)
        #For complexity level 2( Moves based on stratergy )
        elif self.__complexityLevel__ == 2:
            return self.__getNextMoveBasedOnStratergy__(boardStatus)
        #For complexity level 3( Moves based on MinMax AI )
        elif self.__complexityLevel__ == 3:
            return self.__getNextMoveBasedOnMinMaxAI__(boardStatus)

    #Dpricated Method
    #def getNextMoveBasedOnStratergy(self):
    #    if len(self.__playerMoveStratergyCurrent__[self.__moveCount__]) == 0:
    #        return -1
    #    maxIndex = self.__playerMoveStratergyCurrent__[self.__moveCount__].index(max(self.__playerMoveStratergyCurrent__[self.__moveCount__]))
    #    self.__playerMoveStratergyCurrent__[self.__moveCount__].pop(maxIndex)
    #    return maxIndex

    def __getNextMoveBasedOnStratergy__(self,boardStatus):
        #Perform a valid move from the stratergy
        while len(self.__playerMoveStratergyCurrent__[self.__moveCount__]) != 0:
            tempPosition = self.__playerMoveStratergyCurrent__[self.__moveCount__].index(max(self.__playerMoveStratergyCurrent__[self.__moveCount__]))
            self.__playerMoveStratergyCurrent__[self.__moveCount__].pop(tempPosition)
            if boardStatus[tempPosition] != " ":
                return tempPosition

        #Control will come here only if no vaild move can be performed using stratergy. If it does perform random moves
        return self.__getNextMoveBasedOnRandMoves__(boardStatus)
    
    def __getNextMoveBasedOnRandMoves__(self,boardStatus):
        #Perform random moves until you find a valid move
        while True :
            tempPosition = random.randint(0,8)
            if boardStatus[tempPosition] == " ":
                return tempPosition

    def __getNextMoveBasedOnMinMaxAI__(self,boardStatus):
        #Perform a valid move using MiniMaxAI
        result = MinMaxAI.__getMoveAlphaBeta__(boardStatus,self.__sign__,True)
        return result['index']
        