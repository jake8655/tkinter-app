from os import error
import tkinter as tk
from typing import Literal, Union
import random

WIDTH = 800
HEIGHT = 600

win = tk.Tk()
win.geometry(f"{WIDTH}x{HEIGHT}")
win.title("Tic Tac Toe")

canvas = tk.Canvas(bg="pink", width=WIDTH, height=HEIGHT)
canvas.pack()

game_state: list[list[Literal[None, "X", "O"]]] = [[None, None, None], [None, None, None], [None, None, None]]


def draw_play_area(width: int, height: int):
    for i in range(2):
        # Horizontal lines
        canvas.create_line(100, 200 + i * height, 100 + 3 * width, 200 + i * height, fill="black", width=1)
        # Vertical lines
        canvas.create_line(100 + (i + 1) * width, 50, 100 + (i + 1) * width, 50 + height * 3, fill="black", width=1)


width_of_square = 200
height_of_square = 150
coords_of_squares = (
    (
        ((100, 50), (100 + width_of_square, 50 + height_of_square)),
        ((100 + width_of_square, 50), (100 + 2 * width_of_square, 50 + height_of_square)),
        ((100 + 2 * width_of_square, 50), (100 + 3 * width_of_square, 50 + height_of_square)),
    ),
    (
        ((100, 50 + height_of_square), (100 + width_of_square, 50 + 2 * height_of_square)),
        ((100 + width_of_square, 50 + height_of_square), (100 + 2 * width_of_square, 50 + 2 * height_of_square)),
        ((100 + 2 * width_of_square, 50 + height_of_square), (100 + 3 * width_of_square, 50 + 2 * height_of_square)),
    ),
    (
        ((100, 50 + 2 * height_of_square), (100 + width_of_square, 50 + 3 * height_of_square)),
        ((100 + width_of_square, 50 + 2 * height_of_square), (100 + 2 * width_of_square, 50 + 3 * height_of_square)),
        (
            (100 + 2 * width_of_square, 50 + 2 * height_of_square),
            (100 + 3 * width_of_square, 50 + 3 * height_of_square),
        ),
    ),
)


def draw_x(square: tuple[int, int]):
    canvas.create_line(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        fill="blue",
        width=1,
    )
    canvas.create_line(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        fill="blue",
        width=1,
    )
    game_state[square[0]][square[1]] = "X"
    canvas.update()


def check_empty_squares():
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is None:
                return True
    return False


def check_win():
    winner = None

    # Check board for 3 in a row or 3 in a column or 3 diagonal
    for i in range(3):
        if game_state[i][0] == game_state[i][1] == game_state[i][2] is not None:
            winner = game_state[i][0]
        if game_state[0][i] == game_state[1][i] == game_state[2][i] is not None:
            winner = game_state[0][i]
    if game_state[0][0] == game_state[1][1] == game_state[2][2] is not None:
        winner = game_state[0][0]
    if game_state[0][2] == game_state[1][1] == game_state[2][0] is not None:
        winner = game_state[0][2]

    if winner:
        print(f"{winner} won")
        canvas.after(1000, win.destroy)


def draw_o():
    if not check_empty_squares():
        print("Draw")
        return canvas.after(1000, win.destroy)

    square = random.randint(0, 2), random.randint(0, 2)
    while game_state[square[0]][square[1]] is not None:
        square = random.randint(0, 2), random.randint(0, 2)

    canvas.create_oval(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        outline="red",
        width=1,
    )

    game_state[square[0]][square[1]] = "O"
    canvas.update()
    check_win()


def calculate_square(x: int, y: int) -> tuple[int, int]:
    square: Union[None, tuple[int, int]] = None
    for i in range(3):
        for j in range(3):
            if (
                coords_of_squares[i][j][0][0] <= x <= coords_of_squares[i][j][1][0]
                and coords_of_squares[i][j][0][1] <= y <= coords_of_squares[i][j][1][1]
            ):
                square = (i, j)
                break
        if square:
            break
    if not square:
        raise error("Error with finding which square was clicked")
    return square


def check_square_is_taken(square: tuple[int, int]) -> bool:
    return game_state[square[0]][square[1]] is not None


def click(e):
    square = calculate_square(e.x, e.y)

    if check_square_is_taken(square):
        return print("Square already taken")

    draw_x(square)
    check_win()
    canvas.after(1000, draw_o)


draw_play_area(width_of_square, height_of_square)
canvas.bind("<Button-1>", click)

# Quit when ESC is pressed
win.bind("<Escape>", lambda _: win.destroy())

win.mainloop()
