from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[7]+' | '+board[8]+' | '+board[9])
def player_input():
    
    '''
    Output = (player1 marker , player 2 marker)
    '''
    
    marker = ''
    #keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O:').upper()
    
    
    #assign player 2 the opposite marker
    player1 =marker
    
    
    if player1 == 'X':
        player2= 'O'
    else:
        player2 = 'X'
    
    
    return (player1,player2)
def place_marker(board, marker , position):
    
    board[position] = marker
def win_check(board,mark):
    #Win tic tac toe
    
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def space_check(board, position):
    
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board full
    return True
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    
    choice = input('play again? Enter Yes or No')
    
    return choice == 'Yes'
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
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
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break 
