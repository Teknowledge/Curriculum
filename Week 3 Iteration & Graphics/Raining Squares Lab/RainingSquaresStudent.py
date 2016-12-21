#from tkinter import *
from RainingSquaresHelperClasses import Square, Player

def fs_init(self, data):
        data.numSquares = 15
        data.margin = 15
        sideLength = 20
        spacing = data.width/data.numSquares - sideLength
        data.squares = [Square(data.margin + i * (sideLength + spacing), 30, sl = 20, color = 'blue') for i in range(data.numSquares)]
        data.player = Player(data)

def fs_mousePressed(self, event, data):
    # use event.x and event.y
    pass

def fs_keyPressed(self, event, data):
    if (event.keysym == "Right"):
        data.player.cx += 10
    elif (event.keysym == "Left"):
        data.player.cx -= 10


def fs_timerFired(self, data):
    for s in data.squares:
        s.cy += 5
    for s in data.squares:
        if s.cy >= data.height:
            s.cy = 30

def fs_redrawAll(self, canvas, data):
    for square in data.squares: square.draw(canvas)
    data.player.draw(canvas)
