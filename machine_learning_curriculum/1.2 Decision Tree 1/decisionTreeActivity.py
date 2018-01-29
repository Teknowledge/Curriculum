#!/usr/bin/env python3
################################################################################
# Stock Shark
#
# Have you heard of the stock market? If so, you probably know that some people
# have gotten VERY rich trading stocks. However, it is not that easy to do.
# It is very difficult to predict the stock market, and therefore hard to know
# when your money will increase or decrease in value. To help with that, we
# will use machine learning to predict whether the S&P 500, an indicator of
# how well the stocks of 500 of the most influential companies, will go up or
# down today, using yesterday's values. Let's see whether machine learning can
# help us become billionaires!
#
# Each element of our training data contains three entries. The first is the
# simple moving average of the daily change in the stock value over the last
# 14 days (float). The second is a string representing whether the stock
# increased ("UP") or decreased ("DOWN") yesterday. The third is a string
# indicating whether the stock increased or decreased today. Your goal is to
# create a decision tree that uses the first two (yesterday's values) to predict
# the last one (today's value). The training data is from every day the stock
# market was open in 2016, and the test data is from every day the stock market
# was open in 2017.
#
# Like last week, follow the numbered challenges in order. First, try to do each
# challenge by yourself. If you need a hint, look at the "decisionStumpHints.py"
# file for pseudocode and other hints.
#
# Good luck!
#
################################################################################

################################################################################
# DO NOT MODIFY THIS PART OF THE FILE (unless you know what you are doing :P )
#
# However, skim through it to make sure you understand what it is supposed to
# do.
################################################################################
import csv, random

################################################################################
# CHALLENGE 0 - The first part of any problem that uses data is to understand
# the dataset. Go to where we load the training data in this file (near the
# end of the code), and print the trainingData. Make sure you understand
# what the data is, and how to interact with it (ask a friend or mentor for
# help if you are unsure).
# Also, note what the baseline accuracy of our untrained decision tree is!
################################################################################


# This class represents a single node in the decision tree. To create a Node,
# do "exampleNode = Node(data)". The data should be the elements of the training data
# that have filtered down to this node. And then to split this node into two
# children, do "exampleNode.setSplit(attributeIndex, value, split1, split2)".
# Attribute index should be the index of the attribute you are splitting on --
# 0 for simple moving average, and 1 for whether the stock went up or down
# yesterday. Value is the value you are splitting on (i.e. if you are
# checking whether the simple moving average is <= 50.0, the index is 0 and
# the value is 50.0). Split1 and split2 are the two splits
class Node(object):
    def __init__(self, trainingData):
        self.trainingData = trainingData
        self.attributeIndex = None
        self.value = None
        self.leftChild = None
        self.rightChild = None

    def setSplit(self, attributeIndex, value, split1, split2):
        self.attributeIndex = attributeIndex
        self.value = value
        self.leftChild = Node(split1)
        self.rightChild = Node(split2)
        return self.leftChild, self.rightChild

# this function takes in a filepath to the stock data, and returns a list of
# 3-tuples representing the data.
def loadDataFromFile(filepath):
    with open(filepath, 'rt') as csvfile:
        fileReader = csv.reader(csvfile)
        data = []
        for row in fileReader:
            if len(row) < 3: break
            data.append((float(row[0].strip()), row[1].strip(), row[2].strip()))
        return data

# this function takes in a decision tree and the test data, and returns how
# accurate the decision tree is on the test data
def testDecisionTree(decisionTree, testData):
    numCorrect = 0
    for data in testData:
        node = decisionTree
        # Keep going down the tree until we reach a leaf
        while not (node.leftChild is None or node.rightChild is None):
            if node.attributeIndex == 1:
                if data[node.attributeIndex] == node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
            else:
                if data[node.attributeIndex] <= node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
        # Now, "node" is a leaf. Predict the label at this leaf from the training data
        ########################################################################
        # BONUS CHALLENGE - FILL THIS IN AND UNCOMMENT THE LINES
        #
        # # Similar to getImpurity, calculate the upFraction and downFraction
        # # from node.trainingData
        # randomNumber = random.random() # returns a random float in [0.0, 1.0)
        # if randomNumber < upFraction: # true upFraction of the time
        #     predictedLabel = "UP"
        # else: # true downFraction of the time
        #     predictedLabel = "DOWN"
        ########################################################################
        # BONUS CHALLENGE - Comment out the below line
        predictedLabel = node.trainingData[0][2]

        actualLabel = data[2]
        if predictedLabel == actualLabel: numCorrect += 1
    return float(numCorrect)/float(len(testData))


################################################################################
# CHALLENGE 1 - If you recall, the decision tree algorithm consists of finding
# the best splitting point, splitting the data, and continuing from there until
# you have perfectly separated the data. We have written the splitData function
# for you, which takes in the dataset, an attribute index to split on, and a
# value at which to split, and splits the dataset into two along that attribute.
# Read through the splitData function, and make sure you understand what it is doing.
# Ask a mentor if you are unsure!
################################################################################

# Splits the dataset into two, and returns the two lists. If the attributeIndex
# is 1, split1 will contain those data points where yesterday's change is ==
# to value, and split2 will contain the points that were not equal to value.
# If attributeIndex is 0, split1 will contain the points whose simple moving
# average is <= value, and split2 will contain the points whose simple moving
# average is > value.
def splitData(dataset, attributeIndex, value):
    split1, split2 = [], []
    for data in dataset:
        # Index 1 has only two values, "UP" or "DOWN". Therefore, we want to
        # compare it with ==, not <=.
        if attributeIndex == 1:
            if data[attributeIndex] == value:
                split1.append(data)
            else:
                split2.append(data)
        # Index 0 has infinite float values, so we want to compare it with <=
        # and not ==
        else:
            if data[attributeIndex] <= value:
                split1.append(data)
            else:
                split2.append(data)
    # Return the splits
    return split1, split2


################################################################################
# WRITE YOUR CODE BELOW THIS LINE
################################################################################

# Returns a float that represents the impurity of the data, according to the
# Gini Impurity
def getImpurity(dataset):
    ############################################################################
    # Challenge 2: Implement the getImpurity function below this line.
    # Feel free to copy or refer to your code from last week, but note that the
    # dataset consists of three-tuples this time.
    ############################################################################

    # Write your code here!

    return 0 # TODO remove this line once you begin the challenge.

# evaluateSplit takes in three lists: the overall data list, and the two lists
# it is split into. It then returns a float corresponding to how good the
# split is (i.e. the weighted impurity).
def evaluateSplit(dataset, split1, split2):
    ############################################################################
    # Challenge 3: Implement the evaluateSplit function below this line.
    # Again, feel free to copy or refer to your code from last week, but note that
    # the inputs to the function are different than the inputs from last week.
    ############################################################################

    # Write your code here!

    return 0 # TODO remove this line once you begin the challenge.


# Generates the best split of the data. It returns the attributeIndex to split on,
# the value of the split, and the two resulting lists after splitting along
# that attributeIndex and value.
def getBestSplit(dataset):
    # Initialize variables to keep track of the best split we have seen so far
    minImpurity = None
    minAttributeIndex = None
    minValue = None
    minSplit1 = None # Should be set to the left list after the split.
    minSplit2 = None # Should be set to the right list after the split.

    # First, we try splitting along the first attribute (index 0)

    # Sort the dataset so that every value of the first attribute but the max
    # can be used as a splitting point. Note: you do not have to do this for the
    # second attribute. (Think about why that is if you like.)
    sortedDataset = sorted(dataset)
    firstAttributeSplitOptions = [sortedDataset[i][0] for i in range(len(dataset)-1)]
    for value in firstAttributeSplitOptions:
        # In Python, you can specify the parameter name when you pass in values to a
        # function, like we do here. It's a way to write more readable code.
        split1, split2 = splitData(dataset=dataset, attributeIndex=0, value=value)
        impurity = evaluateSplit(dataset, split1, split2)
        if (minImpurity is None or impurity < minImpurity): # we found a better split!
            minImpurity = impurity
            minAttributeIndex = 0
            minValue = value
            minSplit1 = split1
            minSplit2 = split2

    ############################################################################
    # Challenge 4: Under this line, add code to finish implementing the getBestSplit
    # function.
    # You'll have to write code to split along the second attribute (index 1) to find
    # the best split location. Your code should be very similar to the code above
    # that splits along the first attribute, except remember that the second attribute
    # is a binary attribute!
    ############################################################################

    # Write your code here!

    return minAttributeIndex, minValue, minSplit1, minSplit2

# This function takes in a node, and checks if its trainingData is fully pure
# (base case). If not, it gets the best split of the node's training data,
# sets that split for the node to get its new left and right children, and
# calls itself recursively on its two children. This function does not return
# anything and instead modifies the internals of the input node.
def makeDecisionTreeRecursively(node):
    ############################################################################
    # Challenge 5.1: Understand the Node class defined near the top of this file. Make
    # sure you understand what the node.setSplit function does.
    #
    # Challenge 5.2: Finally, we are going to write the core logic of a decision tree
    # that differentiates it from a decision stump -- namely, the recursion.
    # Add code to implement the makeDecisionTreeRecursively function.
    #
    # Hint: you will have to call makeDecisionTreeRecursively at some point within this
    # function. Refer to the hints file for more hints.
    # This function should be around 8 lines long without comments.
    ############################################################################

    # Write your code here!

   return

# Initializes the decision tree with the starting node that has all the training data,
# then calls the recursive function to build the rest of the decision tree
def createDecisionTree(trainingData):
    startingNode = Node(trainingData)
    makeDecisionTreeRecursively(startingNode)
    return startingNode

# First, get the training data
trainingData = loadDataFromFile("trainingData.csv")
# Then, create the decision tree
decisionTree = createDecisionTree(trainingData)

# Now, get the test data
testData = loadDataFromFile("testData.csv")
# Test the decision tree on the test data
accuracy = testDecisionTree(decisionTree, testData)
print("Accuracy: "+str(accuracy)) # Should be 0.5059760956175299


# NOTE: Make sure to keep the order of split1 and split2 the same -- don't mix
# them up! Also, be sure to NOT call setSplit on a leaf node (i.e. a node with
# perfect purity)!


# BONUS CHALLENGE - Every dataset will have some data that represents trends,
# and other data that represents noise (random deviations in the dataset). A
# good machine learning algorithm should learn the trends from the data, but
# not the noise (because if the algorithm customizes itself to something that
# was just due to random chance, then it won't perform as well on future data).
# The act of learning something in the data that was actually due to randomness
# and not a trend is called overfitting.
#
# Overfitting is a big problem with decision trees, since we keep growing the
# tree until every single leaf contains a pure subset of the training data.
# Therefore, we are bound to hardcode some of the noise into our decision tree.
# One way to get around that is by limiting the depth of the decision tree.
# Add two additional parameters to the recursive function, maxDepth and
# currentDepth. Then, modify the recursive function so the tree stops growing
# not only when the impurity is 0, but also when we have exceeded maxDepth.
# In other words, you are modifying the base case of the recursive function.
#
# After modifying the recursive function, you also have to modify how we use the
# decision tree to make predictions. Now, just being at a leaf does not guarentee
# that we have one set label (since some leaves may contain UP and DOWN values).
# Therefore, we have to modify the way we predict a label by looking at what
# fraction of the data at that node is UP, what fraction is DOWN, and picking
# a random label which is UP or DOWN that appropriate fraction of the time.
# Make this modification in the testDecisionTree function.
#
# Lastly, modify the createDecisionTree function, where the recursive function
# is called.
#
# Finally, test it out. Play around with different max depths and look at the
# corresponding accuracy. What was the overall depth of the tree before this
# change? Which depth has the best accuracy? What does that tell you about
# overfitting?
