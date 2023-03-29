import tkinter

WIDTH = 800
HEIGHT = 600

canvas = tkinter.Canvas(bg='pink', width=WIDTH, height=HEIGHT)
canvas.pack()

player = canvas.create_oval(WIDTH//2 - 50, HEIGHT//2 - 50, WIDTH//2 + 50, HEIGHT//2 + 50, fill='lightblue', outline='blue')

def motion(coords):
    canvas.place(x=10, y=10)

# Arrow movements
# canvas.bind('<>', motion)

tkinter.mainloop()