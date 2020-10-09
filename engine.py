from util import key_pressed
from pynput.keyboard import Listener


def create_board(width, height):
    board = []
    upper = ['$'] * width

    for row in range(height):
        line = []
        if row == 0 or row == height - 1:

            line.append(upper)
        else:
            for col in range(width):
                if col == 0 or col == width - 1:
                    line.append('$')
                else:
                    # if col == 5 and row  == 5:
                    #     print(col)
                    #     line.append('P')
                    #     print(line)
                    # else:
                    line.append('.')
        if type(line[0]) == list:
            line = line[0]
        board.append(line)

    return board


# print(create_board(10,10))

b = create_board(15, 15)

for i in b:
    print(i)


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''

    board[player['y']][player['x']] = player['icon']
    return board


p = {'icon': 'P', 'x': 8, 'y': 3}
print(p)
test = put_player_on_board(b, p)
for i in test:
    print(i)


def move_player(board, move):
    pos = [p['y'], p['x']]
    new = [p['y'] + move[0], p['x'] + move[1]]
    try:
        board[new[0]][new[1]] = p['icon']
        board[pos[0]][pos[1]] = '.'
        p['y'] = new[0]
        p['x'] = new[1]

    except ValueError:
        pass
    return board


def run(key):
    global b
    print(p)

    key = str(key)[1]

    print(key)
    if key in ['w', 'a', 's', 'd']:
        move = [0, 0]
        if key == 'w':
            move = [-1, 0]
        elif key == 'a':
            move = [0, -1]
        elif key == 's':
            move = [1, 0]
        elif key == 'd':
            move = [0, 1]

        b = move_player(b, move)
        for i in b:
            print(i)


with Listener(
        on_press=run) as listener:
    listener.join()
