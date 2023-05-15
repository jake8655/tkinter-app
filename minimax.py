import random
from typing import Literal

Board = list[list[Literal[None, "X", "O"]]]
Square = tuple[int, int]

AI = "O"
HUMAN = "X"
SCORES = {
    "X": -1 if AI == "O" else 1,
    "O": 1 if AI == "O" else -1,
    "tie": 0,
}


def check_empty_squares(board: Board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return True
    return False


def check_win(board: Board):
    winner = None

    # Check board for 3 same in a row, in a column or diagonal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] is not None:
            winner = board[i][0]
        if board[0][i] == board[1][i] == board[2][i] is not None:
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] is not None:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] is not None:
        winner = board[0][2]

    if not check_empty_squares(board) and not winner:
        return "tie"

    return winner


def make_move(board: Board, square: Square, player: Literal["X", "O"]) -> Board:
    board[square[0]][square[1]] = player
    return board


def undo_move(board: Board, square: Square) -> Board:
    board[square[0]][square[1]] = None
    return board


def get_available_squares(game_state: Board) -> list[Square]:
    available_squares = []
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is None:
                available_squares.append([i, j])

    return available_squares


def calculate_score_of_next_move(board: Board, depth: int, isMaximizing: bool):
    best_score = -1000 if isMaximizing else 1000
    best_move: Square = random.choice(get_available_squares(board))
    available_squares = get_available_squares(board)

    for square in available_squares:
        make_move(board, square, AI if isMaximizing else HUMAN)
        score = minimax(board, depth + 1, not isMaximizing)
        undo_move(board, square)

        prev_score = best_score
        best_score = max(score, best_score) if isMaximizing else min(score, best_score)
        if prev_score != best_score:
            best_move = square

    return best_score, best_move


def minimax(board: Board, depth: int, isMaximizing: bool):
    result = check_win(board)
    if result:
        return SCORES[result]

    score, _ = calculate_score_of_next_move(board, depth, isMaximizing)
    return score


def find_best_move(board: Board) -> Square:
    _, best_move = calculate_score_of_next_move(board, 0, True)
    return best_move
