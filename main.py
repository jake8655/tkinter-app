import tkinter
from utils import move

WIDTH = 800
HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

canvas = tkinter.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()
img = tkinter.PhotoImage(file="assets/player.png")
canvas.create_image(WIDTH//2,HEIGHT//2, anchor='center', image=img, tag='player')

def motion(event):
    move('player', (event.x, event.y))

# Move player to mouse pos
canvas.bind('<Motion>', motion)

tkinter.mainloop()