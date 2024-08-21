board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

board_letters = set('abcdefgh')
board_numbers = set(map(str, range(1, 9)))
board_pieces_black = {'bking', 'bqueen', 'bbishop', 'brooks', 'bknight', 'bpawn'}
board_pieces_white = {'wking', 'wqueen', 'wbishop', 'wrooks', 'wknight', 'wpawn'}

def isValidChessBoard(theboard):
    return validateLocations(theboard) and validatePieces(theboard)

def validateLocations(theboard):
    return all(location[0] in board_numbers and location[1] in board_letters for location in theboard)

def validatePieces(theboard):
    piece_count = {'wking': 0, 'bking': 0, 'wpawn': 0, 'bpawn': 0, 'white': 0, 'black': 0}

    for piece in theboard.values():
        if piece in board_pieces_black:
            piece_count['black'] += 1
            piece_count[piece] = piece_count.get(piece, 0) + 1
        elif piece in board_pieces_white:
            piece_count['white'] += 1
            piece_count[piece] = piece_count.get(piece, 0) + 1
        else:
            return False
    
    if piece_count['white'] > 16 or piece_count['black'] > 16:
        return False
    if piece_count['wking'] != 1 or piece_count['bking'] != 1:
        return False
    if piece_count['wpawn'] > 8 or piece_count['bpawn'] > 8:
        return False
    return True

print(isValidChessBoard(board))
