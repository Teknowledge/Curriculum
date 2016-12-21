from tkinter import *
from inspect import stack

class Square(object):

    def __init__(self, cx, cy, sl = 24, color = 'red'):
        self.sl = sl
        self.color = color
        self.cx = cx
        self.cy = cy

    def draw(self, canvas):
        if not isinstance(canvas, Canvas):
            raise Exception("Error: canvas argument is of wrong type in function %s" % (stack()[0][3]))
        canvas.create_rectangle(self.cx-self.sl//2, self.cy-self.sl//2,
         self.cx+self.sl//2, self.cy+self.sl//2, fill=self.color )

class Player(object):

    def __init__(self, data):
        self.radius = 10
        self.cx = data.width//2
        self.cy = data.height - self.radius
        
    def draw(self, canvas):
        if not isinstance(canvas, Canvas):
            stackTrace = stack()[0]
            print(repr(stackTrace))
            raise Exception("Error: canvas argument is of wrong type in function %s" % (stack()[0][3]))
        canvas.create_oval(self.cx - self.radius, self.cy - self.radius, self.cx + self.radius, self.cy + self.radius, fill = 'red')