from copy import deepcopy
from data_dict import PIECES


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

        piece_to_insert = pieces[piece_index]
        row, column = find_next_empty(puzzle)
        is_a_fit = False

        while not is_a_fit and not piece_to_insert.circle_complete:
            is_a_fit = piece_fits(piece_to_insert, puzzle, row, column)
            if is_a_fit:
                remaining_pieces = deepcopy(pieces)
                filled_puzzle = deepcopy(puzzle)
                filled_puzzle[row].append(deepcopy(piece_to_insert))
                del remaining_pieces[piece_index]
                ret = fill_puzzle(remaining_pieces, filled_puzzle, 0)

                if not ret:
                    is_a_fit = False
                    piece_to_insert.circle_complete = False
                else:
                    return ret

            piece_to_insert.turn()

        piece_to_insert.circle_complete = False

        if piece_index == len(pieces) - 1:
            return False
        else:
            return fill_puzzle(pieces, puzzle, piece_index + 1)
        raise Exception('should never get here')

    solved_puzzle = fill_puzzle(pieces, puzzle, 0)
    for index, row in enumerate(solved_puzzle):
        print "row %s: %s" % (index + 1, row)

print_puzzle(PIECES)

