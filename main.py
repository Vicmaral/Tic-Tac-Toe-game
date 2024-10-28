import numpy as np
import random
from sys import exit

data_game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board():
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
    print('Player 1: 0 | Player 2: X\n')


def is_winner():
    if (data_game[0][0] == data_game[0][1] == data_game[0][2] != ' ') or (
            data_game[1][0] == data_game[1][1] == data_game[1][2] != ' ') or (
            data_game[2][0] == data_game[2][1] == data_game[2][2] != ' ') or (
            data_game[2][0] == data_game[1][0] == data_game[0][0] != ' ') or (
            data_game[2][1] == data_game[1][1] == data_game[0][1] != ' ') or (
            data_game[2][2] == data_game[1][2] == data_game[0][2] != ' ') or (
            data_game[0][0] == data_game[1][1] == data_game[2][2] != ' ') or (
            data_game[2][0] == data_game[1][1] == data_game[0][2] != ' '):
        return True


def board_values():
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

keys=('q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c')
ia_active = False
inputs = []
outputs = []
print("Welcome to Tic Tac Toe game\n"
      "Use your board to play\n")
instructions_board()
if input("Versus machine? Y/N ").lower() == 'y':
    ia_active = True

while len(inputs) < 9:
    input_ok = True
    if ia_active and (len(inputs) % 2 == 0):
        inputs.append(random.choice(np.setdiff1d(keys, outputs)))

    else:
        while input_ok:
            print_board()
            temp_input = input("Choose your move:").lower()
            if (temp_input not in inputs) and (temp_input in keys):
                inputs.append(temp_input)
                input_ok = False
            else:
                print("Input repeated or not valid")
    board_values()
    if is_winner():
        print("The winner is:")
        if len(inputs) % 2 == 0:
            if ia_active:
                print("Player (X) WINS!!")
            else:
                print("Player 2 (X) WINS!!")
        else:
            if ia_active:
                print("IA (0) WINS!!")
            else:
                print("Player 1 (0) WINS!!")

    if len(inputs) == 9 or is_winner():
        print_board()
        if not is_winner():
            print("Equals")

        if input("play again? Y/N ").lower() == 'y':
            inputs.clear()
            outputs.clear()
            ia_active = False
            data_game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            if input("Versus machine? Y/N ").lower() == 'y':
                ia_active = True
        else:
            print("Bye, bye!!")
            exit(0)
