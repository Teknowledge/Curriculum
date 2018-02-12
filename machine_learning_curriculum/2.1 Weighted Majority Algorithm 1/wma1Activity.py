#!/usr/bin/env python3

################################################################################
# Movie Predictor
#
# You have two friends who want to recommend new movies to you. However, you
# are not sure which friend's movie preferences better align with yours. To
# determine this, you create a test.
#
# You come up with a list of old movies that you have seen. One at a time, you
# ask your two friends whether they liked them. You also know whether you liked
# the movies. Therefore, using the weighted majority algorithm, you keep track
# of weights, which indicate how well-aligned each friends' preferences are to
# yours. In the end, you can use these weights to determine how much to trust
# each friend when they recommend future movies to you!
#
################################################################################

import random, math

# This function takes in a string which represents a yes/no question, asks for
# user input, and returns a boolean value indicating whether the use answers
# yes or no.
def getUserInput(prompt):
    print(prompt)
    print("Answer y/n: ")
    answer = input("> ")
    if (answer[0].lower() == "y"):
        return True
    else:
        return False

############################################################################
# Challenge 0: Change the movieInputs list below to contain up to 10 movies that you 
# and your friends all know.
############################################################################

movieInputs = ["Zootopia",
             "Big Hero 6",
             "The Hunger Games: Catching Fire",
             "Star Wars: The Phantom Menace",
             "Harry Potter and the Deathly Hallows"]

# Shuffle the list of movies.
random.shuffle(movieInputs)

def run(test=False):
    # Initialize two "experts"
    expert0Weight = 1.0
    expert1Weight = 1.0

    # How much the expert weight gets reduced by per wrong prediction
    penalty = 0.5 

    for movie in movieInputs:
        if test:
            # Test mode
            expert0Label = test[movie]["expert0Label"]
            expert1Label = test[movie]["expert1Label"]
            actualLabel = test[movie]["actualLabel"]
        else:
            # User input mode
            expert0Label = getUserInput("Expert 0: Did you like " + movie + "?")
            expert1Label = getUserInput("Expert 1: Did you like " + movie + "?")
            actualLabel = getUserInput("Main Character: Did you like " + movie + "?")

        ############################################################################
        # Challenge 1: The first step is to use the expert labels and weights to
        # determine which label to predict (True or False). 
        ############################################################################
       
        # Write your code here!

        # Fill this conditional in to complete Challenge 1. You might want to create
        # some new variables to compare first. 
        if (trueWeight >= falseWeight): 
            predictedLabel = True
        else:
            predictedLabel = False


        ############################################################################
        # Challenge 2: Use the actualLabel variable (which represents whether or not
        # you liked the movie), the next step is to adjust the expert weights based
        # on whether or not their label was accurate.     
        ############################################################################

        # Write your code here!

        # Uncomment these lines for debugging 
        # print("Expert 0 Weight: " + str(expert0Weight))
        # print("Expert 1 Weight: " + str(expert1Weight))

        if test:
            assert(expert0Weight == test[movie]["expert0Weight"])
            assert(expert1Weight == test[movie]["expert1Weight"])
        else:
            print("Model prediction: " + ("y" if str(predictedLabel) else "n"))
            print("Expert 0 new weight: " + str(expert0Weight))
            print("Expert 1 new weight: " + str(expert1Weight))
            print("-"*88)


############################################################################
# Challenge 3: Now that all the code is in place, run these tests and try to
# figure out why your code might be wrong (if it is).
# It may help to uncomment the two lines that print the expert weights.
############################################################################

test1 = {}
for i in range(len(movieInputs)):
    test1[movieInputs[i]] = {}
    test1[movieInputs[i]]["actualLabel"] = False
    test1[movieInputs[i]]["expert0Label"] = False
    test1[movieInputs[i]]["expert1Label"] = True
    test1[movieInputs[i]]["expert0Weight"] = 1.0
    test1[movieInputs[i]]["expert1Weight"] = 0.5**(i+1)
run(test1)

test2 = {}
for i in range(len(movieInputs)):
    test2[movieInputs[i]] = {}
    test2[movieInputs[i]]["actualLabel"] = True
    test2[movieInputs[i]]["expert0Label"] = False
    test2[movieInputs[i]]["expert1Label"] = True
    test2[movieInputs[i]]["expert0Weight"] = 0.5**(i+1)
    test2[movieInputs[i]]["expert1Weight"] = 1.0
run(test2)

# Ask a mentor for help if you're stuck on debugging test 3!
test3 = {}
for i in range(len(movieInputs)):
    test3[movieInputs[i]] = {}
    test3[movieInputs[i]]["actualLabel"] = True
    test3[movieInputs[i]]["expert0Label"] = (i%2 == 0)
    test3[movieInputs[i]]["expert1Label"] = (i%2 == 1)
    test3[movieInputs[i]]["expert0Weight"] = 0.5**(math.floor((i+1)/2))
    test3[movieInputs[i]]["expert1Weight"] = 0.5**(math.floor((i+2)/2))
run(test3)

print("All tests pass!")

############################################################################
# Challenge 4: Now, run the code in user mode where you can input your actual
# preferences and see which friends align with your tastes! Each person can
# take turns being the "Main Character"
############################################################################
run()


############################################################################
# Challenge 5: COMPREHENSION QUESTIONS -- think about them and/or discuss them
# with a friend. We will discuss them at the end of class.
#    - Do we ever use predictedLabel? What are example scenarios where
#      predictedLabel is important?
#    - Explain in English what the expert weights represent in this scenario.
#      In particular, what does a larger expert weight mean and what does a
#      smaller expert weight mean?
#    - With just two experts, it may not be fair to expect any one expert's
#      movie preferences to completely align with yours. Maybe someone's
#      preferences align with yours when it comes to action movies, but not
#      romance movies. How can you modify WMA to account for preferences by
#      movie genre? (If you have extra time, code it up!)
#    - It is easy to think of real life scenarios where humans can use WMA.
#      What are some real-life scenarios where robots could use WMA? What
#      about where computers and/or machine learning algorithms that are
#      processing tons of data could use WMA?
############################################################################
