from core.Utility import object_from_dict


class Game(object):
    """Contains game state: tick"""
    NOT_STARTED = 0
    RUNNING = 1
    ENDED = 2
    CRASHED = 3

    def __init__(self):
        self.tick = 0
        self.state = Game.NOT_STARTED

    @staticmethod
    def from_dict(settings):
        game = Game()
        return object_from_dict(game, settings)
