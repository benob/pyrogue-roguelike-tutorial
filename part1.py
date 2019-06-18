import rl

from part1_input_handlers import handle_keys

def update(event):
    global font, player_x, player_y

    if event > 0:
        action = handle_keys(event)
        move = action.get('move')
        exit = action.get('exit')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy
        if exit:
            rl.quit()

    rl.clear()
    rl.draw_tile(font, player_x * font.tile_width, player_y * font.tile_height, ord('@'))

def main():
    global font, player_x, player_y

    screen_width = 80
    screen_height = 50

    player_x = screen_width // 2
    player_y = screen_height // 2

    font = rl.Image('arial_32x32.png', 32, 32)

    rl.init_display('libtcod tutorial revised', screen_width * font.tile_width, screen_height * font.tile_height)
    rl.run(update)

if __name__ == '__main__':
    main()
