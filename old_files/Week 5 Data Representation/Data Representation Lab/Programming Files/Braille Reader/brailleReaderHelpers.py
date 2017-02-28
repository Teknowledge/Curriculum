################################################################################
# brailleReaderSampleSolution.py
# Written by Teknowledge
# Contact <amaln@cmu.edu> for questions/comments/feedback
# 
# Other than audio, I couldn't think of any worthwhile helper functions to 
# write, I think this whole program will have to be written by students 
# working with their mentors.  Let me know if you have suggestions for helper 
# functions though!
#
# In this activity, students use six letters on a keyboard that roughly
# make a 3x2 rectangular grid (in the sample solution, tyghvb) and map
# them to the six dots in a braille cell.  They then write a program that
# continually reads keyboard input in braille and converts it to English text.
################################################################################

################################################################################
# Audio Helper
################################################################################

import pyglet

def playsound(filename):
    song = pyglet.media.load(filename)
    song.play()