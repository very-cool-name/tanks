from core.Player import Player
from core.Game import Game
from core.World import World
from core.Unit import Tank
from core.Strategy import Strategy, Move


class MyStrategy(Strategy):
    def move(self, game: Game, world: World, player: Player, tank: Tank, move: Move):
        """Fill move here."""
        pass
