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
    '''Class for modeling the puzzle pieces'''

    def __init__(self, values, order_number):
        '''
        The init method takes 2 variables. The first one is a dictionary containing
        the peg/hole values (keys being "top", "right", "bottom", and "left") and the
        second one represents the order_number in the list of pieces that the
        solver requires as an input to make physically putting the pieces together
        a little easier.
        '''

        self.top = values['top']
        self.right = values['right']
        self.bottom = values['bottom']
        self.left = values['left']
        self.order_number = order_number
        self.turn_count = 0
        self.circle_complete = False

    def __repr__(self):
        repr_str = '|top: %s, right: %s, bottom: %s, left: %s, order_number: %s|\n' % (
            names[self.top],
            names[self.right],
            names[self.bottom],
            names[self.left],
            self.order_number,
        )
        return repr_str

    def turn(self):
        '''
        Turns the piece 90 degrees clockwise by moving the values to the next "slot".
        With each turn the variable "turn_count" is incremented by one.
        Once the piece reaches 4 turns, the variable "circle_complete" is set to
        True and "turn_count" is reset to 0.
        '''
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
