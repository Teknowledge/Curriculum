
# CHALLENGE 2 - Next, write the getImpurity function. In this function, you
# should first determine the number of points in the dataset with the
# "UP" label, and the number of points with the "DOWN" label (be sure one to
# get confused between yesterday's UP/DOWN labels, which are ar index 1, and
# today's UP/DOWN labels, which are at index 2). Once you have the number of
# points, calculate the fraction of points in the dataset that have the up label
# and the down label. Finally, use that to calculate the impurity, using the Gini
# Impurity measure we taught in class.


# CHALLENGE 3 - The next step is to write the evaluateSplit function. Remember,
# this is a weighted average of the impurities in both splits, weighted by
# the fraction of the elements from the original data that is in each split.
# In other words, return the split1 impurity times the split1 fraction, plus the
# split2 impurity times the split2 fraction.


# CHALLENGE 4 - Now the next step is to generate the best split. We do so by
# trying every single splitting point, for every single attribute, and keeping
# track of which results in the least impure splits. We have given the code for
# evaluating the least impure of all aplits aloung the first attribute, the
# simple moving average. Now, write the code to evaluate a better split (if one
# exists) along the second attribute. HINT: most of the code should be the
# same as the first attribute -- you just have to change the attribute index and
# the attribute options.


# CHALLENGE 5 -  This function takes in an instance of the Node class. First, it
# should check if that node's training data is fully pure (base case) by calling
# getImpurity on node.trainingData. If impurity is zero (the node is pure) then
# return since this node is done.
# If the impurity isn't zero, we have more work to do. For the rest of this function,
# pay attention to the inputs and outputs of the functions we call!
# The next thing the function should do is get the best split for node.trainingData
# using getBestSplit(). This tells us where to split our current node's data.
# Next, we should call node.setSplit() on the node to set and get its left and right
# children (NOTE: don't swap the left and right children).
# Finally, we need to make sure that all our children have pure data too.
# So the function should call itself recursively on the left and right children (i.e.
# call createDecisionTreeRecursive twice, once for each child).
# Note that this function does not have to return anything, since it mutably modifies
# the node. (Ask a mentor if you are curious about what this means.)
