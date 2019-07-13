class MinMaxAI():
    @staticmethod
    def __getMoveAlphaBeta__(boardStatus,playerSign,maximizerPlayer,level = 1):
        maxVal = { 'index' : -1, 'value' : -10}
        minVal = { 'index' : -1, 'value' : 10}

        for i in range(0,9):
            if boardStatus[i] != " ":
                continue
            
            boardStatus[i] = playerSign
            #print(boardStatus)

            winner = MinMaxAI.__isGameOver__(boardStatus,playerSign)
            
            if winner == -1:
                return { 'index' : i , 'value' : 0}
            elif winner in('O','X'): 
                if maximizerPlayer:
                    if winner == playerSign:
                        result = { 'index' : i , 'value' : 10/level}
                    else:
                        result = { 'index' : i , 'value' : -10/level}

                    if result['value'] >= maxVal['value']:
                        maxVal['value'] = result['value']
                        maxVal['index'] = i
                else:
                    if winner == playerSign:
                        result = { 'index' : i , 'value' : -10/level}
                    else:
                        result = { 'index' : i , 'value' : 10/level}

                    if result['value'] <= minVal['value']:
                        minVal['value'] = result['value']
                        minVal['index'] = i
                        
                boardStatus[i] = " "
            else:

                newplayerSign = 'X' if playerSign == 'O' else 'O'
                newlevel = level + 1
                newBoardStatus = boardStatus.copy()
                result = MinMaxAI.__getMoveAlphaBeta__(newBoardStatus,newplayerSign,not maximizerPlayer,newlevel)
                if maximizerPlayer:
                    if result['value'] >= maxVal['value']:
                        maxVal['value'] = result['value']
                        maxVal['index'] = i
                else:
                    if result['value'] <= minVal['value']:
                        minVal['value'] = result['value']
                        minVal['index'] = i
                        
                boardStatus[i] = " "
                #print(result)
        return maxVal if maximizerPlayer else minVal
 
        
    @staticmethod
    def __isGameOver__(board,playerSign):
        if ( board[0] == board[1] == board[2] ) and board[0] != " ":
            ##addWinner(checkValAt(0))
            return board[0]
        elif ( board[3] == board[4] == board[5] ) and board[3] != " ":
            ##addWinner(checkValAt(3))
            return  board[3]
        elif ( board[6] == board[7] == board[8] ) and board[6] != " ":
            ##addWinner(checkValAt(6))
            return  board[6]
        elif ( board[0] == board[3] == board[6] ) and board[0] != " ":
            ##addWinner(checkValAt(0))
            return board[0]
        elif ( board[1] == board[4] == board[7] ) and board[1] != " ":
            ##addWinner(checkValAt(1))
            return board[1]
        elif ( board[2] == board[5] == board[8] ) and board[2] != " ":
            ##addWinner(checkValAt(2))
            return board[2]
        elif ( board[0] == board[4] == board[8] ) and board[0] != " ":
            ##addWinner(checkValAt(0))
            return board[0]
        elif ( board[2] == board[4] == board[6] ) and board[2] != " ":
            ##addWinner(checkValAt(2))
            return board[2]
        elif " " not in board:
            ##addWinner(0)
            return -1
        else:
            return 0

print(MinMaxAI.__getMoveAlphaBeta__(['X'," ",'X'," ",'O'," "," ",'O','X'],'O',True))