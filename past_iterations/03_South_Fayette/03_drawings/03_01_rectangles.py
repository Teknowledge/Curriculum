from tkinter import *

def draw(canvas, width, height):
  canvas.create_rectangle(0,0,100,100, fill="maroon")
  # Challenge 01 (see below)
  # canvas.create_rectangle(0,0,50,50, fill="green")
  # canvas.create_rectangle(100,0,200,200, fill="orange")
  # canvas.create_rectangle(0,100,200,200, fill="yellow")
  # Challenge 02 (see below)
  # canvas.create_rectangle(_,_,_,_, fill="lightblue")
  # Challenge 03 (see below)
  # x = 0
  # while (x < 200):
  #   canvas.create_rectangle(x,x,x+100,x+100, fill="maroon")
  #   x += 10

def runDrawing(width=200, height=200):
  root = Tk()
  canvas = Canvas(root, width=width, height=height, highlightthickness=0)
  canvas.pack()
  draw(canvas, width, height)
  root.mainloop()
  print("bye!")

runDrawing()

# Challenge 1.1 - First run the file and look at the first rectangle. Then
#    delete, one-by-one, the comments from lines 6, 7, and 8. Try to predict
#    where each rectangle will draw on the screen.

# Challenge 1.2 - Fill in the dimensions to draw the last lightblue rectangle
#    at the BOTTOM LEFT of the 200x200 screen.

# Challenge 1.3 - Uncomment the rest of the code. Run it to see what it does.
#    Then change the code to draw twice as many rectangles on the screen
#    (still on the same path, just one in between every other).
#    Hint: You only need to change one number!

# Challenge 1.4 - Now make the same behavior, but change the while loop to a
#    for loop.
#    Hint: Look at your syntax guide for help.

# BONUS Challenge 1.5 - Draw another set of yellow rectangles going down the
#    opposite diagonal (within the same while loop!).
