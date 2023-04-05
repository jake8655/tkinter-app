import tkinter

WIDTH = 800
HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

canvas = tkinter.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()
# Face
canvas.create_oval(WIDTH//2 - PLAYER_WIDTH, HEIGHT//2 - PLAYER_HEIGHT, WIDTH//2 + PLAYER_WIDTH, HEIGHT//2 + PLAYER_HEIGHT, fill='lightblue', outline='blue', tag='player')
# Eyes
canvas.create_oval(WIDTH//2 - (PLAYER_WIDTH//2 - 10), HEIGHT//2 - (PLAYER_HEIGHT//2 + 5), WIDTH//2 + (PLAYER_WIDTH//2 - 5), HEIGHT//2 + (PLAYER_HEIGHT//2 - 5), fill='black', tag='player')

def getDistanceBetweenCoords(coords1: tuple[float, float], coords2: tuple[float, float]):
    return coords1[0] - coords2[0], coords1[1] - coords2[1]

def move(tag: str, coords: tuple[float, float]):
    tmp_coords = canvas.coords(tag)
    target_coords = getDistanceBetweenCoords(coords, tmp_coords)
    canvas.move(tag, *target_coords)

def motion(event):
    move('player', (event.x-PLAYER_WIDTH, event.y-PLAYER_HEIGHT))

# Move player to mouse pos
canvas.bind('<Motion>', motion)

tkinter.mainloop()