import numpy as np

data_game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board():
    print("\n\n")
    print(data_game[0][0], ' | ', data_game[0][1], ' | ', data_game[0][2])
    print("--------------")
    print(data_game[1][0], ' | ', data_game[1][1], ' | ', data_game[1][2])
    print("--------------")
    print(data_game[2][0], ' | ', data_game[2][1], ' | ', data_game[2][2])


def instructions_board():
    print('Q', ' | ', 'W', ' | ', 'E')
    print("--------------")
    print('A', ' | ', 'S', ' | ', 'D')
    print("--------------")
    print('Z', ' | ', 'X', ' | ', 'C')


def board_values():
    print(inputs)
    print(outputs)
    print(np.setdiff1d(inputs, outputs))
    for x in np.setdiff1d(inputs, outputs):
        if x == 'q' and (len(inputs) % 2 == 0):
            data_game[0][0] = ' X'
        elif x == 'q':
            data_game[0][0] = ' 0'
        if x == 'w' and (len(inputs) % 2 == 0):
            data_game[0][1] = ' X'
        elif x == 'w':
            data_game[0][1] = ' 0'
        if x == 'e' and (len(inputs) % 2 == 0):
            data_game[0][2] = ' X'
        elif x == 'e':
            data_game[0][2] = ' 0'
        if x == 'a' and (len(inputs) % 2 == 0):
            data_game[1][0] = ' X'
        elif x == 'a':
            data_game[1][0] = ' 0'
        if x == 's' and (len(inputs) % 2 == 0):
            data_game[1][1] = ' X'
        elif x == 's':
            data_game[1][1] = ' 0'
        if x == 'd' and (len(inputs) % 2 == 0):
            data_game[1][2] = ' X'
        elif x == 'd':
            data_game[1][2] = ' 0'
        if x == 'z' and (len(inputs) % 2 == 0):
            data_game[2][0] = ' X'
        elif x == 'z':
            data_game[2][0] = ' 0'
        if x == 'x' and (len(inputs) % 2 == 0):
            data_game[2][1] = ' X'
        elif x == 'x':
            data_game[2][1] = ' 0'
        if x == 'c' and (len(inputs) % 2 == 0):
            data_game[2][2] = ' X'
        elif x == 'c':
            data_game[2][2] = ' 0'
    outputs.append(np.setdiff1d(inputs, outputs))


turns = 10
inputs = []
outputs = []
print("Welcome to Tic Tac Toe game\n"
      "Use your board to play\n")
instructions_board()
while turns > 0:

    print_board()

    temp_input = input("Choose your move:").lower()
    if (temp_input in inputs) or (temp_input not in ('q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c')):
        temp_input = input("Choose your move:(not in used and correct)")
    else:
        inputs.append(temp_input)

    board_values()
    print_board()
    if turns == 1:
        if input("play again? Y/N ") == 'Y':
            turns = 9
            inputs.clear()
            outputs.clear()
