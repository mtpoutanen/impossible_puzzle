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
            print row, column
            fits_left = (piece.left + puzzle[row][column-1]) == 0

        if piece_on_top:
            fits_top = (piece.top + puzzle[row - 1][column]) == 0

        return fits_left and fits_top

    def fill_puzzle(pieces, puzzle, piece_to_insert):
        remaining_pieces = deepcopy(pieces)
        row, column = find_next_empty(puzzle)
        for index, piece in enumerate(remaining_pieces):
            if not piece_to_insert:
                piece_to_insert = piece
            del remaining_pieces[index]
            is_a_fit = piece_fits(piece_to_insert, puzzle, row, column)
            print is_a_fit

    fill_puzzle(pieces, puzzle, None)

print_puzzle(PIECES)

