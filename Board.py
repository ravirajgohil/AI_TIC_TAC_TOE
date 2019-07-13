class Board():
    def __init__(self):
        self.__boardStatus__ = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def updateBoard(self,sign,position,doesPrint = 0):
        if self.__boardStatus__[position] == ' ':
            self.__boardStatus__[position] = sign
            return 0
        else:
            if( doesPrint == 1):
                print("Invalid Move")
            return -1

    def getBoard(self):
        return  self.__boardStatus__
    
    def checkGameOver(self):
        if ( self.__boardStatus__[0] == self.__boardStatus__[1] == self.__boardStatus__[2] ) and self.__boardStatus__[0] != " ":
            ##addWinner(checkValAt(0))
            return self.__boardStatus__[0]
        elif ( self.__boardStatus__[3] == self.__boardStatus__[4] == self.__boardStatus__[5] ) and self.__boardStatus__[3] != " ":
            ##addWinner(checkValAt(3))
            return  self.__boardStatus__[3]
        elif ( self.__boardStatus__[6] == self.__boardStatus__[7] == self.__boardStatus__[8] ) and self.__boardStatus__[6] != " ":
            ##addWinner(checkValAt(6))
            return  self.__boardStatus__[6]
        elif ( self.__boardStatus__[0] == self.__boardStatus__[3] == self.__boardStatus__[6] ) and self.__boardStatus__[0] != " ":
            ##addWinner(checkValAt(0))
            return self.__boardStatus__[0]
        elif ( self.__boardStatus__[1] == self.__boardStatus__[4] == self.__boardStatus__[7] ) and self.__boardStatus__[1] != " ":
            ##addWinner(checkValAt(1))
            return self.__boardStatus__[1]
        elif ( self.__boardStatus__[2] == self.__boardStatus__[5] == self.__boardStatus__[8] ) and self.__boardStatus__[2] != " ":
            ##addWinner(checkValAt(2))
            return self.__boardStatus__[2]
        elif ( self.__boardStatus__[0] == self.__boardStatus__[4] == self.__boardStatus__[8] ) and self.__boardStatus__[0] != " ":
            ##addWinner(checkValAt(0))
            return self.__boardStatus__[0]
        elif ( self.__boardStatus__[2] == self.__boardStatus__[4] == self.__boardStatus__[6] ) and self.__boardStatus__[2] != " ":
            ##addWinner(checkValAt(2))
            return self.__boardStatus__[2]
        elif " " not in self.__boardStatus__:
            ##addWinner(0)
            return -1
        else:
            return 0

    def drawBoard(self):
        #if 1 == 1:
        #    s = True
        
        print()
        print(" " + self.__boardStatus__[6] + " " + "|", end="")
        print(" " + self.__boardStatus__[7] + " " + "|", end="")
        print(" " + self.__boardStatus__[8] + " ")
        print("-----------")

        print(" " + self.__boardStatus__[3] + " " + "|", end="")
        print(" " + self.__boardStatus__[4] + " " + "|", end="")
        print(" " + self.__boardStatus__[5] + " ")
        print("-----------")

        print(" " + self.__boardStatus__[0] + " " + "|", end="")
        print(" " + self.__boardStatus__[1] + " " + "|", end="")
        print(" " + self.__boardStatus__[2] + " ")

        print()
        print("*********************************")
        