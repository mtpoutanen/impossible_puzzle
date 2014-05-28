from copy import deepcopy

from data_dict import PIECES

no_of_pieces = len(PIECES)

def print_puzzle(pieces):
    # the empty lists represent different rows
    puzzle = [
        [],
        [],
        [],
        []
    ]

    def piece_fits(piece, puzzle, row, column):
        fits_left = True
        fits_top = True
        piece_on_left = column > 0
        piece_on_top = row > 0

        if piece_on_left:
            fits_left = (piece.left + puzzle[row][column-1].right) == 0

        if piece_on_top:
            fits_top = (piece.top + puzzle[row - 1][column].bottom) == 0

        return fits_left and fits_top

    def find_next_empty(puzzle):
        for row in xrange(0, 4):
            if not puzzle[row]:
                return row, 0

            rowlen = len(puzzle[row])
            if rowlen == 4:
                continue
            else:
                return row, len(puzzle[row])

    def fill_puzzle(pieces, puzzle, piece_index):

        if not pieces:
            return puzzle

        remaining_pieces = deepcopy(pieces)
        piece_to_insert = remaining_pieces[piece_index]
        filled_puzzle = deepcopy(puzzle)
        row, column = find_next_empty(filled_puzzle)
        is_a_fit = False
        while not is_a_fit and not piece_to_insert.circle_complete:
            is_a_fit = piece_fits(piece_to_insert, filled_puzzle, row, column)
            if not is_a_fit:
                piece_to_insert.turn()
            else:
                filled_puzzle[row].append(piece_to_insert)
                print filled_puzzle
                remaining_pieces.remove(piece_to_insert)
                is_a_fit = False
                ret = fill_puzzle(remaining_pieces, filled_puzzle, 0)
                if not ret:
                    filled_puzzle[row].remove(piece_to_insert)
                    remaining_pieces.insert(piece_index, piece_to_insert)
                else:
                    return ret

        if piece_to_insert.circle_complete:
            # last piece, didn't fit
            if piece_index == len(remaining_pieces) - 1:
                return False
            else:
                return fill_puzzle(remaining_pieces, filled_puzzle, piece_index + 1)

    print fill_puzzle(pieces, puzzle, 0)

print_puzzle(PIECES)

