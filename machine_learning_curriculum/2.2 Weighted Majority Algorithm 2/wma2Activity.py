#!/usr/bin/env python3
# import matplotlib.pyplot as plt

################################################################################
# Weather Predictor
#
# There has been a war and the whole world is decimated. You and 10 other
# friends are the only people alive, and you are all split up across major
# cities around the world. In order to survive, you need to understand the
# environment that you are in. And in order to understand that, you need to
# know the weather. All weather prediction equipment from your city is gone,
# and all you have is a radio to communicate with your friends. Everyday, they
# tell you the weather in their city, and you have to use that to predict the
# weather in your city. You decide to use the weighted majority algorithm to
# do it.
#
# Refer to the wma2Instructions.py file for detailed instructions for each challenge.
#
################################################################################

# Takes in a city name and imports the corresponding data file
def getCityData(cityName):
    prefix = "./weatherDatasetByDays/"   
    suffix = ".txt"
    filename = prefix + cityName + suffix
    with open(filename, 'r') as f:
        data = eval(f.read()) # NOTE: DO NOT USE eval unless you are absolutely
                              # sure that your file is uncorruptable!!!
    return data

myCity = "Pittsburgh"
expertCities = ["Beijing", "Cairo", "Delhi", "Mexico_City", "Mumbai", "New_York", "Osaka", "Sao_Paulo", "Shanghai", "Tokyo"]

# Convert city names to city data
myCityData = getCityData(myCity)


def run(testData=None):
    # Note that expertCityData is a dictionary, where the key is a city name and
    # the value is a list (of size 365) of the average weather on that day
    if testData is None:
        global expertCities
        global myCityData
        expertCityData = {city : getCityData(city) for city in expertCities}
    else:
        expertCityData = testData["expertCityData"]
        myCityData = testData["myCityData"]

    #################################################################################
    # CHALLENGE 0 - 
    # Print myCityData and expertCityData to see what they look like.
    #################################################################################


    #################################################################################
    # CHALLENGE 1 - Initialize the expertWeights variable. 
    expertWeights = {}

    # END OF CHALLENGE 1
    #################################################################################

    # Weather Labels
    # 0 - Sunny
    # 1 - Cloudy
    # 2 - Rain
    # 3 - Snow
    numberOfWeatherLabels = 4

    # The amount to reduce expert weights by each time they are wrong
    PENALTY = 0.5 # This can be any value between 0.0 and 1.0

    for day in range(len(myCityData)):
        ############################################################################
        # CHALLENGE 2 - 
        #      1) Initialize the "expertPredictions" variable. 
        #           Question: why do we need this variable?
        #      2) Initialize the "weatherWeights" variable
        #      3) Finally, implement the logic inside the for loop below

        expertPredictions = {} 
        weatherWeights = {} 

        # Iterate over every expert, and get their prediction (the weather in that
        # city on the specific day)
        for expertCityName in expertCities:
            ########################################################################
            # FILL THE BODY OF THE FOOR LOOP IN HERE
            # Get prediction for that expert (i.e. that expert's weather on the specific
            # day; note the outer for loop), add it to the "expertPredictions" 
            # dictionary, and add that expert's weight to the count for its prediction
            # in "weatherWeights."


            pass # Delete this line when you're finished with this challenge
            ########################################################################

        # END OF CHALLENGE 2
        ############################################################################

        ############################################################################
        # CHALLENGE 3 - We now have to find the weather that had the largest sum of
        # expert weights (that weather will be our prediction). Break ties with the
        # weather with the lowest integer value.
        m = 0
        label = 0
        for weather, value in weatherWeights.items():
            ########################################################################
            # FILL THE BODY OF THE FOOR LOOP IN HERE


            pass # Delete this line when you're finished with this challenge
            ########################################################################

        predictedWeather = None  # Set this to the weather label that had the max count

        if testData is not None and predictedWeather != testData["expPrediction"][day]:
            # If in test mode, test that our prediction is correct.
            print("Wrong prediction! Should be", testData["expPrediction"][day], 
                    "but got", predictedWeather)
            assert(False)

        # END OF CHALLENGE 3
        ############################################################################


        # Get the actual weather
        actualWeather = myCityData[day]

        ############################################################################
        # CHALLENGE 4 - Reweight the expert cities. Use the PENALTY variable defined
        # above.

        for city, weight in expertWeights.items():
            prediction = expertPredictions[city]

            if prediction != actualWeather:
                expertWeights[city] *= PENALTY

        if testData is not None and expertWeights != testData["expWeight"][day]:
            # If in test mode, test that our weights were updated correctly.
            print("Wrong weights! Should be", testData["expWeight"][day], 
                    "but got", expertWeights)
            assert(False)


        # END OF CHALLENGE 4
        ############################################################################

        # For Challenge 5:
        # print(expertWeights)

# End of run function
################################################################################


################################################################################
# BEGIN TESTS
# Note that these are "integration tests," not "unit tests"

# Test 1: Tiebreaking
testData = {}
testData["expertCities"] = [0,1,2]
testData["expertCityData"] = {2: [0,0,0], 1: [1,1,1], 0: [2,2,2]}
testData["myCityData"] = [2,1,0]
testData["expWeight"] = [
        {0: 1.0, 1: 0.5, 2: 0.5},
        {0: 0.5, 1: 0.5, 2: 0.25},
        {0: 0.25, 1: 0.25, 2: 0.25}
        ]
testData["expPrediction"] = [0, 2, 1]
print ("Running test 1")
# run(testData)


# Test 2: Summing weights
testData = {}
testData["expertCities"] = [0,1,2]
testData["expertCityData"] = {2: [0,1,2], 1: [2,1,0], 0: [1,0,2]}
testData["myCityData"] = [0,1,2]
testData["expWeight"] = [
        {2: 1.0, 1: 0.5, 0: 0.5},
        {2: 1.0, 1: 0.5, 0: 0.25},
        {2: 1.0, 1: 0.25, 0: 0.25}
        ]
testData["expPrediction"] = [0, 1, 2]
print ("Running test 2")
# run(testData)


print("All tests pass!")
################################################################################


################################################################################
# CHALLENGE 5 - Uncomment "run()" and the print statement at the end of the
# run function. Do the weights for each city make sense?
# Then, change myCityName from Pittsburgh to a different city from the expertCity
# list (and put Pittsburgh into the expertCity list). See what changes!

run()

################################################################################


################################################################################
# Finally, do the comprehension questions and bonus challenge!
################################################################################



################################################################################
# # BONUS CHALLENGE UNCOMMENT THIS
# 
# First, uncomment the import on line 2
#
# # Convert Loss to Cumulative Loss
# predictionCumulativeLoss = [0.0]
# for loss in predictionLoss:
#     predictionCumulativeLoss.append(predictionCumulativeLoss[-1] + loss)
# expertCumulativeLosses = {city : [0.0] for city in expertCities}
# for expertCityName, expertLoss in expertLosses.items():
#     for loss in expertLoss:
#         expertCumulativeLosses[expertCityName].append(expertCumulativeLosses[expertCityName][-1] + loss)
#
# # Convert Cumulative Loss to Average Cumulative Loss
# predictionAverageCumulativeLoss = [predictionCumulativeLoss[t+1]/(t+1) for t in range(len(predictionCumulativeLoss)-1)]
# expertAverageCumulativeLosses = {city : [expertCumulativeLosses[city][t+1]/(t+1) for t in range(len(expertCumulativeLosses[city])-1)] for city in expertCities}
#
# # Plot the Cumulative Losses
# fig, ax = plt.subplots()
# ax.set_title("Average Cumulative Loss for " + myCity + " Weather")
# expertColors = ["red", "orange", "yellow", "green", "turquoise", "purple", "pink", "indigo", "brown", "black"]
# i = 0
# for expertCityName, expertAverageCumulativeLoss in expertAverageCumulativeLosses.items():
#     color = expertColors[i]
#     ax.plot(range(1, len(expertAverageCumulativeLoss)+1), expertAverageCumulativeLoss, color=color, label=expertCityName)
#     i += 1
# color = "blue"
# ax.plot(range(1, len(predictionAverageCumulativeLoss)+1), predictionAverageCumulativeLoss, color=color, label="WMA")
# ax.set_xlabel("Timesteps")
# ax.set_ylabel("Average Loss")
# ax.grid()
# ax.legend(loc='center left', bbox_to_anchor=(0.90, 0.5))
# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()
# plt.show()
################################################################################




