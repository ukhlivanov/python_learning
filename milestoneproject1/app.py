def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if(board[1]==board[2]==board[3]==mark): return True
    if(board[4]==board[5]==board[6]==mark): return True
    if(board[7]==board[8]==board[9]==mark): return True

    if(board[1]==board[4]==board[7]==mark): return True
    if(board[2]==board[5]==board[8]==mark): return True
    if(board[3]==board[6]==board[9]==mark): return True

    if(board[3]==board[5]==board[7]==mark): return True
    if(board[1]==board[5]==board[9]==mark): return True


import random

def choose_first():
    return ('Player{n}'.format(n=random.randint(1,2)))


def space_check(board, position):
    return board[position]==' '


def full_board_check(board):
        return ' ' not in board


def player_choice(board):
    position = 0

    while True:
        position = input('Choose your next position: (1-9) ')
        is_available = space_check(board, int(position))
        is_correct = int(position) in [1,2,3,4,5,6,7,8,9]
        if( is_correct == True and is_available == True) : break

    return int(position)

def replay():
    return input("Again?").lower().startswith('y')


def tic_tac_toe():

    while True:

        print('Welcome to Tic Tac Toe!')
        board = [' ']*10
        board[0] = '$'
        player1_marker, player2_marker = player_input()

        turn = choose_first()

        print(turn + " will go first!")

        while True:
            ready = input('Are you ready to play? (Yes or No)').lower()
            if(ready.startswith('y') or ready.startswith('n')): break

        if(ready[0]=='y'): game_on = True
        else: game_on = False
        
        print(turn)
    

        while game_on:
            if(turn == 'Player1'):
                print(turn)
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_marker, position)

                if(win_check(board, player1_marker)):
                    display_board(board)
                    print("Player 1 won!")
                    game_on = False
                else: 
                    if(full_board_check(board)):
                        display_board(board)
                        print("Draw!")
                        break;
                    else: turn = 'Player2'
            else:

                print(turn)
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)

                if(win_check(board, player2_marker)):
                    display_board(board)
                    print("Player 2 won!")
                    game_on = False
                else: 
                    if(full_board_check(board)):
                        display_board(board)
                        print("Draw!")
                        break
                    else: turn = 'Player1'
 
        if(not replay()): break
    

tic_tac_toe()