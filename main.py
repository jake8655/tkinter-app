import tkinter

WIDTH = 800
HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

canvas = tkinter.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()

def getDistanceBetweenCoords(coords1: tuple[float, float], coords2: tuple[float, float]):
    return coords1[0] - coords2[0], coords1[1] - coords2[1]

def move(tag: str, coords: tuple[float, float]):
    tmp_coords = canvas.coords(tag)
    target_coords = getDistanceBetweenCoords(coords, tmp_coords)
    canvas.move(tag, *target_coords)

canvas.create_oval(WIDTH//2 - PLAYER_WIDTH, HEIGHT//2 - PLAYER_WIDTH, WIDTH//2 + PLAYER_HEIGHT, HEIGHT//2 + PLAYER_HEIGHT, fill='lightblue', outline='blue', tag='player')

def motion(event):
    move('player', (event.x-PLAYER_WIDTH, event.y-PLAYER_HEIGHT))

# Mouse movements
# motion({'x': 100, 'y': 100})
canvas.bind('<Motion>', motion)

tkinter.mainloop()