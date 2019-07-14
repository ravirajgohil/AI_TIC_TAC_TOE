class MinMaxAI:
    # This method returns move based on MinMax algorithm
    # Input
    #   1. boardStatus - Current board status
    #   2. playerSign - player sign
    #   3. maximizerPlayer - maximizer of minimizer player flag
    #   4. level - current level of tree
    # Output
    #   1. best possible move
    @staticmethod
    def __getMoveAlphaBeta__(boardStatus, playerSign, maximizerPlayer, level=1):
        maxVal = {'index': -1, 'value': -10}
        minVal = {'index': -1, 'value': 10}

        for i in range(0, 9):
            if boardStatus[i] != " ":
                continue
            
            boardStatus[i] = playerSign

            winner = MinMaxAI.__isGameOver__(boardStatus, 'X' if playerSign == 'O' else 'O')
            
            if winner == -1:
                return {'index': i, 'value': 0}
            elif winner in('O', 'X'):
                if maximizerPlayer:
                    if winner == playerSign:
                        result = {'index': i, 'value': 10/level}
                    else:
                        result = {'index': i, 'value': -10/level}

                    if result['value'] >= maxVal['value']:
                        maxVal['value'] = result['value']
                        maxVal['index'] = i
                else:
                    if winner == playerSign:
                        result = {'index': i, 'value': -10/level}
                    else:
                        result = {'index': i, 'value': 10/level}

                    if result['value'] <= minVal['value']:
                        minVal['value'] = result['value']
                        minVal['index'] = i
                        
                boardStatus[i] = " "
            else:

                newplayerSign = 'X' if playerSign == 'O' else 'O'
                newlevel = level + 1
                newBoardStatus = boardStatus.copy()
                result = MinMaxAI.__getMoveAlphaBeta__(newBoardStatus, newplayerSign, not maximizerPlayer, newlevel)
                if maximizerPlayer:
                    if result['value'] >= maxVal['value']:
                        maxVal['value'] = result['value']
                        maxVal['index'] = i
                else:
                    if result['value'] <= minVal['value']:
                        minVal['value'] = result['value']
                        minVal['index'] = i
                        
                boardStatus[i] = " "
        return maxVal if maximizerPlayer else minVal


    # This method return if the game is active or not flag
    # Input
    #   1. current board status
    # Output
    #   1. game activation status
    @staticmethod
    def __isGameOver__(board, nextMoveSign= ' '):
        if (board[0] == board[1] == board[2]) and board[0] != " ":
            return board[0]
        elif (board[3] == board[4] == board[5]) and board[3] != " ":
            return board[3]
        elif (board[6] == board[7] == board[8]) and board[6] != " ":
            return board[6]
        elif (board[0] == board[3] == board[6]) and board[0] != " ":
            return board[0]
        elif (board[1] == board[4] == board[7]) and board[1] != " ":
            return board[1]
        elif (board[2] == board[5] == board[8]) and board[2] != " ":
            return board[2]
        elif (board[0] == board[4] == board[8]) and board[0] != " ":
            return board[0]
        elif (board[2] == board[4] == board[6]) and board[2] != " ":
            return board[2]
        elif " " not in board:
            return -1
        else:
            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
            indices = get_indexes(" ", board)
            if len(indices) == 1:
                board[indices[0]] = nextMoveSign
                if MinMaxAI.__isGameOver__(board) == -1:
                    board[indices[0]] = ' '
                    return -1
                board[indices[0]] = ' '
            return 0

#print(MinMaxAI.__getMoveAlphaBeta__(['X'," ",'X'," ",'O'," "," ",'O','X'],'O',True))
