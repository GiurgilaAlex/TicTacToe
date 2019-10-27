import random

game_matrix = []
turn = 0

def set_initial_state():
    global game_matrix
    game_matrix = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]

def display_current_state():
    global game_matrix
    for item in game_matrix:
        print('|', end = '')
        for pos in item:
            print('', pos, '|', end = '')
        print('')

def check_line_if_final(line):
    return (line[0] != ' ' or line[1] != ' ' or line[2] != ' ') and line[0] == line [1] == line [2]

def check_state_if_final():
    global game_matrix
    for item in game_matrix:
        if check_line_if_final(item):
            if turn == 0:
                print("Computer won!")
            else:
                print("You won!")
            return True

    is_draw = True
    for item in game_matrix:
        for pos in item:
            if pos == ' ':
                is_draw = False

    if is_draw:
        print("It's a draw!")
        return True
    return False

def check_if_move_is_valid(x, y):
    global game_matrix
    return game_matrix[int(x)][int(y)] == ' '

def player_turn():
    global game_matrix, turn

    print("Your turn:")

    print("Line: ", end = '')
    player_move_line = input()

    print("Column: ", end = '')
    player_move_column = input()

    if check_if_move_is_valid(player_move_line, player_move_column):
        game_matrix[int(player_move_line)][int(player_move_column)] = 'X'
    turn = 1

def computer_turn():
    global game_matrix, turn
    print("Computer turn:")
    computer_move_line = random.randint(0, 2)
    computer_move_column = random.randint(0, 2)
    while not check_if_move_is_valid(computer_move_line, computer_move_column):
        computer_move_line = random.randint(0, 2)
        computer_move_column = random.randint(0, 2)

    print("Line: ", computer_move_line, '\n', end = '')
    print("Column: ", computer_move_column, '\n', end = '')
    game_matrix[computer_move_line][computer_move_column] = 'O'

    turn = 0

def game():
    global game_matrix, turn
    set_initial_state()
    display_current_state()

    while not check_state_if_final():
        if turn == 0:
            player_turn()
        else:
            computer_turn()
        display_current_state()

game()
