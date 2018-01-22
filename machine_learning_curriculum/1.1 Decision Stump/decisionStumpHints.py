################################################################################
# HINTS
################################################################################

# CHALLENGE 2:
# Use a for loop to iterate over every element in data. Each element in data is
# a tuple, where the first element is the temperature and the the second element
# is the label (0 for cold and 1 for flu). For example, data[i][1] == 0 if the
# i-th datapoint is a cold, and data[i][1] == 1 if the i-th datapoint is a flu.
# Before the for loop, create a variable to keep track of of the number of
# zeroes in the list. Then within the for loop, if you see a zero, add one to
# that variable. At the end of the for loop, determine the fraction of 0s in the
# dataset and the fraction of 1s in the dataset by dividing numZeroes by the
# length of the data, and by dividing (len(data) - numZeroes) by the len of the
# data. Remember that you want to result to be a float, not an integer! Finally,
# return 1 - (fraction 0s)**2.0 - (fraction 1s)**2.0

# CHALLENGE 3:
# Create two variables, leftList which stores all the elements from 0:i (note that
# this excludes i) and rightList which includes all the elements from i:len(data).
# (I am using i to refer to the index you split at). Then, calculate the impurity
# of leftList and rightList using the function written in CHALLENGE 2. Next, you
# have to calulate the weight for leftList and rightList. This is equal to the
# length of the sublist, divided by the length of the overall data. Finally,
# return leftWeight*leftImpurity + rightWeight*rightImpurity

# CHALLENGE 4:
# Call the getWeightedImpurity function to get the impurity of this split.
# If it is less than minImpurity, set minImpurity to the new impurity, and set
# bestSplit to the new split index. Since this is in a for loop, it will keep
# going, continually updating the min impurity and best split until it actually
# gets the best split out of all the elements.

# CHALLENGE 5:
# In this part, we are converting from the splitIndex to the splitValue. This is
# necessary because the split index is tied to our specific training data. With
# different data (like test data), it no longer makes sense to talk about an
# index. Instead, we have to talk about the temperature value (i.e. if temp <
# 98.6, predict cold, else predict flu). Therefore, for this challenge we need to
# change the index to a temperature value. To do so, get the temperature of the
# datapoint to the left of the index (i.e. self.trainingData[bestSplitIndex-1][0])
# and the datapoint at that index, and average them to get the splitValue.

# CHALLENGE 6:
# Finally, in classify, you should check whether the datapoint (in this case, the
# datapoint is just the temperature, since we don't know the label for test data)
# is less than splitValue, in which case you will predict cold (0), or greater
# than splitValue, in which case you will predict flu (1).

# CHALLENGE 7:
# Debugging is the hardest part, but it is also the most rewarding as you understand
# why the code isn't working and finally get it to work. We can't tell you how to
# fix problems in your code because everyone will have different bugs. However,
# below are two general tips for debugging:
#
# (1) Take advantage of error messages, they are super useful! Python not only
# gives you a brief description of the error (bottom line of the error message)
# but also tells you what line it is on (third to bottom line of the error
# message). These can very easily help you fix your code fast. Search online if
# you don't know what an error message means.
#
# (2) In general print statements are very useful in debugging, since they can
# show you what is happening behind-the-scenes while your code is being run.
# We would recommend printing at various points in your code to understand
# what is going wrong. For example, you could print the training data at the
# beginning to make sure it is as you expect. You could print the impurity
# every time you call the getImpurity function, to make sure it is reasonable.
# You could print the bestSplitIndex in every iteration of the for loop, etc.
# Basically, print where you think your code might be wrong, and if you are unsure,
# print in multiple places to find out where your code is wrong.
#
# (3) If you re having trouble debugging, email us (cmu.teknowledge@gmail.com)
# with your code, a brief description of what you have tried so far, and what
# your ideas are, and we will send you suggestions.
