from tkinter import *
import random

# This file builds off of the previous file, but once completely coded,
# will allow you to collaboratively create works of randomly-generated art!

# add any shapes here that you wish to be part of the drawing from the start
drawList = []

canvasWidth = 200
canvasHeight = 200

def makeIterativeArt():
  while (True):
    print('What would you like to add to the drawing?')
    print('(examples: "red rectangle", "blue oval")')

    drawCommand = input("> ")

    processDrawCommand(drawCommand)
    print("Close the drawing window to continue.")
    runDrawing()

def processDrawCommand(drawCommand):
  # the .split() function turns a string of words (with spaces in between)
  # into a list of words of separate elements.
  # example: "fee fi fo fum".split() becomes ["fee", "fi", "fo", "fum"]
  drawCommandList = drawCommand.split()
  (color, shape) = (drawCommandList[0], drawCommandList[1])
  drawList.append((color, shape))

def draw(canvas, cw, ch):
  for drawCommand in drawList:
    if len(drawCommand) == 6:
      (x0, y0, x1, y1, color, shape) = drawCommand
    else:
      (color, shape) = drawCommand
      (x0, y0, x1, y1) = getRandomSquareCoordinates(canvasWidth, canvasHeight)
    if shape == "rectangle":
      canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    elif shape == "oval":
      canvas.create_oval(x0, y0, x1, y1, fill=color)
    else:
      print("Couldn't draw:", drawCommand)

def getRandomSquareCoordinates(cw, ch):
  squareWidth = 10
  x0 = random.randint(0, cw-squareWidth)
  y0 = random.randint(0, ch-squareWidth)
  x1 = x0 + squareWidth
  y1 = y0 + squareWidth
  return (x0, y0, x1, y1)

def runDrawing(width=canvasWidth, height=canvasHeight):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()

makeIterativeArt()

# Challenge fun.1 - Run the file to get an idea of what it does.
#    Then make it much cooler by making the shape width random as well.
#    Hint: You need only change one line in getRandomSquareCoordinates.

# Challenge fun.2 - Right now you can never be finished! Change the function
#    makeIterativeArt so that:
#    - it prints an instruction like:
#       'Type "finish" to show your drawing once more then stop.'
#    - if you type "finish" the loop will stop
#    Hint: you'll need to change the while loop condition to use a variable!

# Challenge fun.3 - Right now it doesn't save the location of the shapes, but
#    draws them in a random spot each time!  Figure out a way to save one
#    position for each shape.

# Challenge fun.4 - Add a new drawing command "delete" that deletes the last
#    shape added to the list.

# BONUS Challenge fun.4 - Wouldn't it be cool to have more shapes to add?
#    Do some research online to find out how to draw:
#    - triangles (look for "tkinter create_polygon")
#      Suggested input format: "yellow triangle"
#    - text (look for "tkinter create_text")
#      Suggested input format: "blue hello" (draws the text "hello" in blue
#      font color in a random position)
#    Hint: You will have to be very creative and make decisions on how you will
#    store the coordinates for each new shape.
