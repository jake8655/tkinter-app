import tkinter

WIDTH = 800
HEIGHT = 600

canvas = tkinter.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()

player = canvas.create_oval(WIDTH//2 - 50, HEIGHT//2 - 50, WIDTH//2 + 50, HEIGHT//2 + 50, fill='lightblue', outline='blue')

def motion(event):
    print(event["x"], event["y"])
    canvas.move(player, event["x"], event["y"])

# Mouse movements
motion({'x': 100, 'y': 100})
# canvas.bind('<Motion>', motion)

tkinter.mainloop()