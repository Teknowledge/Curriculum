from tkinter import *

def draw(canvas, width, height):
    # draw these on a piece of paper before you run the code
    canvas.create_rectangle(0,0,50,50, fill="maroon")
    canvas.create_rectangle(100,100,200,200, fill="pink")
    canvas.create_rectangle(50,50,150,150, fill="turquoise")
    # challenge rectangle! (add it to your drawing, then delete the #)
    # canvas.create_rectangle(25,125,75,175, fill="purple")

def runDrawing(width=200, height=200):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing()