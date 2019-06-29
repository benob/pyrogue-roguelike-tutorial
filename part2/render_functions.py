import rl

tiles = rl.Image('arial_32x32.png', 32, 32)

def render_all(entities, game_map, screen_width, screen_height, colors):
    rl.clear()
    # Draw all the tiles in the game map
    '''for y in range(game_map.height):
        for x in range(game_map.width):
            #wall = game_map.tiles[x][y].block_sight
            wall = True

            if wall:
                #rl.draw_tile(tiles, x * 32, y * 32, ord('#'), 0, colors.get('dark_wall'))
                rl.draw_tile(tiles, x * 32, y * 32, ord('#'), 0, rl.RED)
            else:
                rl.draw_tile(tiles, x * 32, y * 32, ord('.'), 0, rl.BLUE)
                '''
    rl.draw_array(game_map.blocked, tiles, 0, 0, mapping=[ord('.'), ord('#')])

    # Draw all entities in the list
    for entity in entities:
        draw_entity(entity)


def draw_entity(entity):
    rl.draw_tile(tiles, entity.x * 32, entity.y * 32, ord(entity.char), entity.color)

