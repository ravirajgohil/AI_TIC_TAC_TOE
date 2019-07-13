f = open("gameLog.txt", "r")
logData = f.readlines()
moveLog = [[],[],[],[],[]]
attackDiffence = [True]

for log in logData:
    #print(logData)
    gTimeStamp,gDetails,gLog = log.split(",")

    #Only for win strategy
    logLen = len(gLog)
    #if gLog[-2] == "2":
    player = gLog[-2]
    gLog = gLog[:-1]

    sliceNum = logLen // 13 #13 in the length of each move in the log

    count = 0

    while count < sliceNum:
        tempStr = gLog[(count*13):((count+1)*13)]
        #print(tempStr)
        if tempStr[0] == "1":   #Moves of Player 2 only
            if player == "1":
                moveLog[count//2].append(tempStr[2])
            else:
                if attackDiffence[0]:
                    moveLog[count // 2].append("-"+tempStr[2])
        count+= 1

mcount = 0
#print(moveLog)

f = open("attackStrategy1.txt", "w+")
for moveCount in moveLog:
    moveCount.sort()
    moveLocation = [0,0,0,0,0,0,0,0,0]
    for moveOccurance in moveCount:
        if len(moveOccurance) == 2:
            moveLocation[int(moveOccurance[-1])] -= 1
        else:
            moveLocation[int(moveOccurance)] += 1

    count = 0
    movePerc = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    while count < 9:
        movePerc[count] = ((moveLocation[count] / len(moveCount))*100)
        count+= 1
    #movePerc.sort(reverse=True)

    print(movePerc)

    mcount += 1
    perStr = str(mcount)+"-"
    for i,moveP in enumerate(movePerc):
        perStr = perStr + str(moveP) + ","

    perStr += '\n'
    f.write(perStr)

    print(perStr)

f.close()


