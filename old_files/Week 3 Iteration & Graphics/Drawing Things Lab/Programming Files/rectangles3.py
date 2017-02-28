from tkinter import *

def draw(canvas, width, height):
    # guess what this will draw before running!
    x = 0
    while (x < 200):
        canvas.create_rectangle(x,x,x+100,x+100, fill="maroon")
        x += 10

def runDrawing(width=200, height=200):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing()