class Game(object):
    """Contains game state: tick"""
    NOT_STARTED = 0
    RUNNING = 1
    ENDED = 2
    CRASHED = 3

    def __init__(self):
        self.tick = 0
        self.state = Game.NOT_STARTED
