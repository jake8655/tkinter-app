import tkinter as tk

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()

def draw_play_area():
    width = 200
    height = 150
    for i in range(2):
        canvas.create_line(100, 200+i*height, 100+3*width, 200+i*height, fill="black", width=1)
    for i in range(2):
        canvas.create_line(100+i*width, 50+height, 100+i*width, 50+height, fill="black", width=1)

draw_play_area()

tk.mainloop()