import random

def startgame():
    #init the board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    drawboard(board)
    #pick the first player
    player = random.choice(['X', 'O'])
    print("Player " + player + " goes first")
    
    #turn
    while(player_turn(board, player)):
        drawboard(board)
        #if the game isnt over yet, switch the player
        if (player == 'X'):
            player = "O"
        else:
            player = 'X'
    

def player_turn(board, player):
    print("Player " + player + " turn")
    collect_input(board, player)
    if(check_for_wins(board) or check_if_board_full(board)):
        print("Game over")
        return False
    else:
        print("Game not over yet!")
        return True

def drawboard(board):
    count = 0
    print("  a   b   c ")
    for row in board:
        print(str(count) + ":" + row[0] + " | " + row[1] + " | " + row[2])
        if (count < 2):
            print("  ---------")
            count += 1
    
def collect_input(board, player):
    column = input("Select a column:")
    column = column.lower()
    if column in ['a', 'b', 'c']:
        #ask for the row
        row = input("Select a row:")
        if row in ['0', '1', '2']:
            place_character(board, player, row, column)
        else:
            print("Invalid input. Try again.")
            collect_input(board, player)
    else:
        print("Invalid input. Try again.")
        collect_input(board, player)
        
def place_character(board, player, row, column):
    column = ord(column) - 97
    row = int(row)
    if (board[row][column] == ' '):
        board[row][column] = player
    else:
        print("Location is occupied. Try again.")
        collect_input(board, player)

def check_for_wins(board):
    if(check_across(board) or check_down(board) or check_diagonal(board)):
        print("You win!")
        return True
    else:
        print("No wins yet")
        return False
        
def check_across(board):
    for row in board:
        if(row[0] == row[1] == row[2]):
            if (row[0] != ' '):
                print("Player " + row[0] + " wins across")
                return True
    return False
    
def check_down(board):
    i = 0
    while i < 3:
        if(board[i][0] == board[i][1] == board[i][2]):
            if board[i][0] != ' ':
                print("Player " + board[i][0] + " wins down")
                return True
        i += 1
    return False

def check_diagonal(board):
    if board[1][1] == ' ':
        return False
    else:
        if(board[0][0] == board[1][1] == board[2][2]):
            print("Player " + board[1][1] + " wins diagonal")  
            return True
        elif(board[0][2] == board[1][1] == board[2][0]):
            print("Player " + board[1][1] + " wins diagonal")
            return True
        else:
            return False
            
def check_if_board_full(board):
    for row in board:
        if ' ' in row:
            #print("Still space on the board")
            return False
    print("Board full")
    return True

#board0 = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#board1 = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
#board2 = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']]
#board3 = [['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']]
#board4 = [['O', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'O']]

startgame()

#drawboard(board0)
#player_turn(board0, 'X')
#drawboard(board0)
#drawboard(board0)
#collect_input(board0, 'X')
#drawboard(board0)
#check_for_wins(board0)
#check_for_wins(board1)
#check_for_wins(board3)
#check_for_wins(board4)
#check_if_board_full(board0)
#check_if_board_full(board1)
#check_if_board_full(board2)
#check_if_board_full(board3)
#check_if_board_full(board4)
