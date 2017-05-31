from tkinter import *

def draw(canvas, width, height):
    canvas.create_rectangle(0,0,100,100, fill="maroon")
    # delete the #s from these lines one by one
    # canvas.create_rectangle(0,0,50,50, fill="green")
    # canvas.create_rectangle(100,0,200,200, fill="orange")
    # canvas.create_rectangle(0,100,200,200, fill="yellow")
    # how to fill bottom left corner?
    # canvas.create_rectangle(_,_,_,_, fill="lightblue")

def runDrawing(width=200, height=200):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing()