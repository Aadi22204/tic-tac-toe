
import numpy as np


def create_board():
    """Create and return an empty 3x3 Tic-Tac-Toe board."""
    return np.zeros((3, 3), dtype=int)


def check_winner(board):
    """
    Check the current board and return:
    X     -> X wins
    O     -> O wins
    DRAW  -> Board is full
    None  -> Game is still running
    """

    # Check rows
    row_sums = np.sum(board, axis=1)

    # Check columns
    col_sums = np.sum(board, axis=0)

    # X wins
    if 3 in row_sums or 3 in col_sums:
        return "X"

    # O wins
    if -3 in row_sums or -3 in col_sums:
        return "O"

    # Check diagonals
    main_diagonal = np.trace(board)
    opposite_diagonal = np.trace(np.fliplr(board))

    if main_diagonal == 3 or opposite_diagonal == 3:
        return "X"

    if main_diagonal == -3 or opposite_diagonal == -3:
        return "O"

    # Check draw
    if not np.any(board == 0):
        return "DRAW"

    return None