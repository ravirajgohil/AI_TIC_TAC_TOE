from Game import Game
import datetime


#Check this method
#This method is used to log the game information to the file
#Input 
#   1. log - Receives the game log
#   2. gameType - Type of the game(0), Check Game.py for more detail
#   3. gameComplexity - Complexity of the game(0),  Check Game.py for more detail
#Output
#   
def addLog(log, gameType = 0, gameComplexity = 0 ):
    
    logstr = str(datetime.datetime.now()) + "," + str(gameType) + str(gameComplexity) + ","

    f = open("gameLog.txt", "a+")

    for l in log:
        logstr += str(l)

    print(logstr)
    logstr += "\n"
    f.write(logstr)
    f.close()


#This method reads moves data from the allGames.txt file which contains all possible games
#Input
#
#Output
#   1. Move Log data
def getMovesFromFile():
    f = open("C:\\Users\\I344148\\Desktop\\Newfolder\\Programs\\miniProjects\\TicTacToe\\allGames.txt", "r")
    txtData = f.readlines()
    f.close()
    return txtData


#This method reads moves data from the movelog file
#Input
#   1. currGame - Contains the current Game object
#Output
#
def playIntern(currGame):
    while currGame.isGameOn():
        currPlayer = currGame.getCurrPlayer()
        
        if currPlayer["PlayerType"] == 1:                       #If manual player
            currGame.PerfomMove(int(input("Perform your move")))
        else:
            #print("Robot in progress")                         #If computer
            currGame.PerfomMove(-1) 

    print(currGame.getMoveLog())                                    #Print move log in the screen
    addLog(currGame.getMoveLog())                                   #Add move log to the file


#This method gets the user input and validates with expected input
#Input
#   1. typeOfInput - data type of expected input
#   2. message - message to be displayed
#   3. rangeInput - range of inputs if required
#Output
#   1. inputVal - Validated input value

def getInput(typeOfInput, message='', rangeInput=[]):
    while True:
        inputVal = input(message)
        try:
            if typeOfInput == 'int':
                inputVal = int(inputVal)
                if rangeInput:
                    if inputVal in rangeInput:
                        return inputVal
                    else:
                        raise("wrong input")
                else:
                    return inputVal
        except:
            print("Invalid input, try again.")


#This method is the main method of this application
#Input
#   1. allGames(False) - A flag which if set, indicates reading all possible games and simulating them one by one 
#Output
#
def main(allGames = False):

    allGames = getInput("int", "Enter 0 if you want to play game and 1 if you want to simulate all games.", [0, 1])
    if allGames:
        allGameMoves = getMovesFromFile()

        for aGameMoves in allGameMoves:
            a = aGameMoves[1:-2].split(',')

            game = Game(gameTy=3, playAllFromFile=True, movesFromFile=a, noPrintMode=False)        #Game setting for perfroming all moves

            playIntern(game)
    else:
        print("1 - Human VS Human  2 - Human VS Computer  3 - Computer VS Computer ")
        gameType = getInput("int", "Chose game type.", [1, 2, 3])
        
        gameComplexity = 0
        if not gameType == 1:
            print("1 - Beginner  2 - Intermmediate  3 - Pro ")
            gameComplexity = getInput("int", "Chose game complexity.", [1, 2, 3])

        game = Game(gComplexity=gameComplexity, gameTy=gameType, noPrintMode=False)
        # game = Game(gComplexity=3, gameTy=2, noPrintMode=False)        #Game setting for P VS C
        playIntern(game)


main()
