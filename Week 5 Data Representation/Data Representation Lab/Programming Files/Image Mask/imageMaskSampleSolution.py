################################################################################
# imageMaskHelpersSampleSolution.py
# Written by Teknowledge
# Contact <amaln@cmu.edu> for questions/comments/feedback
#
# This library contains helper functions to allow students to create a basic 
# image masking program, that takes two images and puts one on top of the
# other using a mask.  The mask will be created using user-defined threshold
# values for pixels.
# 
# Questions for students to ponder as they write image mask program:
#   1) How will they deal with different sized images?
#   2) What if instead of overlapping images using masks, we wanted to overlay
#      images (i.e. both images are partially visible)?  How could we do that?
#   3) What are other ways to represent masks (as oppose to 2D lists of bools)?
#   4) Does it matter whether the parts we want to mask are represented as 
#      (0, 0, 0) (black) or (255, 255, 255) (white)?  Does it matter whether 
#      we or pixels together, or and them together?
#
# Some helper functions were adapted from:
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
    colors = numberOfColors(rgbArray)
    if colors > 256:
        raise Exception("Gif images can have max 256 unique colors, this"+
            " gif has %d" % colors)

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
                            g0//factor*factor, 
                            b0//factor*factor)
            finalRgbArray[y].append((r1, g1, b1))

    return finalRgbArray

################################################################################
# Mask Helpers
################################################################################

# convertImageToMask creates a mask that is the same size 2D list as the 
# image, with boolean values (true and false).  This function takes any pixel
# from image that has r, g, and b values between the given min and max values
# (inclusive) and makes that true.  All other pixels become false.
def convertImageToMask(rMin, rMax, gMin, gMax, bMin, bMax, image):
    mask = [[None for col in range(len(image[row]))] for row in range(len(image))]
    for row in range(len(image)):
        for col in range(len(image[row])):
            (r, g, b) = image[row][col]
            if (rMin <= r and r <= rMax and gMin <= g and g <= gMax and
                bMin <= b and b <= bMax):
                mask[row][col] = True
            else:
                mask[row][col] = False
    return mask

# reverseMask takes a 2D mask of booleans and swaps all the trues and falses
def reverseMask(mask):
    newMask = [[None for col in range(len(mask[row]))] for row in range(len(mask))]
    for row in range(len(mask)):
        for col in range(len(mask[row])):
            newMask[row][col] = not mask[row][col]
    return newMask

# applyMask takes an image of (r, g, b) values and a mask of bools,
# and returns a newImage where the (r, g, b) values for every index that is 
# true in the mask is (0, 0, 0) and all other (r, g, b) values are the same.
# The mask and image are aligned at the top-left pixel, and the returned
# image will be the same size as the original.
def applyMask(image, mask):
    newImage = [[image[row][col] for col in range(len(image[row]))] for row in range(len(image))]
    for row in range(min(len(mask), len(image))):
        for col in range(min(len(mask[row]), len(image[row]))):
            if mask[row][col]:
                newImage[row][col] = (0, 0, 0) # black out the pixels in the mask
    return newImage

################################################################################
# Sample Solution
################################################################################

# combineImages takes two 2D lists of (r, g, b) values or-s 
# together the corresponding r, g, and b values, and returns the final image.
# The images are aligned at the top-left corner, and the returned image will
# be the min size on both dimensions.
def combineImages(image1, image2):
    finalImage = [[None for col in range(len(image1[row]))] for row in range(len(image1))]
    for row in range(min(len(image1), len(image2))):
        for col in range(min(len(image1[row]), len(image2[row]))):
            (r1, g1, b1) = image1[row][col]
            (r2, g2, b2) = image2[row][col]
            finalImage[row][col] = (r1 | r2, g1 | g2, b1 | b2) # or the values
    return finalImage

# maskImage takes in the filenames for the two images to combine, the 
# filenmae to save the final image as, threshold values that indicate what 
# pixels in image1 to mask.
def maskImages(image1FileName, image2FileName, finalImageFileName,
    rMin, rMax, gMin, gMax, bMin, bMax, reductionFactor):
    image1 = readGif(image1FileName)
    image2 = readGif(image2FileName)
    mask = convertImageToMask(rMin, rMax, gMin, gMax, bMin, bMax, image1)
    image1Masked = applyMask(image1, mask)
    image2Masked = applyMask(image2, reverseMask(mask))
    finalImage = combineImages(image1Masked, image2Masked)
    finalImageReduced = reduceColors(finalImage, reductionFactor)
    writeGif(finalImageReduced, finalImageFileName)

def main():
    Tk() # must initialize Tk
    maskImages("pikachu.gif", "background.gif", "finalImage.gif", 
        240, 255, 240, 255, 240, 255, 32)

main()
