"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Let X always starts
    if board == initial_state():
        return X

    num_X = 0
    num_O = 0

    # Calculates number of X and O in the board
    for row in board:
        num_X = row.count(X)
        num_O = row.count(O)

    # if number of X equals O then its X's as X always starts
    if num_X == num_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is EMPTY:
                available.add((i, j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the action is valid
    # print(action)
    if action is not None:
        if action[0] > 2 or action[1] > 2:
            raise ValueError

        # Making a deepcopy of the board
        new_board = board[:]
        new_board[action[0]][action[1]] = player(new_board)

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
            return board[0][i]

    # Checks for diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    # No winner or tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for i in range(3):
            if not None in board[i]:
                return True
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
    elif w:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    best = [float('-inf'), (None, None)]

    for action in actions(board):
        move_value = find_board_value(board[:], 0, False)
        print(f"Board_Value: {move_value}")
        if move_value > best[0]:
            best = [move_value, action]
    print(f"Best Move: {best[1]}")
    return best[1]

    # if terminal(board) or winner(board):
    #     return utility(board)

    # for i in range(3):
    #     print(board[i])
    # print(f"Player: {player(board)}")
    # print()

    # if player(board) is X:
    #     best = float("-inf")
    #     for move in actions(board):
    #         result_board = result(board, move)
    #         value = minimax(result_board)
    #         best = max(best, value)
    #     return best
    # else:
    #     best = float("inf")
    #     for move in actions(board):
    #         result_board = result(board, move)
    #         value = minimax(board)
    #         best = min(best, value)
    #     return best

    # for i in range(3):
    #     print(result_board[i])
    # print(f"Player's turn: {player(result_board)}")
    # print(f"First_player: {first_player}")
    # print()


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

#     if winner(board):
#         return utility(board)
#     elif not winner(board):
#         return utility(board)
#     elif terminal(board):
#         return None

#     if player(board) is X:
#         best = [(None, None), float("-inf")]
#     else:
#         best = [(None, None), float("inf")]

#     if player(board) is X:
#         for move in actions(board):
#             result_board = result(board, move)
#             score = utility(board)
#             if score > best[1]:
#                 best = [move, score]
#             for i in range(3):
#                 print(result_board[i])
#             print(best, end="\n\n")

#     else:
#         for move in actions(board):
#             result_board = result(board, move)
#             score = utility(board)
#             if score < best[1]:
#                 best = [move, score]
#             for i in range(3):
#                 print(result_board[i])
#             print(best, end="\n\n")


# def test(board):

#     if terminal(board) or winner(board):
#         return utility(board)

#     for i in range(3):
#         print(board[i])
#     print(f"Player: {player(board)}")

#     if player(board) is X:
#         best = float("-inf")
#         for move in actions(board):
#             result_board = result(board,move)
#             value = test(result_board)
#             best = max(best, value)
#         return best
#     else:
#         best = float("inf")
#         for move in actions(board):
#             result_board = result(board,move)
#             value = test(board)
#             best = min(best, value)
#         return best


def find_board_value(board, depth, maxplayer):

    for i in range(3):
        print(board[i])
    print()

    if winner(board):
        return utility(board)
    elif terminal(board):
        return utility(board)
    if maxplayer:
        best = float("-inf")

        for action in actions(board):
            result_board = result(board, action)
            best = max(best, find_board_value(
                result_board, depth+1, not maxplayer))
        return best
    else:
        best = float("inf")

        for action in actions(board):
            result_board = result(board, action)
            best = min(best, find_board_value(
                result_board, depth+1, not maxplayer))
        return best


def max_board_value(board):
    if terminal(board):
        return utility(board)

    best_value = float("-inf")
    for action in actions(board):
        result_board = result(board, action)
        best_value = max(best_value, min_board_value(result_board))
    
    return best_value


def min_board_value(board):
    if terminal(board):
        return utility(board)

    best_value = float("inf")
    for action in actions(board):
        result_board = result(board, action)
        best_value = min(best_value, max_board_value(result_board))
    
    return best_value
