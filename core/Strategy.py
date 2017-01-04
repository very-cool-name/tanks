from abc import ABC, abstractmethod

from core.Game import Game
from core.World import World
from core.Unit import Tank
from core.Player import Player


class Move(object):
    """Players choice.
    Default action is do nothing. If action is:
        Move.Movement - engine sets the vx and vy of players tank. vx and vy are truncated to Tank.MAX_V
        Move.SHOOT - parameters are ignored.
    """
    NONE = 0
    MOVEMENT = 1
    SHOOT = 2

    def __init__(self):
        self.action = Move.NONE
        self.vx = 0
        self.vy = 0


class Strategy(ABC):
    @abstractmethod
    def move(self, game: Game, world: World, player: Player, tank: Tank, move: Move):
        """Core method of strategy. Should fill move to appropriate state."""
        pass
