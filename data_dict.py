CROSS = 1
OCTAGON = 2
OUT_ARROW = 3
IN_ARROW = 4
CROSS_HOLE = -CROSS
OCTAGON_HOLE = -OCTAGON
OUT_ARROW_HOLE = -OUT_ARROW
IN_ARROW_HOLE = -IN_ARROW


class Piece(object):

    def __init__(self, top, right, left, bottom):
        super(Piece, self).__init__()
        self.top = top
        self.right = right
        self.left = left
        self.bottom = bottom
        self.flipped_horizontally = False
        self.flipped_vertically = False
        self.turn_count = 0

    def __repr__(self):
        repr_str = '\t%s\t\n%s\t\t%s\n\t%s\t' % (
            self.top, self.left, self.right, self.bottom
        )
        return repr_str

    def turn_clockwise(self):
        top = self.top
        right = self.right
        left = self.left
        bottom = self.bottom
        self.top = left
        self.left = bottom
        self.bottom = right
        self.right = top

        self.turn_count += 1

    def flip_horizontally(self):
        left = self.left
        right = self.right
        self.left = right
        self.right = left

        self.turn_count = 0
        self.flipped_horizontally = True

    def flip_vertically(self):
        top = self.top
        bottom = self.bottom
        self.top = bottom
        self.bottom = top

        self.turn_count = 0
        self.flipped_vertically = True

    def next_position(self):
        '''If the method returns False, there are no more positions to try'''
        if self.turn_count == 3 and self.flipped_horizontally and self.flipped_vertically:
            return False
        elif self.turn_count < 3:
            self.turn_clockwise()
            return True
        elif self.turn_count == 3 and not self.flipped_horizontally:
            self.turn_clockwise()
            self.flip_horizontally()
            return True
        elif self.turn_count == 3 and self.flipped_horizontally:
            self.turn_clockwise()
            self.flip_vertically()
            return True
        else:
            raise Exception('Something went wrong...')

PIECES = [
    Piece(IN_ARROW, IN_ARROW_HOLE, OUT_ARROW_HOLE, OUT_ARROW),
    Piece(IN_ARROW, OCTAGON_HOLE, OUT_ARROW_HOLE, OUT_ARROW),
    Piece(CROSS, IN_ARROW_HOLE, CROSS_HOLE, OUT_ARROW),
    Piece(IN_ARROW, CROSS_HOLE, OCTAGON_HOLE, IN_ARROW),
    Piece(OCTAGON, OCTAGON_HOLE, CROSS_HOLE, CROSS),
    Piece(OCTAGON, IN_ARROW, CROSS_HOLE, IN_ARROW),
    Piece(OUT_ARROW, OUT_ARROW_HOLE, OCTAGON_HOLE, OCTAGON),
    Piece(OCTAGON, OUT_ARROW, OUT_ARROW, CROSS),
    Piece(IN_ARROW, OUT_ARROW_HOLE, CROSS_HOLE, IN_ARROW),
    Piece(CROSS, OCTAGON_HOLE, OUT_ARROW_HOLE, OUT_ARROW),
    Piece(OUT_ARROW, CROSS_HOLE, OCTAGON_HOLE, OCTAGON),
    Piece(OCTAGON, OUT_ARROW_HOLE, OCTAGON_HOLE, OCTAGON),
    Piece(OCTAGON, OUT_ARROW_HOLE, CROSS_HOLE, IN_ARROW),
    Piece(OCTAGON, OCTAGON_HOLE, IN_ARROW_HOLE, IN_ARROW),
    Piece(IN_ARROW, OCTAGON_HOLE, CROSS_HOLE, OCTAGON),
    Piece(OUT_ARROW, IN_ARROW_HOLE, OCTAGON_HOLE, OUT_ARROW),
]

