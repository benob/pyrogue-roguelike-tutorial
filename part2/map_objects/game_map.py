import rl

from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.initialize_tiles()

    def initialize_tiles(self):
        self.blocked = rl.Array(self.width, self.height)
        self.block_sight = rl.Array(self.width, self.height)

        self.blocked[30, 22] = 1
        self.blocked[31, 22] = 1
        self.blocked[32, 22] = 1

        self.block_sight[30, 22] = 1
        self.block_sight[31, 22] = 1
        self.block_sight[32, 22] = 1

    def is_blocked(self, x, y):
        return self.blocked[x, y] == 1
