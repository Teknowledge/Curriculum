from AnimationFramework import AnimationFramework, Struct
from RainingSquaresStudent import fs_init, fs_mousePressed, fs_keyPressed, fs_timerFired, fs_redrawAll

class RainingSquaresAnimationClass(AnimationFramework):

    def init(self, data):
        fs_init(self, data)

    def mousePressed(self, event, data):
        fs_mousePressed(self, event, data)

    def keyPressed(self, event, data):
        fs_keyPressed(self, event, data)

    def timerFired(self, data):
        fs_timerFired(self, data)

    def redrawAll(self, canvas, data):
        fs_redrawAll(self, canvas, data)

if __name__ == "__main__":
    RainingSquaresAnimationClass().run(400,400)
