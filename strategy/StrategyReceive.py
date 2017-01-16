from core.Game import Game
from core.World import World
from core.Unit import Tank
from core.Player import Player
from core.Strategy import Strategy, Move

from strategy.MyStrategy import MyStrategy

class StrategyReceive(object):
    def __init__(self, socket):
        self._socket = socket
        self.strategy = MyStrategy()
        
    def move(self):
        # deserialize game, world, player, tank
        # self.strategy.move(...)
        # serialize and send move
        raise NotImplementedError()
        
    def is_running(self):
        return True