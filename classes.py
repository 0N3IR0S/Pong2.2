class Player:
    def __init__(self, name, up, down, pos, score):
        self.name = name
        self.up = up
        self.down = down
        self.pos = pos
        self.score = score


class Ball:
    def __init__(self, name, pos_x, pos_y, x_change, y_change):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.x_change = x_change
        self.y_change = y_change
