"""
TIC TAC TOE!
"""
#from IPython.display import clear_output
import random

def display_board(a,b):
#    clear_output()
    print('\n'*100)
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')
    
    
def place_marker(avail,board, marker, position):
    board[position] = marker
    avail[position] = ' '
    
def win_check(board, mark):
    return ((board[7]==board[8]==board[9] and board[7]==mark) or
    (board[4]==board[5]==board[6] and board[4]==mark) or
    (board[1]==board[2]==board[3] and board[1]==mark) or
    (board[7]==board[4]==board[1] and board[7]==mark) or
    (board[8]==board[5]==board[2] and board[8]==mark) or
    (board[9]==board[6]==board[3] and board[9]==mark) or
    (board[7]==board[5]==board[3] and board[7]==mark) or
    (board[9]==board[5]==board[1] and board[1]==mark))    
    
def random_player():
    return random.choice((-1,1))
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board,player):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        try:
            position = int(input('Player %s, choose your next position: (1-9) \n'%(player)))
        except:
            print("I'm sorry, please try again.\n")
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: \n').lower().startswith('y')

while True:
    print('Welcome to Tic Tac Toe!\n')
    board = [' ']*10
    available = [str(num) for num in range(0,10)]
    players = [0,'X','O']
    
    toggle = random_player()
    player = players[toggle]
    
    game_on = True
    input('Hit Enter to start\n')
    while game_on:
        display_board(available,board)
        position = player_choice(board,player)
        place_marker(available,board,player,position)
        
        if win_check(board,player):
            display_board(available,board)
            print('Congratulations! Player '+player+' wins!\n')
            game_on = False
        else:
            if full_board_check(board):
                display_board(available,board)
                print('The game is draw\n')
                break
            else:
                toggle*=-1
                player = players[toggle]
    
    if not replay():
        break