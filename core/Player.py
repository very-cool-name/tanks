from core.Utility import object_from_dict


class Player(object):
    """Player class. Contains id, given by engine."""
    def __init__(self, player_id):
        self.player_id = player_id

    def is_enemy(self, player_id):
        return self.player_id != player_id

    @staticmethod
    def from_dict(settings):
        player = Player(-1)
        return object_from_dict(player, settings)
