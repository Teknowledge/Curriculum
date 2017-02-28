from tkinter import *
import random

# the game data for the initial game state
def init():
  data.playerX = 250
  data.playerY = 550
  data.circles = []  # store circles as [x, y, r, color]
  data.gameOver = False
  data.time = 0
  data.score = 0

# events updating the game data
def keyPressed(event):
  if event.keysym == "Right" and data.playerX < 550:
    data.playerX += 5
  elif event.keysym == "Left" and data.playerX > 0:
    data.playerX -= 5

# the game data updating the game state
def timerFired():
  if not data.gameOver:
    data.time += 1
    data.score += 5
    if data.time % 3 == 0:
      createNewCircle()
    moveCircle()
    for circle in data.circles:
      if checkCollision(data.playerX, data.playerY, 
                        circle[0], circle[1], 10, circle[2]):
        data.gameOver = True

def createNewCircle():
  x = random.randint(0, 550)
  y = 0
  r = random.randint(20, 40)
  color = random.choice(
    ["orange", "yellow", "green", "blue", "purple", "cyan", "magenta"])
  data.circles.append([x, y, r, color])

def moveCircle():
  for circle in data.circles:
    circle[1] += 10

def checkCollision(x1, y1, x2, y2, r1, r2):
  distance = ((x2-x1)**2 + (y2 - y1)**2)**0.5
  return distance <= r1 + r2

# the game state updating what is drawn
def redrawAll(canvas):
  canvas.create_oval(data.playerX - 10, data.playerY - 10, 
                     data.playerX + 10, data.playerY + 10,
                     fill="red")
  scoreString = "Score: %d" % data.score
  for circle in data.circles:
    x, y, r, color = circle
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
  canvas.create_text(300, 30, text=scoreString, font="Arial 30 bold")
  if data.gameOver:
    canvas.create_text(300, 250, text="Game Over", font="Arial 20")



# animation setup code below here #

class Struct(object): pass
data = Struct()

def run(width=600, height=600):
  def redrawAllWrapper(canvas):
    canvas.delete(ALL)
    redrawAll(canvas)
    canvas.update()    

  def keyPressedWrapper(event, canvas):
    keyPressed(event)
    redrawAllWrapper(canvas)

  def timerFiredWrapper(canvas):
    timerFired()
    redrawAllWrapper(canvas)
    # pause, then call timerFired again
    canvas.after(data.timerDelay, timerFiredWrapper, canvas)

  # Set up data and call init
  data.width = width
  data.height = height
  data.timerDelay = 200 # milliseconds
  init()
  # create the root and the canvas
  root = Tk()
  canvas = Canvas(root, width=data.width, height=data.height)
  canvas.pack()
  # set up events
  root.bind("<Key>", lambda event:
                          keyPressedWrapper(event, canvas))
  timerFiredWrapper(canvas)
  # and launch the app
  root.mainloop()  # blocks until window is closed
  print("bye!")

run()
