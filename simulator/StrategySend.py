import json

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
        to_serialize = [game, world, player, tank]
        data = '[{}]'.format(','.join([json.dumps(x.__dict__) for x in to_serialize]))
        self._socket.send(data.encode())
        move_set = json.loads(self._socket.recv(1024).decode())
        move = Move.from_dict(move_set)
