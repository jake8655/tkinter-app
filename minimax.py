import random
from typing import Literal, Union

Board = list[list[Literal[None, "X", "O"]]]
Square = tuple[int, int]


def get_available_squares(game_state: Board) -> list[Square]:
    available_squares = []
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is None:
                available_squares.append([i, j])

    return available_squares


def minimax(board: Board) -> int:
    return 1


def find_best_move(board: Board) -> Square:
    available_squares = get_available_squares(board)
    best_score = -1000
    best_move: Union[Square, None] = None

    for square in available_squares:
        board[square[0]][square[1]] = "O"
        score = minimax(board)
        board[square[0]][square[1]] = None
        if score > best_score:
            best_score = score
            best_move = square

    return best_move or random.choice(available_squares)
