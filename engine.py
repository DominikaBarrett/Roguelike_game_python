def create_board(width, height):
    board = []
    upper =['@']* width

    for row in range(height):
        line =[]
        if row == 0 or row == height -1:
            line.append(upper)
            print(row)
        else:
            for col in range(width):
                if col ==0 or col == width -1:
                    line.append('@')
                    print(line)
                else:
                    if col == 5 and row  == 5:
                        line.append('-')
                        print(line)
                    else:
                        line.append('.')
    board.append(line)
print(create_board(4,6))
#     # return board
    # pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
