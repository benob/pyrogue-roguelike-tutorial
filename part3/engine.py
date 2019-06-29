import rl

from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import render_all

screen_width = 80
screen_height = 50
map_width = 80
map_height = 45
room_max_size = 10
room_min_size = 6
max_rooms = 30

colors = {
    'dark_wall': rl.color(0, 0, 100),
    'dark_ground': rl.color(50, 50, 150)
}

rl.init_display('libtcod tutorial revised', screen_width * 32, screen_height * 32)

player = Entity(screen_width // 2, screen_height // 2, '@', rl.WHITE)
npc = Entity(screen_width // 2 - 5, screen_height // 2, '@', rl.YELLOW)
entities = [npc, player]

game_map = GameMap(map_width, map_height)
game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)

def update(event):
    render_all(entities, game_map, screen_width, screen_height, colors)

    action = handle_keys(event)

    move = action.get('move')
    exit = action.get('exit')

    if move:
        dx, dy = move

        if not game_map.is_blocked(player.x + dx, player.y + dy):
            player.move(dx, dy)

    if exit:
        rl.quit()

rl.run(update)

