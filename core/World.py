from core.Utility import object_from_dict


class World(object):
    """Holds information about world: map, tanks position"""
    def __init__(self):
        self.tanks = []
        self.map = []
        self.width = 0
        self.height = 0

    def is_free(self, x, y):
        """Returns if (x, y) is free of object"""
        raise NotImplementedError()

    @staticmethod
    def from_dict(settings):
        world = World()
        return object_from_dict(world, settings)
