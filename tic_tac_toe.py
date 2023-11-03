import os

# Constants for game state
Win = 1
Draw = -1
Running = 0
Stop = 1

# Initialize the game state and the board
board = [' '] * 10  # Using a 1-based index for easier checking
player = 1
Game = Running
Mark = 'X'

def draw_board():
    print(' %c | %c | %c ' % (board[1], board[2], board[3]))
    print("____________")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("____________")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print('\n')

def check_position(x):
    return board[x] == ' '

def check_win():
    global Game

    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != ' ':
            Game = Win
            return

    if ' ' not in board[1:10]:
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe")
print("Player 1 [X] --- Player 2 [O]\n")

while Game == Running:
    draw_board()

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    choice = int(input('Enter the position between [1-9] where you want to mark: \n'))
    print('\n')
    if 1 <= choice <= 9 and check_position(choice):
        board[choice] = Mark
        player += 1
        check_win()

if Game == Draw:
    print("Game Draw")
else:
    winner = "Player 1" if player % 2 == 0 else "Player 2"
    print(f"{winner} Won")
