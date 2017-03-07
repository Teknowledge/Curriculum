from tkinter import *
import random

# format of tuples is
# (x0, y0, x1, y1, shapeColor)
# so you can do canvas.create_rectangle(x0, y0, x1, y1, fill=shapeColor)
drawList = [
	(0, 0, 20, 20, 'red'),
	(30, 30, 180, 180, 'blue'),
  (110, 20, 140, 190, 'yellow'),
]

def draw(canvas, width, height):
  # YOUR CODE HERE
  canvas.create_rectangle(0, 0, 10, 10, fill=None)

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# Challenge 2.1 - For each tuple in the drawList, draw a rectangle with the
#    corresponding parameters.  For example, drawList[0] should draw a red
#    rectangle in the top left corner.

# Challenge 2.2 - Add another element to each tuple that is either 'rectangle'
#    or 'oval' and causes your draw function to draw the corresponding shape.

# Challenge 2.3 - Write a new function:
#      getRandomSquareCoordinates(cw, ch)
#    that given a canvas width (cw) and canvas height (ch), returns a tuple
#    like so:
#      (x0, y0, x1, y1)
#    where the points (x0, y0) and (x1, y1) are the top left and bottom right
#    points of a square, with width 10, that is randomly placed on the canvas.
#    Use this function to draw everything in drawList in a random spot.
#    (You can use this for both drawing rectangles and ovals.)

# Challenge 2.4 - Now, add some new rows to drawList, like:
#      ('navy', 'rectangle'),
#      ('gold', 'oval')
#    and change your draw function to draw these with random coordinates, but
#    if the coordinates are present, draw the shape with those coordinates.

# BONUS Challenge - NONE!  Continue to the next file if you are ahead :)
