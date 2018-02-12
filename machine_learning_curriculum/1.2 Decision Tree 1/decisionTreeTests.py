from decisionTreeActivity import getImpurity
from decisionTreeActivity import evaluateSplit
from decisionTreeActivity import getBestSplit

''' 
Here are some simple unit tests for the Decision Tree Activity.
They're designed to make sure your code at each of the challenges is correct,
which will help you debug your overall code!

Instructions: Place this file in the same directory as your 
decitionTreeActivity.py file. Then run it once you think you're done
with an activity. 

If you're completely done and your code is correct, you should see the
file print "All tests passed!"

Otherwise, you'll see some error code with an AssertionError. Look at the
Traceback that's printed and look for something that looks like:
  File "decisionTreeTests.py", line X, in <module>
Look at line X in this file and try to see why your code fails for this case!

'''


# Unit tests for Challenge 2

assert(getImpurity([(0,'','UP')]) == 0.0)
assert(getImpurity([(0,'','DOWN')]) == 0.0)
assert(getImpurity([(0,'','UP'),(0,'','UP')]) == 0.0)
assert(getImpurity([(0,'','UP'),(0,'','DOWN')]) == 0.5)
assert(getImpurity([(0,'','UP'),(0,'','DOWN'),(0,'','DOWN')]) == 4/9)

# Unit tests for Challenge 3

dataset = [(0,'','UP'),(0,'','DOWN'),(0,'','DOWN')]
split1 = dataset[:1]
split2 = dataset[1:]
assert(evaluateSplit(dataset, split1, split2) == 0.0)

dataset = [(0,'','UP'),(0,'','DOWN'),(0,'','DOWN')]
split1 = dataset[:2]
split2 = dataset[2:]
assert(evaluateSplit(dataset, split1, split2) == 1/3)

# Unit tests for Challenge 4
dataset = [(0,'UP','UP'),(0.1,'DOWN','DOWN'),(0.2,'DOWN','DOWN')]
assert(getBestSplit(dataset)[2] == [(0,'UP','UP')])

dataset = [(0,'UP','UP'),(0.1,'DOWN','DOWN'),(0.2,'DOWN','DOWN'),(0.3,'UP','UP')]
assert(getBestSplit(dataset)[2] == [(0, 'UP', 'UP'), (0.3, 'UP', 'UP')])

# If all is good, we should reach this line.
print("All tests passed!")
