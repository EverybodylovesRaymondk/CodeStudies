# Mile stone project 1

#########################################################################

def display_board(board):
    '''
    The function will create a 3 x 3 board and populate each section with a value as indexed from the test_board variable.
    '''
    print('\n' * 100)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = [' '] * 10
test_board2 = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

#Look at pyQT / QTDesigner

# Test display board
# display_board(test_board)

#########################################################################

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


##Test player imput
# player1_marker , player2_marker = player_input()
# print(player1_marker,player2_marker)

#########################################################################

def place_marker(board, marker, position):
    board[position] = marker


# Test place marker
# place_marker(test_board,'X',6)
# display_board(test_board)

#########################################################################

def win_check(board, mark):
    return (
        # Horisontal
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # Top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # Middle
            (board[3] == mark and board[2] == mark and board[1] == mark) or  # Bottom
            # Vertical
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # Right
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # Middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # Left
            # Diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark) or  # Top right to bottom left
            (board[7] == mark and board[5] == mark and board[3] == mark)  # Top left to bottom right
    )


# Test of win check
# display_board(test_board)
# print(win_check(test_board,'x'))

#########################################################################

import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


##Test choose first
# print(choose_first())

#########################################################################

def space_check(board, position):
    return board[position] == ' '


#########################################################################

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


#########################################################################

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


#########################################################################

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


#########################################################################

# while loop to keep running the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


