# ^_^ WEEK 03 FUN ^_^
# TAKE-HOME CHALLENGE
from tkinter import *

def drawSquareDiagonal(canvas, startX, startY, squareWidth, numSquares,
                       fillColor):
  canvas.create_rectangle(0, 0, 10, 10, fill=fillColor)
  canvas.create_rectangle(10, 10, 20, 20, fill=fillColor)
  canvas.create_rectangle(20, 20, 30, 30, fill=fillColor)

def drawCheckerboard(canvas, color1, color2):
  pass

def draw(canvas, width, height):
  drawSquareDiagonal(canvas, 0, 0, 10, 20, "powder blue") 

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# Challenge fun.1 - Change the drawSquareDiagonal function to:
#      > draw a given number of squares (numSquares)
#      > with a given width (squareWidth)
#      > with a given color (fillColor)
#      > starting at a given top left point (startX, startY)
#      > in a diagonal pattern (as it is starting to do now if you run it)

# Challenge fun.2 - Make another function:
#      drawCheckerboard(canvas, color1, color2)
#    that will draw square diagonals to fill the screen (don't worry about
#    drawing extra squares offscreen) in a checkerboard pattern with two
#    different colors (specified by the strings color1 and color2).
# Hint: Use a loop that calls drawSquareDiagonal. It shouldn't be a long
#    function (should be around 5 - 10 lines).
# You can continue to make the squareWidth be 10.
# Fun: For more interesting colors, visit: http://wiki.tcl.tk/37701

# BONUS Challenge fun.3 - If you're up for an extra challenge, let's change
#    drawCheckerboard to ask for your input by asking for the following input:
#      Input your choice for color 1: 
#      Input your choice for color 2: 
#      How many rows/columns do you want: 
#    And with the rows/columns number (say a 10x10 board or 16x16 board),
#    change the calls to drawSquareDiagonal so that the board fits perfectly
#    in the 200x200 canvas window (by doing some math there).
