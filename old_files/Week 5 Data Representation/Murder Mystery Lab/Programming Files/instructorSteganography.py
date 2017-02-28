################################################################################
# instructorSteganography.py
# Written by Teknowledge
# Contact <amaln@cmu.edu> for questions/comments/feedback
#
# This is an example of steganogrphy, or hiding a private image inside a public
# one with little visible change to the public image.  It is meant to be used
# by Teknowledge instructors & mentors to prepare the clues in Murder Mystery 
# Lab.  Students are also welcome to use this as an example or to play around 
# with it, but steganographyHelpers.py has all the functions they need to write
# their own steganography encoded/decoder!
#
# This code was adapted from:
# <http://www.kosbie.net/cmu/fall-14/15-112/notes/notes-steganography.html>
################################################################################

from Tkinter import *

################################################################################
# getRGB, setRGB, hexColor (usual image helper fn's)
################################################################################

def getRGB(image, x, y):
    value = image.get(x, y)
    return tuple(map(int, value.split(" ")))

def setRGB(image, x, y, red, green, blue):
    color = hexColor(red, green, blue)
    image.put(color, to=(x,y))
    
def hexColor(red, green, blue):
    assert((0 <= red <= 255) and
           (0 <= green <= 255) and
           (0 <= blue <= 255))
    return ("#%02x%02x%02x" % (red, green, blue))

################################################################################
# steganography functions
################################################################################

def encodePart(publicPart, privatePart, publicColorReductionFactor, 
    privateColorReductionFactor):
    return (publicPart & ~0b1) + privatePart/privateColorReductionFactor

def decodePart(encodedPart, publicColorReductionFactor, 
    privateColorReductionFactor):
    return privateColorReductionFactor*(encodedPart & 0b1)

def makeBlackAndWhite(image):
    for x in xrange(image.width()):
        for y in xrange(image.height()):
            (r, g, b) = getRGB(image, x, y)
            gray = (r + g + b)/3
            bw = 0 if (gray < 128) else 255
            setRGB(image, x, y, bw, bw, bw)

def reduceColors(image, factor):
    for x in xrange(image.width()):
        for y in xrange(image.height()):
            (r, g, b) = getRGB(image, x, y)
            (r, g, b) = (r/factor*factor, g/factor*factor, b/factor*factor)
            setRGB(image, x, y, r, g, b)

def encodeSteganographyImage(publicGifName, privateGifName, encodedGifName, 
    publicColorReductionFactor, privateColorReductionFactor):

    print "Making encoded image..."
    publicImage = PhotoImage(file=publicGifName+".gif")
    privateImage = PhotoImage(file=privateGifName+".gif")
    width, height = publicImage.width(), publicImage.height()
    
    print "  Reducing colors in public and private image...", 
    reduceColors(publicImage, publicColorReductionFactor)
    publicImage.write(publicGifName+"Reduced.gif", format="gif")

    # NOTE: Either reduce colors in the private image or convert it to B/W,
    # there is no need to do both.  If you make the image B/W, adjust the
    # encoding and decoding functions accordingly
    reduceColors(privateImage, privateColorReductionFactor)
    # makeBlackAndWhite(privateImage)
    privateImage.write(privateGifName+"Reduced.gif", format="gif")
    print "Done!"

    print "  Building encoded image...",
    encodedImage = PhotoImage(width=width, height=height)
    for x in xrange(width):
        for y in xrange(height):
            (r1, g1, b1) = getRGB(publicImage, x, y)
            if ((x < privateImage.width()) and (y < privateImage.height())):
                (r2, g2, b2) = getRGB(privateImage, x, y)
            else:
                (r2, g2, b2) = (0, 0, 0)
            r = encodePart(r1, r2, publicColorReductionFactor, 
                privateColorReductionFactor)
            g = encodePart(g1, g2, publicColorReductionFactor, 
                privateColorReductionFactor)
            b = encodePart(b1, b2, publicColorReductionFactor, 
                privateColorReductionFactor)
            setRGB(encodedImage, x, y, r, g, b)
    print "Done!  Now saving..."
    encodedImage.write(encodedGifName+".gif", format="gif")
    print "Saved encoded image in file:", encodedGif

def decodeSteganographyImage(encodedGifName, decodedGifName, 
    publicColorReductionFactor, privateColorReductionFactor):
    print "Making decoded image...",
    encodedImage = PhotoImage(file=encodedGifName+".gif")
    width, height = encodedImage.width(), encodedImage.height()
    decodedImage = PhotoImage(width=width, height=height)
    for x in xrange(width):
        for y in xrange(height):
            (r, g, b) = getRGB(encodedImage, x, y)
            r = decodePart(r, publicColorReductionFactor, 
                privateColorReductionFactor)
            g = decodePart(g, publicColorReductionFactor, 
                privateColorReductionFactor)
            b = decodePart(b, publicColorReductionFactor, 
                privateColorReductionFactor)
            setRGB(decodedImage, x, y, r, g, b)
    print "Done!  Now saving..."
    decodedImage.write(decodedGifName+".gif", format="gif")
    print "Saved encoded image in file:", decodedGif

###############################################################################
# main
###############################################################################

def main():
    Tk() # must initialize Tk
    publicColorReductionFactor = 64
    privateColorReductionFactor = 128
    publicGifName = "imageToHide"
    privateGifName = "murderer"
    encodedGifName = "overlayedImage"
    decodedGifName = "decodedImage"

    encodeSteganographyImage(publicGif,
                             privateGif,
                             encodedGif, 
                             publicColorReductionFactor, 
                             privateColorReductionFactor)
    decodeSteganographyImage(encodedGif, 
                             decodedGif, 
                             publicColorReductionFactor, 
                             privateColorReductionFactor)
main()