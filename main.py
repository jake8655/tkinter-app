from os import error
import tkinter as tk
import minimax

WIDTH = 800
HEIGHT = 600

win = tk.Tk()
win.geometry(f"{WIDTH}x{HEIGHT}")
win.title("Tic Tac Toe")

canvas = tk.Canvas(bg="pink", width=WIDTH, height=HEIGHT)
canvas.pack()

game_state: minimax.Board = [[None, None, None], [None, None, None], [None, None, None]]

width_of_square = 200
height_of_square = 150
# Very glad I had not had to write these myself, but probably should change to generated
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


def draw_play_area(width: int, height: int):
    for i in range(2):
        # Horizontal lines
        canvas.create_line(100, 200 + i * height, 100 + 3 * width, 200 + i * height, fill="black", width=1)
        # Vertical lines
        canvas.create_line(100 + (i + 1) * width, 50, 100 + (i + 1) * width, 50 + height * 3, fill="black", width=1)


def draw_x(square: minimax.Square, color: str):
    canvas.create_line(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        fill=color,
        width=1,
    )
    canvas.create_line(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        fill=color,
        width=1,
    )
    canvas.update()


def draw_o(square: minimax.Square, color: str):
    canvas.create_oval(
        coords_of_squares[square[0]][square[1]][0][0] + 20,
        coords_of_squares[square[0]][square[1]][0][1] + 20,
        coords_of_squares[square[0]][square[1]][1][0] - 20,
        coords_of_squares[square[0]][square[1]][1][1] - 20,
        outline=color,
        width=1,
    )
    canvas.update()


def make_human_move(square: minimax.Square):
    if minimax.HUMAN == "X":
        draw_x(square, "blue")
    else:
        draw_o(square, "blue")

    minimax.make_move(game_state, square, minimax.HUMAN)


def handle_win(winner):
    if not winner:
        return False

    if winner == "tie":
        print("Tie!")
    else:
        print(f"{winner} wins!")

    win.after(1000, win.destroy)
    return True


def make_ai_move():
    square = minimax.find_best_move(game_state)

    if minimax.AI == "X":
        draw_x(square, "red")
    else:
        draw_o(square, "red")

    minimax.make_move(game_state, square, minimax.AI)

    handle_win(minimax.check_win(game_state))


def calculate_clicked_square(x: int, y: int) -> minimax.Square:
    square: None | minimax.Square = None
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


def check_square_is_taken(square: minimax.Square) -> bool:
    return game_state[square[0]][square[1]] is not None


def click(event):
    square = calculate_clicked_square(event.x, event.y)

    if check_square_is_taken(square):
        return print("Square already taken")

    make_human_move(square)

    if handle_win(minimax.check_win(game_state)):
        return

    canvas.after(1000, make_ai_move)


def after_wait():
    make_ai_move()
    canvas.bind("<Button-1>", click)


draw_play_area(width_of_square, height_of_square)
if minimax.AI == "X":
    canvas.after(1000, after_wait)
else:
    canvas.bind("<Button-1>", click)

# Quit when ESC is pressed
win.bind("<Escape>", lambda _: win.destroy())

win.mainloop()
