from tkinter import Canvas

def getDistanceBetweenCoords(coords1: tuple[float, float], coords2: tuple[float, float]):
    return coords1[0] - coords2[0], coords1[1] - coords2[1]

def move(canvas: Canvas, tag: str, coords: tuple[float, float]):
    tmp_coords = canvas.coords(tag)
    target_coords = getDistanceBetweenCoords(coords, tmp_coords)
    canvas.move(tag, *target_coords)
