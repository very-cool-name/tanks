import json
import socket
import threading
import sys

from core.Player import Player
from core.Strategy import DummyStrategy, Move
from core.Game import Game
from core.World import World
from core.Unit import Tank
from core.Player import Player

from simulator.StrategySend import StrategySend

class Settings(object):
    """Settings of launch, loaded from json file."""
    class StrategyType(object):
        DUMMY = 'DUMMY'
        NETWORK = 'NETWORK'

    def __init__(self, settings):
        self.players = []  # should be one of StrategyType
        self.round_ticks = 0
        self.strategy_timeout = 0  # in seconds
        for key in self.__dict__.keys():  # fill only above mentioned names
            if key in settings:
                setattr(self, key, settings[key])
        self._verify_settings()
                
    def _verify_settings(self):
        if len(self.players) < 2:
            raise ValueError('There should be at least two players (players option)')
        if self.round_ticks < 1:
            raise ValueError('Round should have length at least 1 tick (round_ticks option)')
        if self.strategy_timeout < 30:
            raise ValueError('Strategy timeout should be at least 30 sec (strategy_timeout option)')
        if self.strategy_timeout > 60 * 10:
            raise ValueError('Strategy timeout should be no more than 10 min (strategy_timeout option)')
        

class Simulator(object):
    """Holds game logics, and all machinery with connections and simulations.
    Must be splited to less responsible classes."""
    def __init__(self, json_settings_name):
        settings_file = open(json_settings_name)
        self.settings = Settings(json.load(settings_file))
        self.connector_socket = None
        self.players = {}
        self.strategies = {}
        self.world = World()
        self.game = Game()
        
    def run(self):
        self._initialize_players()
        self._make_moves()
        
    def _initialize_players(self):
        connector_threads = []
        next_id = 0
        network_players = self.settings.players.count(Settings.StrategyType.NETWORK)
        if network_players > 0:
            self.connector_socket = socket.socket()
            self.connector_socket.bind(('', 8080))
            self.connector_socket.settimeout(60)
            self.connector_socket.listen(network_players)
        for strategy_type in self.settings.players:
            id = next_id
            next_id += 1
            self.players[id] = Player(id)
            if strategy_type == Settings.StrategyType.DUMMY:
                self.strategies[id] = DummyStrategy()
            elif strategy_type == Settings.StrategyType.NETWORK:
                connector_threads.append(threading.Thread(target=self._new_network_strategy, args=(id,), daemon=True))
                connector_threads[-1].start()
        for thread in connector_threads:
            thread.join(60)
        self.connector_socket.close()
        if any(t.is_alive() for t in connector_threads):
            raise RuntimeError("Could not connect network players in 1 min interval.")
                
    def _new_network_strategy(self, id):
        socket, address = self.connector_socket.accept()
        self.strategies[id] = StrategySend(socket, address)  # should be thread safe

    def _make_moves(self):
        self.game.state = Game.RUNNING
        for i in range(self.settings.round_ticks):
            moves = {}
            for id, strategy in self.strategies.items():
                move = Move()
                tank = Tank(0, 0, 0, 0, id)  # TODO obviously tank should be somewhere else
                # starting in notherthread alows us to make time limit
                move_runner = threading.Thread(target=strategy.move, args=(self.game, self.world, self.players[id], tank, move))
                move_runner.start()
                move_runner.join(self.settings.strategy_timeout)
                moves[id] = move
        self.game.state = Game.ENDED
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Pass settings file name as first argument, pelase')
        sys.exit(1)
    simulator = Simulator(sys.argv[1])
    simulator.run()