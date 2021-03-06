import math
import pickle

################################################################################################
# Predicting Cold or Flu
#
# Various students have had their temperatures taken at the school infirmary.  As the infirmary
# doctor you are trying to figure out if the students have a cold or a flu so you have a better
# idea of what to do next to help them.
#
# Based on previous student's temperatures and the illness that they had, you can use decision
# stumps to find what a good dividing point is for a future student's temperature to predict
# whether the student has a cold or flu!
#
# A note on terminology: a "class" or "label" is what we're trying to classify.
# In our case, it can be either 0 or 1. In the flu example, cold = 0, flu = 1.
#
# Complete this activity by following the numbered challenges in order. First,
# try to do each challenge by yourself. If you need a hint, look at the
# "decisionStumpHints.py" file for pseudocode and other hints.
#
#################################################################################################

################################################################################
# CHALLENGE 1:
# Briefly read through the code below and see how the pieces fit together and
# correspond to the pseudocode you wrote. Don't write any code yet!
################################################################################

def getImpurity(data):
    """
    Returns the Gini impurity of |data|
    """
    # Let's say the impurity of an empty list is 0.
    if len(data) == 0:
        return 0

    ############################################################################
    # CHALLENGE 2:
    # Fill out the rest of this function to return the Gini impurity of
    # the input list.
    ############################################################################

    return 0 # Delete this line when you begin Challenge 2


def getWeightedImpurity(data, possibleSplitIndex):
    """
    Returns the weighted impurity of |data| split into two lists by |possibleSplitIndex|
    """

    ############################################################################
    # CHALLENGE 3:
    # Use the function you wrote in Challenge 2 to now return the weighted impurity
    # of the input list |data| if it were split at |possibleSplitIndex|. A "split" is
    # an index in the  list where we split the list into two parts: 1) everything to
    # the left of the index, 2) everything to the right of the index, including the index.
    ############################################################################

    return 0 # Delete this line when you begin Challenge 3

class DecisionStump:
    """
    This class represents a single Decision Stump. To create a decision stump,
    do "exampleStump = DecisionStump(data)".
    The data should be the elements of the training data to train on.
    """

    def __init__(self, trainingData):
        # No need to modify this function! Just take a look at the class variables.

        # |trainingData| is a list of tuples. A tuple in the list is the pair (value, class)
        # where |class| is either 0 or 1.
        # For example, a tuple could be (99.7, 0)

        # Initialize class variables
        self.splitValue = 0

        # First, we sort the data. Because the data is a list of tuples, we use a
        # special way to sort that takes a "lambda function." You don't have to worry
        # about how this works. Now the list is sorted by increasing values (temperatures).
        self.trainingData = sorted(trainingData, key=lambda x: x[0])

    def train(self):
        # This function finds the index that divides the two splits with the lowest impurity
        # It then sets self.splitValue to the mean of the cells to the right and left of the
        # split. See Challenge 3 for the definition of a split.

        # Initialize |minImpurity| to greater than the maximum possible value of an impurity
        minImpurity = 1.1

        # We will update this value with better splits. A "split" is an index in the
        # list where we split the list into two parts: 1) everything to the left of
        # the index, 2) everything to the right of the index, including the index.
        bestSplitIndex = -1

        # Try all possible places to split the list.
        for possibleSplitIndex in range(len(self.trainingData)):

            ####################################################################
            # CHALLENGE 4
            # For all possible places to split the list, call the function we wrote in
            # Challenge 3. If the impurity we get is smaller than minImpurity, we should
            # update minImpurity and bestSplitIndex with the current split index and impurity.
            ####################################################################

            continue # Delete this line when you begin Challenge 4.

        if bestSplitIndex == 0:
            # If the best split is to put everything in the right side, then we should
            # always classify everything as 1 by setting splitValue to negative infinity.
            # (If you'd like, think about why this works.)
            self.splitValue = -float('inf')
        elif bestSplitIndex == len(self.trainingData) - 1:
            # If the best split is to put everything in the left side, then we should
            # always classify everything as 1 by setting splitValue to infinity.
            self.splitValue = float('inf')
        else:

            ####################################################################
            # CHALLENGE 5
            # Here, we know that the split point is not at the left or right of the list.
            # So, change the next line so that self.splitValue is set to the mean of the
            # values directly to the left and right of the splitting point.
            ####################################################################

            self.splitValue = 0 # Delete 0 and replace it with the correct value here.

        print ("Finished training the decision stump. Our split value is", self.splitValue)

    def classify(self, datapoint):
        """
        Returns an int value 0 or 1 denoting flu or cold if you input a single datapoint
        """

        ########################################################################
        # CHALLENGE 6
        # Given a datapoint to test, we want to return whether its class should be
        # 0 or 1. Use self.splitValue to help you decide.
        ########################################################################

        return 0 # Delete this line when you begin Challenge 6

################################################################################
# Below this line are utility functions to create and test the decision stump.
# Feel free to try to understand what's going on if you're curious.
################################################################################

def loadDataFromFile(filepath):
    """
    This function takes in a filepath to the temperature data, and returns a list of
    2-tuples representing the data.
    """
    name = str(filepath)
    output = pickle.load(open(name, "rb" ))
    return output


def testDecisionStump(trainingData, testData):
    """
    This function takes in a decision stump and the test data, and returns how accurate the
    decision tree is on the test data.  Please use this to test how accurate you are.
    """
    numCorrect = 0
    stump = DecisionStump(trainingData)
    stump.train()

    for i in range(len(testData)):
        label = stump.classify(testData[i][0])
        if label == testData[i][1]:
            numCorrect +=1

    return float(numCorrect) / float(len(testData))

################################################################################
# CHALLENGE 7
# Run and test your code! If you're having issues, consider debugging by printing values at
# intermediate points in your algorithm. For example, maybe print the impurities you get
# at each split in Challenge 4. Also, consider printing the actual labels and your
# predictions for each test datapoint in testDecisionStump.
################################################################################

studentDataPure = loadDataFromFile("studentDataPure.p")
acc = testDecisionStump(studentDataPure, studentDataPure)
# If your implementation is correct, this value should be 100%.
print ("Accuracy of our decision stump on the training data is", str(acc*100) + "%")


studentTest = loadDataFromFile("studentTest.p")
acc = testDecisionStump(studentDataPure, studentTest)
# If your implementation is correct, this value should be 80%.
# Why is the accuracy worse on the test data than on the training data?
print ("Accuracy of our decision stump on the test data is", str(acc*100) + "%")

################################################################################
# BONUS CHALLENGE 1
# There is actually a bug in this implementation of decision trees. When
# calculating splitValues and using the splitValue to classify datapoints,
# we assume that every point below the split is a 0 and every point above the
# split is a 1. However, that is not necessarily true. For example, consider the
# below data:
#
# 93.0, 1
# 94.5, 1
# 96.8, 0
# 98.6, 0
#
# In this case, our decision tree algorithm will misclassify all points. This is
# not good, since we ideally want a general decision tree implementation that
# can work regardless of the data. Find a way to modify this implementation so
# that after calculating a splitValue, it predicts the label that is most common
# below/above the splitValue. It is extra good if you don't iterate over the
# training data in the classify function (since that is inefficient).
################################################################################

################################################################################
# BONUS CHALLENGE 2
# Also test your decision stump implementation on the impure dataset, by
# modifying the lines between CHALLENGE 7 and the BONUS CHALLENGE. If your
# implementation is correct, your training accuracy should be 78.57142857142857%
# and your test accuracy should be 66.66666666666666%. Why does it make sense
# that our decision stump is less accurate for impure data?
################################################################################
