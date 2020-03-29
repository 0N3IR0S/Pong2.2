class Player:
    def __init__(self, up, down, pos, score):
        self.up = up
        self.down = down
        self.pos = pos
        self.score = score


class Ball:
    def __init__(self, pos_x, pos_y, x_change, y_change):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.x_change = x_change
        self.y_change = y_change


class Options:
    def __init__(self, start_screen, finished, enter):
        self.start_screen = start_screen
        self.finished = finished
        self.enter = enter
