from Game import Game
import datetime

#Check this method
def addLog(log,gameType = 0 ,gameComplexity = 0):

    logstr = str(datetime.datetime.now()) + ","
    logstr = logstr + str(gameType)
    logstr = logstr + str(gameComplexity) + ","

    f = open("gameLog.txt", "a+")

    for l in log:
        logstr += str(l)

    print(logstr)
    logstr += "\n"
    f.write(logstr)
    f.close()

def getMovesFromFile():
    f = open("C:\\Users\\I344148\\Desktop\\Newfolder\\Programs\\miniProjects\\TicTacToe\\allGames.txt", "r")
    txtData = f.readlines()
    f.close()
    return txtData


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

def play():
    allGames = False

    if allGames:
        allGameMoves = getMovesFromFile()

        for aGameMoves in allGameMoves:
            a = aGameMoves[1:-2].split(',')

            game = Game(gameTy = 3, playAllFromFile = True, movesFromFile = a , noPrintMode = False)        #Game setting for perfroming all moves

            playIntern(game)
    else:
        game = Game(gComplexity = 3, gameTy = 2, noPrintMode = False)        #Game setting for P VS C    
        playIntern(game)  

play()
