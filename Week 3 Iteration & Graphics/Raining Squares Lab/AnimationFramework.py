from tkinter import *

####################################
# use the run function as-is
####################################
class Struct(object): 
        pass

class AnimationFramework(object):

    ####################################
    # customize these functions
    ####################################

    def init(self, data):
        # load data.xyz as appropriate
        pass

    def mousePressed(self, event, data):
        # use event.x and event.y
        pass

    def keyPressed(self, event, data):
        # use event.char and event.keysym
        pass

    def timerFired(self, data):
        pass

    def redrawAll(self, canvas, data):
        pass

    def redrawAllWrapper(self, canvas, data):
            canvas.delete(ALL)
            canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)
            self.redrawAll(canvas, data)
            canvas.update()    

    def mousePressedWrapper(self, event, canvas, data):
        self.mousePressed(event, data)
        self.redrawAllWrapper(canvas, data)

    def keyPressedWrapper(self, event, canvas, data):
        self.keyPressed(event, data)
        self.redrawAllWrapper(canvas, data)

    def timerFiredWrapper(self, canvas, data):
        self.timerFired(data)
        self.redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, self.timerFiredWrapper, canvas, data)

    def run(self, width=300, height=300):
        # Set up data and call init
        data = Struct()
        data.width = width
        data.height = height
        data.timerDelay = 100 # milliseconds
        self.init(data)
        # create the root and the canvas
        root = Tk()
        canvas = Canvas(root, width=data.width, height=data.height)
        canvas.pack()
        # set up events
        root.bind("<Button-1>", lambda event:
                                self.mousePressedWrapper(event, canvas, data))
        root.bind("<Key>", lambda event:
                                self.keyPressedWrapper(event, canvas, data))
        self.timerFiredWrapper(canvas, data)
        # and launch the app
        root.mainloop()  # blocks until window is closed
        print("bye!")