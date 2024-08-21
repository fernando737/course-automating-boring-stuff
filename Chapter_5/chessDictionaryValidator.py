board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking' }

board_letters = ['a','b','c','d','e','f','g','h']
board_numbers = [1,2,3,4,5,6,7,8,9]
board_pieces_black = ['bking', 'bqueen', 'bbishop', 'brooks', 'bknight', 'bpawn']
board_pieces_white = ['wking', 'wqueen', 'wbishop', 'wrooks', 'wknight', 'wpawn']

def isValidChessBoard(theboard):
    if validateLocations(theboard) and validatePieces(theboard):
        return True
    else:
        return False

def validateLocations(theboard):
    for location in theboard.keys():
        if len(location) == 2 and int(location[0]) in board_numbers and location[1] in board_letters:
            next
        else:
            return False    
    return True

def validatePieces(theboard):
    amountWhitePieces = 0
    amountBlackPieces = 0
    whitePieces = {}
    blackPieces = {}

    for value in theboard.values():
        if value in board_pieces_black:
            blackPieces.setdefault(value,0)
            blackPieces[value] = blackPieces[value] + 1
            amountBlackPieces += 1
        elif value in board_pieces_white:
            whitePieces.setdefault(value,0)
            whitePieces[value] = whitePieces[value] + 1
            amountWhitePieces += 1
        else:
            return False
    
    if amountWhitePieces > 16 or amountBlackPieces > 16:
        return False
    elif whitePieces.get('wking',0) > 1 or blackPieces.get('bking',0) > 1 or whitePieces.get('pawn',0) > 8 or blackPieces.get('pawn',0) > 8:
        return False
    return True

print(isValidChessBoard(board))