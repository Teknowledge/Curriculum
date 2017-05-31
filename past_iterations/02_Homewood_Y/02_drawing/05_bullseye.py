from tkinter import *
from random import randint

def draw(canvas, width, height):
  # write solution here, the first circle is given to you
  canvas.create_oval(0, 0, 200, 200, fill="")

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()