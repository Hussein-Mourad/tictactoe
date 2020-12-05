from tictactoe import *

board = initial_state()

board[0][0] = X
board[0][1] = O
board[0][2] = X
board[1][0] = O
board[1][1] = X
board[1][2] = O
board[2][0] = X
board[2][1] = O
board[2][2] = X

for i in range(3):
    print(board[i])
print(f"Player's turn: {player(board)}")
print(f"First_player: {first_player}")


