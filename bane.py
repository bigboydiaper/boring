print('Welcome to Tic Tac Toe')
name = input('Please enter your avatard\'s callsign: ')

print('Welcome ' + name + '!')

print('Choose your marker: X or O')
marker = input('(Enter X or O):')

if not (marker == 'X' or marker == 'O'):
    marker = input('Invalid selection, re enter your choice X or O: ')

print('Great!  You have chosen ' + marker + "!")

if marker == 'X':
    print('You will be X.')
    print('The computer will be O.')
else:
    print('You will be O.')
    print('The computer will be X.')

# board spaces defined as a nested list of cartesian coordinates

x1y1 = '?'
x1y2 = '?'
x1y3 = '?'
x2y1 = '?'
x2y2 = '?'
x2y3 = '?'
x3y1 = '?'
x3y2 = '?'
x3y3 = '?'

game_board = [[x1y1, x1y2, x1y3], [x2y1, x2y2, x2y3], [x3y1, x3y2, x3y3]]


# def a function which displays the currents state of the board using the data set game_board

def display_board(game_board_input):
    print(game_board_input[0][0] + '|' + game_board_input[0][1] + '|' + game_board_input[0][2])
    print('------')
    print(game_board_input[1][0] + '|' + game_board_input[1][1] + '|' + game_board_input[1][2])
    print('------')
    print(game_board_input[2][0] + '|' + game_board_input[2][1] + '|' + game_board_input[2][2])


display_board(game_board)

print('Roll to see who goes first.')

player_roll = input('Type \'roll\' to roll the dice: ')
if player_roll != 'roll':
    player_roll = input('Invalid entry.  Type \'roll\' to roll the dice: ')

import random

player_roll = random.randint(1, 100)
comp_roll = random.randint(1, 100)
print(name + ' rolled a ' + str(player_roll) + ".")
print('Skynet rolled a ' + str(comp_roll) + ".")

# define a variable in the if statement that equals 1 if it is the player's turn.
# equals zero if it is the computer's turn

if player_roll >= comp_roll:
    print('Congratulations.  You won the roll.  You will go first.')
    turn = 1
else:
    print('Skynet won the roll.  Skynet will go first.')
    turn = 0


# create the function loop for the player's turn

def player_turn(z):
    turn_row = input('Please make your move.  Choose the row you would like to mark (top, middle, bottom): ')
    if not input == ('top' or 'middle' or 'bottom'):
        turn_row = input(
            'Invalid entry.  Please make your move.  Choose the row you would like to mark (top, middle, bottom): '
        )
    turn_column = input(
        'Please make your move.  Choose the column you would like to mark (left, middle, right): '
    )
    if not input == ('left' or 'middle' or 'right'):
        turn_row = input(
            'Invalid entry.  Please make your move.  Choose the row you would like to mark (top, middle, bottom): '
        )
    if turn_row == 'top':
        turn_index = [0]
    elif turn_row == 'middle':
        turn_index = [1]
    else:
        turn_index = [2]

    if turn_column == 'left':
        turn_index.append(0)
    elif turn_column == 'middle':
        turn_index.append(1)
    else:
        turn_index.append(2)

    return turn_index

# create the while loop for the computer's turn
