from decisionTreeActivity import getImpurity
from decisionTreeActivity import evaluateSplit
from decisionTreeActivity import getBestSplit

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
