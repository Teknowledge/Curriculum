################################################################################
# Supernova 
#
# Note: this week's coding activity is less structured than we've seen in the past.
# This time, we want you to translate the pseudocode you wrote to code with
# less help than before. It might be more challenging than before, so make sure you
# have good pseudocode!
# 
# We have data on about 500 stars in the universe. We have the age at which
# they died in millions of years, and the temperature at which they died in 
# millions of degrees. The other most important data point is whether or not
# that star supernova'd or not upon death.
#
# One at a time you are going to go through your test set to see whether you can
# correctly predict whether a star will supernova or not based on stars closest 
# to it with the training set given, following the KNN algorithm. From
# the main function we will return how accurate our test set is at predicting
# whether a star will supernova or not given said information about the star.
#
################################################################################

from math import *
from random import *
import knnTests

# This code retrives the data from the data.txt file
############ Training and Test Set ####################
def getDataFromFile(filename):
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

# Here we randomly pull half of the data out to use as our test set.
trainingSet = getDataFromFile("data.txt")
testSet = []
for i in range(len(trainingSet)//2):
    testSet.append(trainingSet.pop())

################################################################################
# Challenge 0: Print out the testSet and trainingSet.
# Notice how the data is set up: 
# [[ageOfStarAtDeath, tempOfStarAtDeath, superNova?]....]

# print(trainingSet)
# print(testSet)
################################################################################


############# KNN ###########

# Helper function to return the euclidean distance of the points on a 2-D grid.
def distance(x0, y0, x1, y1):
    dx = x1-x0
    dy = y1-y0
    return sqrt((dx**2)+(dy**2))


################################################################################
# Challenge 1: The first step is to complete the function getNeighbors. 
# We are going to calculate the distance between the current test instance
# and every point in the training instance, put them in a list, then sort them.
# Then we will pick the top k elements from the list.
# 
# Hint: If I call sort on a 2D list, then it will sort by the first element of 
# each list.
################################################################################

# Returns the K closest neighbors to |testInstance|, in order of distance
# from the test instance.
def getNeighbors(trainingSet, testInstance, k):
    # Gather the x, y points of the test instance, and initialize the lists
    # of distances.
    distances = []
    x0, y0 = testInstance[:2]

    ########################################################################
    # Challenge 1.1: Fill the |distances| list. Hint: use the distance 
    # function from above.
    # YOUR CODE HERE:


    ########################################################################

    distances.sort()
    
    neighbors = []

    ########################################################################
    # Challenge 1.2: Add the correct values to the |neighbors| list so that 
    # we return the correct list. What should this function return?
    # YOUR CODE HERE:


    ########################################################################

    return neighbors

################################################################################
# Challenge 1.3: Run the tests for getNeighbors by uncommenting the line below

# knnTests.testGetNeighbors(getNeighbors)

########################################################################



################################################################################
# Challenge 2: The next step is to complete the getLabel function. In this 
# function we are iterating through the returned neighbors, and getting the 
# True or False label and adding that label to our counts.
################################################################################

# Returns True if the majority of |neighbors| are supernovae, False otherwise
def getLabel(neighbors):

    ###########################################################################
    # YOUR CODE HERE:




    pass # Delete this line when you're finished with challenge 2.2
    ###########################################################################

################################################################################
# Challenge 2.1: Run the tests for getLabel by uncommenting the line below

# knnTests.testGetLabel(getLabel)

################################################################################



###############################################################################
# Challenge 3: The last step is to iterate through the test set in the knnMain
# function. First gather your neighbors using the getNeighbors helper function.
# Then, get the label using the getLabel helper function. Then check whether 
# the label retrieved matches the actual label and increment |correct|
# accordingly.
###############################################################################

# Returns the accuracy of our testSet at determining whether a star will supernova.
def knnMain(trainingSet, testSet, k):
    total = len(testSet)
    correct = 0
    accuracy = 0

    ###########################################################################
    # Challenge 3.1: For each instance in |testSet|, get our prediction and then 
    # update the test set accuracy.
    # YOUR CODE HERE:


    ###########################################################################

    return accuracy

################################################################################
# Challenge 3.2: Run the tests for knnMain by uncommenting the line below

# knnTests.testKnnMain(knnMain)

################################################################################



################################################################################
# Challenge 4: Run your code on the training and test sets provided by uncommenting
# the line below. Our code's accuracy is 95.6 for K=1 and K=2, and 96.3999 for K=3.

K = 3
# print(knnMain(trainingSet, testSet, K))

################################################################################



