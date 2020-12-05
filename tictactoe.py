"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
first_player = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X = 0
    num_O = 0
    total_moves = 0
    global first_player

    # Calculates number of X and O in the board
    for row in board:
        for col in row:
            if col == X:
                total_moves += 1
                num_X += 1
            elif col == O:
                total_moves += 1
                num_O += 1

    print(
        f"Total Moves: {total_moves}\t Number of X: {num_X}\t Number of O: {num_O}")

    if total_moves == 1 and num_X == 1:
        first_player = X
        return O
    elif total_moves == 1 and num_O == 1:
        first_player = O
        return X
    elif num_X > num_O:
        return O
    elif num_O > num_X:
        return O
    elif num_X == num_O and first_player == X:
        return X
    elif num_X == num_O and first_player == O:
        return O
    elif terminal(board):
        return None

    # # if number of X equals O then its X's turn assuming that X always starts
    # if num_X == num_O:
    #     return X
    # else:
    #     return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is EMPTY:
                available.add((i, j))
    if terminal(board):
        return None
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        return None
    # Making a deepcopy of the board
    new_board = board[:]
    if action is not None:
        new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks for rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

        elif board[0][i] == board[1][i] == board[2][i]:
            return board[i][0]

    # Checks for diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for row in board:
            for item in row:
                if item is EMPTY:
                    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w is X:
        return 1
    elif w is O:
        return -1
    elif w is None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # best_value = -100
    # best_move = None
    # for move in actions(board):
    #     value = move_value(board, 0)
    #     if value > best_value:
    #         best_move = move
    # print(f"Move:{best_move}")
    # return best_move

    for move in actions(board):
        result_board = result(board, move)
        for i in range(3):
            print(board[i])
        print(f"Player's turn: {player(board)}")
        print(f"First_player: {first_player}")
        print()


"""
if player is X:
    for all possible moves:
        calculate score for the board
    choose the move with highest score

if player is O:
    for all possible moves:
        calculate score for the board
    choose the move with lowest score"""


# def move_value(board, depth):

#     score = utility(board)
#     if score == 1:
#         return score
#     elif score == -1:
#         return score
#     elif terminal(board):
#         return 0

#     # return utility(board)

#     if player(board) is X:
#         best = -100
#         for move in actions(board):
#             result_board = result(board, move)
#             best = max(best, move_value(result_board, depth + 1))
#         return best
#     else:
#         best = 100
#         for move in actions(board):
#             result_board = result(board, move)
#             best = min(best, move_value(result_board, depth + 1))
#         return best
