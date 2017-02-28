from tkinter import *

def draw(canvas, width, height):
  # Write your solution here! The outside circle is given to you.
  # The parameters work the same as "create_rectangle"!
  canvas.create_oval(0, 0, 200, 200, fill="")

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# FINAL Challenge 3.1 - Change the code above to draw a set of 10 concentric
#    circles (evenly spaced, in a "dartboard" pattern) using a loop.
# For an added challenge, draw the circles alternating black and white.

# FINAL BONUS Challenge 3.2 - Draw four "dartboards" in the four quadrants of
#    the screen, by way of making a drawDartboard function you call four times.
# For a super bonus added challenge, draw random "dartboards" all over the
#    screen with each being a random size.