import json

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
        self._running = True
        
    def move(self):
        game_set, world_set, player_set, tank_set = json.loads(self._socket.recv(1024).decode())
        game = Game.from_dict(game_set)
        world = World.from_dict(world_set)
        player = Player.from_dict(player_set)
        tank = Tank.from_dict(tank_set)
        move = Move()
        self.strategy.move(game, world, player, tank, move)
        self._socket.send(json.dumps(move.__dict__).encode())
        self._running = False
        
    def is_running(self):
        return self._running
