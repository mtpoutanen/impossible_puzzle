CROSS = 1
OCTAGON = 2
OUT_ARROW = 3
IN_ARROW = 4
CROSS_HOLE = -CROSS
OCTAGON_HOLE = -OCTAGON
OUT_ARROW_HOLE = -OUT_ARROW
IN_ARROW_HOLE = -IN_ARROW

names = {
    CROSS: 'cross',
    OCTAGON: 'octagon',
    OUT_ARROW: 'out_arrow',
    IN_ARROW: 'in_arrow',
    CROSS_HOLE: 'cross_hole',
    OCTAGON_HOLE: 'octagon_hole',
    OUT_ARROW_HOLE: 'out_arrow_hole',
    IN_ARROW_HOLE: 'in_arrow_hole',
}


class Piece(object):

    def __init__(self, top, right, bottom, left):
        super(Piece, self).__init__()
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.turn_count = 0
        self.circle_complete = False

    def __repr__(self):
        repr_str = '|top: %s, right: %s, bottom: %s, left: %s|\n' % (
            names[self.top],
            names[self.right],
            names[self.bottom],
            names[self.left],
        )
        return repr_str

    def turn(self):
        top = self.top
        right = self.right
        left = self.left
        bottom = self.bottom
        self.top = left
        self.left = bottom
        self.bottom = right
        self.right = top

        self.turn_count += 1
        # print self.turn_count
        if self.turn_count >= 4:
            self.circle_complete = True
            self.turn_count = 0


PIECES = [
    Piece(OCTAGON, CROSS, IN_ARROW_HOLE, OCTAGON_HOLE),
    Piece(IN_ARROW, OUT_ARROW, OUT_ARROW_HOLE, OCTAGON_HOLE),
    Piece(OUT_ARROW, OCTAGON, OCTAGON_HOLE, OUT_ARROW_HOLE),
    Piece(OCTAGON, IN_ARROW, OCTAGON_HOLE, CROSS_HOLE),

    Piece(OCTAGON, CROSS, OUT_ARROW_HOLE, OUT_ARROW_HOLE),
    Piece(IN_ARROW, CROSS, OUT_ARROW_HOLE, IN_ARROW_HOLE),
    Piece(IN_ARROW, IN_ARROW, OUT_ARROW_HOLE, CROSS_HOLE),
    Piece(IN_ARROW, IN_ARROW, OCTAGON_HOLE, CROSS_HOLE),

    Piece(OCTAGON, OCTAGON, OCTAGON_HOLE, OUT_ARROW_HOLE),
    Piece(OCTAGON, CROSS, CROSS_HOLE, OCTAGON_HOLE),
    Piece(OUT_ARROW, OCTAGON, OCTAGON_HOLE, CROSS_HOLE),
    Piece(CROSS, OUT_ARROW, OUT_ARROW_HOLE, OCTAGON_HOLE),

    Piece(OCTAGON, IN_ARROW, CROSS_HOLE, IN_ARROW_HOLE),
    Piece(CROSS, OUT_ARROW, CROSS_HOLE, IN_ARROW_HOLE),
    Piece(OCTAGON, IN_ARROW, IN_ARROW_HOLE, OUT_ARROW_HOLE),
    Piece(OUT_ARROW, OUT_ARROW, OCTAGON_HOLE, IN_ARROW_HOLE),
]

