import rl

from part1_input_handlers import handle_keys

def update(event):
    global console, font, player_x, player_y

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

    console.fill(0)
    console[player_x, player_y] = ord('@') - 32

    rl.draw_array(console, font, 0, 0)

def main():
    global console, font, player_x, player_y

    screen_width = 80
    screen_height = 50

    player_x = screen_width // 2
    player_y = screen_height // 2

    font = rl.Image('arial10x10.png', 10, 10)

    rl.init_display('libtcod tutorial revised', screen_width * 10, screen_height * 10)

    console = rl.Array(screen_width, screen_height)

    rl.run(update)

if __name__ == '__main__':
    main()
