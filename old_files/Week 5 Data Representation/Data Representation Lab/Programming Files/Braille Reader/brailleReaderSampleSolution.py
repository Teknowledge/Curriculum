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

################################################################################
# Sample Solution
################################################################################

numsToLetters = {
    0b100000: "a",
    0b101000: "b",
    0b110000: "c",
    0b110100: "d",
    0b100100: "e",
    0b111000: "f",
    0b111100: "g",
    0b101100: "h",
    0b011000: "i",
    0b011100: "j",
    0b100010: "k",
    0b101010: "l",
    0b110010: "m",
    0b110110: "n",
    0b100110: "o",
    0b111010: "p",
    0b111110: "q",
    0b101110: "r",
    0b011010: "s",
    0b011110: "t",
    0b100011: "u",
    0b101011: "v",
    0b011101: "w",
    0b110011: "x",
    0b110111: "y",
    0b100111: "z", 
}

# wordToNumber converts the braille "word" the student wrote to the 
# corresponsing number based on the letter-digit mapping in letters.
# (i.e. if a t was in the word, that represents a 1 in the 6th digit, if a "v"
# was in the word that represents a 1 in the 2nd digit, etc.)
def wordToNumber(word):
    letters = ["t", "y", "g", "h", "v", "b"]
    num = 0
    for letter in letters:
        num = num << 1
        if letter in word:
            num += 1
    return num

# Enters a game loop that reads braille "words" and converts them to "letters"
def main():
    word = ""
    while True:
        brailleLetter = input("Type the Braille letter: ") # Python 3
        if len(brailleLetter) == 0:
            print("Final Braille Word: ", word)
            return
        if len(brailleLetter.strip()) < len(brailleLetter):
            word += " "
        else:
            num = wordToNumber(brailleLetter)
            if num in numsToLetters:
                englishLetter = numsToLetters[num]
                word += englishLetter
                playsound(englishLetter+".mp3")
            else:
                print("Unknown Braille Letter: ", brailleLetter)
        print("Braille Word So Far: ", word)

main()