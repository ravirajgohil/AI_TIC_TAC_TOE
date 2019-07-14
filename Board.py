import copy

class Board:
    def __init__(self):
        self.__boardStatus__ = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


    # This method updates the game board
    # Input
    #   1. sign - Sign of current player
    #   2. position - position of current move
    #   2. doesPrint - print the table after move flag
    # Output
    #
    def updateBoard(self, sign, position, doesPrint = 0):
        if self.__boardStatus__[position] == ' ':
            self.__boardStatus__[position] = sign
            return 0
        else:
            if( doesPrint == 1):
                print("Invalid Move")
            return -1


    def getBoard(self):
        return self.__boardStatus__


    # This method check if the game is active
    # Input
    #
    # Output
    #   1. return the game activation status
    def checkGameOver(self, nextMoveSign=' '):
        if (self.__boardStatus__[0] == self.__boardStatus__[1] == self.__boardStatus__[2]) and self.__boardStatus__[0] != " ":
            return self.__boardStatus__[0]
        elif (self.__boardStatus__[3] == self.__boardStatus__[4] == self.__boardStatus__[5]) and self.__boardStatus__[3] != " ":
            return self.__boardStatus__[3]
        elif (self.__boardStatus__[6] == self.__boardStatus__[7] == self.__boardStatus__[8]) and self.__boardStatus__[6] != " ":
            return self.__boardStatus__[6]
        elif (self.__boardStatus__[0] == self.__boardStatus__[3] == self.__boardStatus__[6]) and self.__boardStatus__[0] != " ":
            return self.__boardStatus__[0]
        elif (self.__boardStatus__[1] == self.__boardStatus__[4] == self.__boardStatus__[7]) and self.__boardStatus__[1] != " ":
            return self.__boardStatus__[1]
        elif (self.__boardStatus__[2] == self.__boardStatus__[5] == self.__boardStatus__[8]) and self.__boardStatus__[2] != " ":
            return self.__boardStatus__[2]
        elif (self.__boardStatus__[0] == self.__boardStatus__[4] == self.__boardStatus__[8]) and self.__boardStatus__[0] != " ":
            return self.__boardStatus__[0]
        elif (self.__boardStatus__[2] == self.__boardStatus__[4] == self.__boardStatus__[6]) and self.__boardStatus__[2] != " ":
            return self.__boardStatus__[2]
        elif " " not in self.__boardStatus__:
            return -1
        else:
            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
            indices = get_indexes(" ", self.__boardStatus__)
            if len(indices) == 1:
                self.__boardStatus__[indices[0]] = nextMoveSign
                if self.checkGameOver() == -1:
                    self.__boardStatus__[indices[0]] = ' '
                    return -1
                self.__boardStatus__[indices[0]] = ' '
            return 0


    # This method prints the board
    # Input
    #
    # Output
    #
    def drawBoard(self):
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
