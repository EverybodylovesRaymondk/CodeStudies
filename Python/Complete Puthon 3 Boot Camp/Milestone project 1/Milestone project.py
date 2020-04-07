# Mile stone project 1
def display_board(board):
    ''' The function will create a 3 x 3 board and populate each section with a value as indexed from the test_board variable '''
    print('\n'*1)
    print("\033[4mStart tick tack toe\033[0m")
    print (board[6]+ ' | ' + board[7] + ' | ' + board[8])
    print (board[3]+ ' | ' + board[4] + ' | ' + board[5])
    print (board[0]+ ' | ' + board[1] + ' | ' + board[2])

test_board = ['','','','','','','','','']  

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 : Do you want to be X or O ? ').upper()
    if marker =='X' :
        return ('x','O')
    else:
        return ('O','X')
print(player_input())

def place_marker(board,marker,position):
    board[position]=marker

place_marker(test_board,'X',8)
display_board(test_board)

def win_check(board,mark):
    return (
            #Horisontal
            (board[6] == mark and board[7] == mark and board[8] == mark) or #Top
            (board[5] == mark and board[4] == mark and board[3] == mark) or #Middle
            (board[2] == mark and board[1] == mark and board[0] == mark) or #Bottom
            #Vertical
            (board[8] == mark and board[5] == mark and board[2] == mark) or #Right
            (board[7] == mark and board[4] == mark and board[1] == mark) or #Middle
            (board[6] == mark and board[3] == mark and board[0] == mark) or #Left
            #Diagonal
            (board[8] == mark and board[4] == mark and board[0] == mark) or #Top right to bottom left
            (board[6] == mark and board[4] == mark and board[2] == mark) # Top left to bottom right
            )