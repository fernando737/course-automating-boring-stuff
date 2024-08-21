ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe"""
    print("Welcome to the Tic Tac Toe!")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))

        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move (1-9)'.format(currentPlayer))
            move = input()
        updateBoard(gameBoard, move, currentPlayer)

        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print("The game is a tie!")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')

def getBlankBoard():
    """Create a new, blank tic tac toe board."""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def getBoardStr(board):
    """Return a tex-representation of the board."""
    return '''
        {}|{}|{}  1 2 3
        -+-+-
        {}|{}|{}  4 5 6
        -+-+-
        {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'],
                                      board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """Returns True if the space on the Board is a valid space number and the space is blank."""
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board,player):
    """Return True if player is a winner on this TTTBoard."""
    b, p = board, player

    return((b['1'] == b['2'] == b['3'] == p) or #Across the top
           (b['4'] == b['5'] == b['6'] == p) or #Across the middle
           (b['7'] == b['8'] == b['9'] == p) or #Across the bottom
           (b['1'] == b['4'] == b['7'] == p) or #Down the left
           (b['2'] == b['5'] == b['8'] == p) or #Down the middle
           (b['3'] == b['6'] == b['9'] == p) or #Down the right
           (b['3'] == b['5'] == b['7'] == p) or #Diagonal right to left
           (b['1'] == b['5'] == b['9'] == p))

def isBoardFull(board):
    """Return true if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True

def updateBoard(board, space, mark):
    """Set the space on the board to mark."""
    board[space] = mark

if __name__ == '__main__':
    main()