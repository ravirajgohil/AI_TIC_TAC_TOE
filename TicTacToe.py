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
def addLog(log,gameType = 0 ,gameComplexity = 0):
    
    logstr = str(datetime.datetime.now()) + "," + str(gameType) + str(gameComplexity) + ","
    #logstr = logstr + str(gameType)
    #logstr = logstr + str(gameComplexity) + ","

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


#This method is the main method of this application
#Input
#   1. allGames(False) - A flag which if set, indicates reading all possible games and simulating them one by one 
#Output
#
def main(allGames = False):
    
    if allGames:
        allGameMoves = getMovesFromFile()

        for aGameMoves in allGameMoves:
            a = aGameMoves[1:-2].split(',')

            game = Game(gameTy = 3, playAllFromFile = True, movesFromFile = a , noPrintMode = False)        #Game setting for perfroming all moves

            playIntern(game)
    else:
        game = Game(gComplexity = 3, gameTy = 2, noPrintMode = False)        #Game setting for P VS C    
        playIntern(game)  


main()
