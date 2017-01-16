from core.Game import Game
from core.World import World
from core.Unit import Tank
from core.Player import Player
from core.Strategy import Strategy, Move

class StrategySend(Strategy):
    """Strategy, which is connected over socket to some clent, doing real work."""
    def __init__(self, socket, address):
        self._socket = socket
        self.address = address
        
    def move(self, game: Game, world: World, player: Player, tank: Tank, move: Move):
        # serialize game, world, player, tank
        # send over socket
        # wait till receive move
        raise NotImplementedError()