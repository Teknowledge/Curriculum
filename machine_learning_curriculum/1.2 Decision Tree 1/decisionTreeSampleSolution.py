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
# was open in 2017. Good luck!
#
################################################################################

################################################################################
# DO NOT MODIFY THIS PART OF THE FILE (unless you know what you are doing :P )
#
# However, skim through it to make sure you understand what it is supposed to
# do.
################################################################################
import csv, random

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
        # Similar to getImpurity, calculate the upFraction and downFraction
        # from node.trainingData
        # Get the number of datapoints with up and down labels
        ########################################################################
        upPoints, downPoints = 0, 0
        for nodeData in node.trainingData:
            if nodeData[2] == "UP":
                upPoints += 1
            else:
                downPoints += 1
        # Convert the counts to fractions
        upFraction = float(upPoints)/float(len(node.trainingData))
        downFraction = float(downPoints)/float(len(node.trainingData))
        randomNumber = random.random() # returns a random float in [0.0, 1.0)
        if randomNumber < upFraction: # true upFraction of the time
            predictedLabel = "UP"
        else: # true downFraction of the time
            predictedLabel = "DOWN"
        ########################################################################
        # BONUS CHALLENGE - Comment out the below line
        # predictedLabel = node.trainingData[0][2]

        actualLabel = data[2]
        if predictedLabel == actualLabel: numCorrect += 1
    return float(numCorrect)/float(len(testData))

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
# WRITE YOUR CODE BELOW THIS
################################################################################

# Returns a float that represents the impurity of the data, according to the
# Gini Impurity
def getImpurity(dataset):
    ############################################################################
    # Get the number of datapoints with up and down labels
    upPoints, downPoints = 0, 0
    for data in dataset:
        if data[2] == "UP":
            upPoints += 1
        else:
            downPoints += 1
    # Convert the counts to fractions
    upFraction = float(upPoints)/float(len(dataset))
    downFraction = float(downPoints)/float(len(dataset))
    return 1.0 - ((upFraction)**2.0 + (downFraction)**2.0)
    ############################################################################

# evaluateSplit takes in three lists -- the overall data list, and the two lists
# it is split into. It then returns a float corresponding to how good the
# split is
def evaluateSplit(dataset, split1, split2):
    ############################################################################
    # First, get the weights of each split (i.e. what fraction of elements from
    # the original dataset are in the split)?
    split1Weight = float(len(split1))/float(len(dataset))
    split2Weight = float(len(split1))/float(len(dataset))
    # Next, get the impurity of each split
    split1Impurity = getImpurity(split1)
    split2Impurity = getImpurity(split2)
    # Return the weighted average of these impurities
    weightedImpurity = split1Impurity*split1Weight + split2Impurity*split2Weight
    return weightedImpurity
    ############################################################################


# generates the best split of the data. It returns the attributeIndex to split on,
# the value of the split, and the two resulting lists after splitting along
# that attributeIndex and value.
def getBestSplit(dataset):
    # Initialize variables to keep track of the best split we have seen so far
    minImpurity = None
    minAttributeIndex = None
    minValue = None
    minSplit1 = None
    minSplit2 = None
    # First, try splitting along the first attribute (index 0)
    sortedDataset = sorted(dataset) # sort it so that every value except the max can be used as a splitting point
    firstAttributeSplitOptions = [sortedDataset[i][0] for i in range(len(dataset)-1)]
    for value in firstAttributeSplitOptions:
        split1, split2 = splitData(dataset, 0, value) # Remember, the first attribute is at index 0!!!
        impurity = evaluateSplit(dataset, split1, split2)
        if (minImpurity is None or impurity < minImpurity): # we found a better split!
            minImpurity = impurity
            minAttributeIndex = 0
            minValue = value
            minSplit1 = split1
            minSplit2 = split2
    # Next, write code to split along the second attribute (index 1)
    ############################################################################
    secondAttributeSplitOptions = ["UP", "DOWN"]
    for value in secondAttributeSplitOptions:
        split1, split2 = splitData(dataset, 1, value) # Remember, the second attribute is at index 1!!!
        impurity = evaluateSplit(dataset, split1, split2)
        if (minImpurity is None or impurity < minImpurity): # we found a better split!
            minImpurity = impurity
            minAttributeIndex = 1
            minValue = value
            minSplit1 = split1
            minSplit2 = split2
    ############################################################################
    return minAttributeIndex, minValue, minSplit1, minSplit2

# This function takes in a node, and checks if its trainingData is fully pure
# (base case). If not, it generates the best split of that training data,
# sets that split for the node to get its new left and right children, and
# calls itself recursively on the two children.
def makeDecisionTreeRecursively(node, currentDepth, maxDepth):
    ############################################################################
    # Is this node finished yet or not?
    impurity = getImpurity(node.trainingData)
    if impurity == 0.0 or currentDepth == maxDepth:
        return 0 # this node is done
    # If this node is not yet finished
    attributeIndex, value, split1, split2 = getBestSplit(node.trainingData)
    leftNode, rightNode = node.setSplit(attributeIndex, value, split1, split2)
    # Call this function recursively on the children
    depth1 = makeDecisionTreeRecursively(leftNode, currentDepth+1, maxDepth)
    depth2 = makeDecisionTreeRecursively(rightNode, currentDepth+1, maxDepth)
    return max(depth1+1, depth2+1) # this node is done
    ############################################################################

# Initializes the decision tree with the starting node, then calls the recursive
# function to build the rest of the decision tree
def createDecisionTree(trainingData):
    maxDepth = 175
    startingNode = Node(trainingData)
    depth = makeDecisionTreeRecursively(startingNode, 1, maxDepth)
    print("Depth: "+str(depth+1))
    return startingNode

# First, get the training data
trainingData = loadDataFromFile("trainingData.csv")
# Then, create the decision tree
decisionTree = createDecisionTree(trainingData)

# Now, get the test data
testData = loadDataFromFile("testData.csv")
# Test the decision tree on the test data
accuracy = testDecisionTree(decisionTree, testData)
print("Accuracy: "+str(accuracy))
