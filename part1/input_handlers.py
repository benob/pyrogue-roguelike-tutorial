import rl

def handle_keys(key):
    # Movement keys
    if key == rl.UP:
        return {'move': (0, -1)}
    elif key == rl.DOWN:
        return {'move': (0, 1)}
    elif key == rl.LEFT:
        return {'move': (-1, 0)}
    elif key == rl.RIGHT:
        return {'move': (1, 0)}

    elif key == rl.ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}

