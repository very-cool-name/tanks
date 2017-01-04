class Player(object):
    """Player class. Contains id, given by engine."""
    def __init__(self, player_id):
        self.player_id = player_id

    def is_enemy(self, player_id):
        return self.player_id != player_id
