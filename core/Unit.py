"""Multiple inheritance structure of all this is bad, but it is cheap and fast.
LivingUnit and player_id should really be properties, with appropriate visitors.
"""

from core.Utility import object_from_dict


class Unit(object):
    """Something placed in the world"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MovingUnit(Unit):
    """Something that is moving"""
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y)
        self.vx = vx
        self.vy = vy


class LivingUnit(Unit):
    """Something, that has hp"""
    def __init__(self, x, y, hp):
        super().__init__(x, y)
        self.hp = hp


class Shell(MovingUnit):
    """Tank shell. Moves and id of player-creator"""
    def __init__(self, x, y, vx, vy, player_id):
        super().__init__(x, y, vx, vy)
        self.player_id = player_id


class Tank(MovingUnit):
    """Tank. Moves, has 1 hp and has player_id"""
    HP = 1
    MAX_V = 1

    def __init__(self, x, y, vx, vy, player_id):
        MovingUnit.__init__(self, x, y, vx, vy)
        self.player_id = player_id
        self.hp = Tank.HP

    @staticmethod
    def from_dict(settings):
        tank = Tank(None, None, None, None, None)
        return object_from_dict(tank, settings)
