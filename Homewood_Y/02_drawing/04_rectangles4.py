from tkinter import *
from random import randint

def draw(canvas, width, height):
  # let's have fun with random numbers!
  for i in range(100): # try increasing this number
    # why are these values like this?
    x = randint(1, 190)
    y = randint(1, 190)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    # try changing width and height
    w = 10
    h = 10
    # how would we pick from a few random colors?
    fillColor = "maroon"
    # try changing "create_rectangle" to "create_oval"
    canvas.create_rectangle(x,y,x+w,y+h, fill='#%02x%02x%02x' % (r,g,b))

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()