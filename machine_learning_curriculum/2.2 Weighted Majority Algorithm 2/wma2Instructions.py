
# CHALLENGE 0 - 
# Print out myCityData and expertCityData to understand the dataset. The data for each
# city is a list of size 365, with integers from 0-3. The integers represent
# the weather on that day of 2017, where 0 is sunny, 1 is cloudy, 2 is rainy,
# and 3 is snowy.


# CHALLENGE 1 - Initialize the expertWeights variable. Although in the previous
# activity we had one separate variable for each expert weight, we cannot do
# that with 10 experts (too many variables!) Therefore, we will store all expert
# weights in a dictionary, that maps from city name to initial weights (1.0).


# CHALLENGE 2 - In the previous activity, we had one separate variable to store
# each expert prediction, and to store the sum of the weights of the experts
# that made each prediction (i.e. the sum of weights of experts that predicted
# True and False). This time, since we have 10 experts and 4 labels, we will
# store these in dictionaries. In this challenge, we initialize the variables 
# that will store expert predictions and the overall weight assigned to each 
# weather category.
#      1) Initialize the "expertPredictions" variable as a dictionary that maps
#         from city name to None (since they have not yet made a prediction).
#      2) Initialize the "weatherCount" variable as a dictionary that maps from
#         each weather label (an int from 0 to 3), to 0.0 (since no expert has
#         currently predicted that weather).
#      3) Finally, implement the logic inside the for loop:         
#           Get prediction for that expert (i.e. that expert's weather on the specific
#           day; note the outer for loop), add it to the "expertPredictions" 
#           dictionary, and add that expert's weight to the count for its prediction
#           in "weatherCount."


# CHALLENGE 3 - We now have to find the weather that had the largest sum of
# expert weights (that weather will be our prediction). Iterate over the
# "weatherCount" dictionary (using "weatherCount.items()"), storing the
# maxCount you have seen so far as well as the corresponding weather label.
# That weather will be the weather the algorithm will predict.


# CHALLENGE 4 - Now that we know what all the experts predicted and what the
# actual weather was in our city, re-weight all the experts. Iterate over the
# expertWeights dictionary, and multiple each weight by penalty if the expert
# prediction was not equal to the actual weather. Hint: how did we iterate
# in Challenge 3?


# CHALLENGE 5 - The algorithm is all coded up! Finally (outside the for loop),
# print expertWeights. 
# Then run your code, debug, and see if the weights you get are
# logical (higher weights mean a greater similarity between city weather).
# Which cities have the highest similarity to Pittsburgh?


# COMPREHENSION QUESTIONS - think about them and/or discuss them
# with a friend. We will discuss them at the end of class.
#    - Intuitively, the weights represent a measure of similarity -- how similar
#      that city's weather is to your city's weather. The way we measure this
#      is by starting at 1.0 and multiplying it by penalty for every day that
#      city's weather differs from your city's weather. What are strengths and
#      shortcomings of this similarity measure? What are other ways you can
#      measure the similarities between two city's weather?
#    - If City A's weight for City B is X, can you say anything about City B's
#      weight for City A? Why or why not?
#    - If you got to the BONUS CHALLENGE, you saw that we used a zero-one loss
#      to measure the effectiveness of our prediction system. What are strengths
#      and shortcomings of this loss? How else can we measure loss?


# BONUS CHALLENGE - If we were to actually use this system as a weather
# predictor, how well would it perform? To understand this, we use a notion
# called loss, which is a measure of how bad a prediction is. In this case,
# for every day let us say the loss is 1.0 if the prediction is wrong and 0.0
# if the prediction is correct (called a zero-one loss). What we want to do is
# understand the cumulative loss over time of our weighted majority prediction,
# as well as the other experts (ideally, weighted majority will be the best).
#
# To do this, we need to store the loss that our predictor and each expert
# recieve every day. Create a list, "predictionLosses", and a dictionary of lists,
# "expertLosses". At every time step, append onto "predictionLosses" 1.0 if the
# predicted weather and actual weather are the same, and 0.0 otherwise. At every
# timestep, for every expert, append onto its corresponding value in
# "expertLosses" a 1.0 or 0.0 depending on whether that expert's prediction
# was wrong or not. In the end, "predictionLosses" should be a list of size 365,
# and "expertLosses" should be a dictionary where the keys are city names and
# each value is a list of size 365. HINT: You should not have to add more than
# 5 lines of code for this.
#
# Now, uncomment the lines of code at the bottom of the code, and run. If all
# worked well, you should get a graph of how the average cumulative loss of your
# algorithm compared to each expert. Try to find interesting trends in the graph.


