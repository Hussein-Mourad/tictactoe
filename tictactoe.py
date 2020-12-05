"""
Tic Tac Toe Player
"""

import copy

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
        num_X += row.count(X)
        num_O += row.count(O)

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
        new_board = copy.deepcopy(board)
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
            if None in board[i]:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w is X:
        return 1
    elif w is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move = None
    if player(board) is X:
        best_value = float("-inf")
        for action in actions(board):
            result_board = result(board, action)
            current_value = min_board_value(result_board)
            if current_value > best_value:
                best_value = current_value
                best_move = action
    else:
        best_value = float("inf")
        for action in actions(board):
            result_board = result(board,action)
            current_value = max_board_value(result_board)
            if current_value < best_value:
                best_value = current_value
                best_move = action
    return best_move
    
    
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
