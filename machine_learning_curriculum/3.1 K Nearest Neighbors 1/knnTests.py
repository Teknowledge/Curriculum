from random import shuffle

def assertEqual(tested, expected, testFun, testNum):
    if tested != expected:
        print(testFun, "test number", testNum, "fails") 
    assert(tested == expected)

def testGetNeighbors(getNeighbors):
    # Test 1
    trainingSet = [[1,1,True],[0,0,True]]
    testInstance=[0,0,False]
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=0),
                expected=[],
                testFun="getNeighbors", testNum=1)
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=1),
                expected=[[0, 0, True]],
                testFun="getNeighbors", testNum=1)
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=2),
                expected=[[0, 0, True], [1, 1, True]],
                testFun="getNeighbors", testNum=1)

    # Test 2
    trainingSet = [[1,1,True],[0,0,True],[2,2,True],[3,3,True],[4,4,True]]
    testInstance=[3,4,False]
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=2),
                expected=[[3, 3, True], [4, 4, True]],
                testFun="getNeighbors", testNum=2)
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=3),
                expected=[[3, 3, True], [4, 4, True], [2, 2, True]],
                testFun="getNeighbors", testNum=2)

    # Test 3
    trainingSet = [[1,1,True],[2,2,True],[3,3,True],[3.9,3.9,False]]
    testInstance=[3.5,3.5,False]
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=1),
                expected=[[3.9, 3.9, False]],
                testFun="getNeighbors", testNum=3)

    # Test 4
    trainingSet = [[-3,-3,True],[-3.9,-4,True]]
    testInstance=[-3,-4,False]
    assertEqual(tested=getNeighbors(trainingSet, testInstance, k=1),
                expected=[[-3.9, -4, True]],
                testFun="getNeighbors", testNum=4)

    print("All getNeighbors tests pass!")


def testGetLabel(getLabel):
    # Test 1
    assertEqual(getLabel([[0,0,True],[0,0,False],[0,0,False]]),
            False, "testGetLabel", 1)

    # Test 2
    bigNeighbors = [[0,0,True]]*1000 + [[0,0,False]]*1001
    shuffle(bigNeighbors)
    assertEqual(getLabel(bigNeighbors), False, "testGetLabel", 2)

    # Test 3
    bigNeighbors = [[0,0,True]]*1000 + [[0,0,False]]*999
    shuffle(bigNeighbors)
    assertEqual(getLabel(bigNeighbors), True, "testGetLabel", 3)

    print("All getLabel tests pass!")

def testKnnMain(knnMain):
    # Test 1
    trainingSet = [[1,1,False],[2,2,False],[0,0,True]]
    testSet=[[0,0,False]]
    assertEqual(tested=knnMain(trainingSet, testSet, k=1),
                expected=0.0, testFun="testKnnMain", testNum=1)
    assertEqual(tested=knnMain(trainingSet, testSet, k=3),
                expected=100.0, testFun="testKnnMain", testNum=1)

    # Test 2
    trainingSet = [[1,1,False],[2,2,False],[0,0,True]]
    testSet=[[0,0,False],[1,1,False]]
    assertEqual(tested=knnMain(trainingSet, testSet, k=1),
                expected=50.0, testFun="testKnnMain", testNum=2)
    assertEqual(tested=knnMain(trainingSet, testSet, k=3),
                expected=100.0, testFun="testKnnMain", testNum=2)

    print("All knnMain tests pass!")


