from tkinter import *
from random import randint

def draw(canvas, width, height):
    # write solution here, the first three rectangles are given to you
    canvas.create_rectangle(0, 0, 20, 20, fill="darkblue")
    canvas.create_rectangle(20, 0, 40, 20, fill="blue")
    canvas.create_rectangle(40, 0, 60, 20, fill="lightblue")

def runDrawing(width=200, height=200):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing()