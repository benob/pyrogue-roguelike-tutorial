import rl

from map_objects.rectangle import Rect
from map_objects.tile import Tile

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.initialize_tiles()

    def initialize_tiles(self):
        self.blocked = rl.Array(self.width, self.height)
        self.block_sight = rl.Array(self.width, self.height)

        self.blocked.fill(1)
        self.block_sight.fill(1)

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.blocked[x, y] = 0
                self.block_sight[x, y] = 0

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        rooms = []
        num_rooms = 0
 
        for r in range(max_rooms):
            # random width and height
            w = rl.random_int(room_min_size, room_max_size)
            h = rl.random_int(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = rl.random_int(0, map_width - w - 1)
            y = rl.random_int(0, map_height - h - 1)
            # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)
 
            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid
 
                # "paint" it to the map's tiles
                self.create_room(new_room)
 
                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()
 
                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel
 
                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
 
                    # flip a coin (random number that is either 0 or 1)
                    if rl.random_int(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
 
                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1


    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.blocked[x, y] = 0
            self.block_sight[x, y] = 0
 
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.blocked[x, y] = 0
            self.block_sight[x, y] = 0

    def is_blocked(self, x, y):
        return self.blocked[x, y] == 1
