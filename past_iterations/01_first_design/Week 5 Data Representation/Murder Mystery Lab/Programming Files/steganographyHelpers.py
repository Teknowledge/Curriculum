################################################################################
# steganographyHelpers.py
# Written by Teknowledge
# Contact <amaln@cmu.edu> for questions/comments/feedback
#
# This library contains helper functions to allow students to create basic 
# steganography programs, that take one image and encodes it into another
# with minimal visible change to the public image, or that take an encoded
# image and decode it.
#
# Questions for students to ponder as they design their steganography decoder:
# 1) What shared information do the person sending the message and the person
#    recieving the message need to know?
#
# Questions for students to ponder as they design their steganography encoder:
# 1) How will I combine two sets of (r, g, b) values into one while minimally
#    changing how the public image looks?
# 2) How will I reduce the amount of information in each image? (In other
#    words, how colorful do I want each image to be?)
# 3) What will I do if the images are of different sizes?
# 4) If, instead of images, I were encoding a message (string), how would I
#    do that?
# 5) If, instead of hiding one image inside the other, I wanted to overlay
#    them, how would I do that?
#
#
# These helper functions were adapted from:
# <http://www.kosbie.net/cmu/fall-14/15-112/notes/notes-steganography.html>
################################################################################

from Tkinter import *

################################################################################
# File Input/Output Helpers
################################################################################

# readGif reads the gif image stored at filename and returns the image as a
# 2D list of (r, g, b) tuples
def readGif(filename):
    # Read the image
    image = PhotoImage(file=filename)
    width, height = image.width(), image.height()

    # For each pixel, get a 3-tuple of its (r, g, b) values
    # Each value will be an integer between 0 and 255, inclusive
    rgbImage = [[] for y in range(height)]
    for x in range(width):
        for y in range(height):
            rgbString = image.get(x, y)
            (r, g, b) = map(int, rgbString.split(" "))
            rgbImage[y].append((r,g,b))

    return rgbImage

# writeGif takes rgbArray, a 2D list of (r, g, b) values, converts it to a
# gif image, and saves it as filename
def writeGif(rgbArray, filename):
    # Check that the rgbArray is valid
    if len(rgbArray) == 0 or len(rgbArray[0]) == 0:
        raise Exception("The rgb array cannot have empty rows or columns")
    if numberOfColors(rgbArray) > 256:
        raise Exception("Gif images can have max 256 unique colors")

    # Create the final image
    width, height = len(rgbArray[0]), len(rgbArray)
    image = PhotoImage(width=width, height=height)

    # For each 3-tuple (r, g, b) convert it to a pixel and insert in the image
    for x in range(width):
        for y in range(height):
            (r, g, b) = rgbArray[y][x]
            color = rgbToHex(r, g, b)
            image.put(color, to=(x, y))

    # Write the image
    image.write(filename, format="gif")

# rgbToHex converts a tuples of (r, g, b) integer values to the corresponding
# hex color
def rgbToHex(red, green, blue):
    assert((0 <= red <= 255) and
           (0 <= green <= 255) and
           (0 <= blue <= 255))
    return ("#%02x%02x%02x" % (red, green, blue))           

# numberOfColors returns the number of unique (r, g, b) combinations in
# rgbArray.  This is necessary because gifs cannot have more that 256
# unique colors
def numberOfColors(rgbArray):
    uniqueColors = set(sum(rgbArray, []))
    return len(uniqueColors)

################################################################################
# Image Manipulation Helpers
################################################################################

# reduce colors takes every r, g, b value of every pixel in rgbArray, and 
# rounds it to the nearest multiple of the given factor.  This is because
# gifs cannot have more than 256 unique colors, and since we are combining
# two gifs into one, we will need to lose some information.
def reduceColors(rgbArray, factor):
    # Check that the rgbArray is valid
    if len(rgbArray) == 0 or len(rgbArray[0]) == 0:
        raise Exception("The rgb array cannot have empty rows or columns")

    # Create the finalRgbArray
    width, height = len(rgbArray[0]), len(rgbArray)
    finalRgbArray = [[] for y in range(height)]

    # Round the rgb values of each pixel
    for x in range(width):
        for y in range(height):
            (r0, g0, b0) = rgbArray[y][x]
            (r1, g1, b1) = (r0//factor*factor, 
                            g1//factor*factor, 
                            b1//factor*factor)
            finalRgbArray[y].append(r1, g1, b1)

    return finalRgbArray

