# You’ve got a list, and you want to do something useful on it. Let’s check out
# looping over them in two different ways.

favMovies = ["Finding Dory", "Star Wars: The Force Awakens", "Frozen"]
favMoviesRating = [4.8, 4.5, 4.8]
print("Here are my favourite movies:")
for movie in favMovies:
    print(movie)
# but with this you’re unable to figure out the rank of the movies. What would 
# you have o

print("Here are my favourite movies, with rank:")
for movie in range(len(favMovies)):
	print(index, favMovies[index])
# but what if you wanted to see them in reverse order?
for movie in range(len(favMovies)):
    revIndex = len(favMovies)-1-movie
    print("Movies in reverse[", revIndex, "] =", favMovies[revIndex])
# But while you do all of that, please don’t do thing destructively!

# Comparing Lists
# Let’s say you want to compare your favourite list of actors with your friend
# you would have two different lists, and you can do a direct comparison.
johnFavActors = [“Sean Connery”, “Johnny Depp”, “Tom Cruise”]
jackFavMovies = [“Will Smith”, “Tom Hanks”, “Brad Pitt”]
print(johnFavMovies == jackFavMovies)

# what would happen if the list contained the same actors, but in a different order?
# what would happen if the list had a different number of actors?

# Copying Lists
# The ability to copy lists is crucial, so pay attention! Copying a list means
# that you call a function, copy.copy(), on the list so that you can get a
# copy and change that without affecting the original
import copy
worldWarMovies = [“Saving Private Ryan”]
worldWarMoviesBadCopy = worldWarMovies
worldWarMoviesCopy = copy.copy(worldWarMovies)
# print out the list and see what it has. All should seem fine
# now, attempt to change both copied lists and see if that
# affects the original at all

worldWarMoviesBadCopy[0] = “Thin Red Line”
# does anything happen to the original list? It gets changed also,
# which is undesirable behaviour. Changing worldWarMoviesCopy
# wouldn’t affect the original list, so copy.copy is the way to go!

# Sorting Lists
# you can sort the list, but in different ways. One way will change the list
# forever and it won’t be the same anymore. The other way will create a
# new sorted list that is distinct from the original
moviesRating = [4.8, 4.5, 4.7, 4, 4.7]
sortedMoviesRating = sorted(moviesRating)

print(moviesRating)
print(sortedMoviesRating)

moviesRating.sort()

print(moviesRating)

# So all that's really cool to sort the list. What if we want to do more? Let's
# use a few basic concepts that we've covered so far to figure more things out

# the length of a list can be figured out by keeping a counter, and then 
# using a loop to go through each element in the list. For every element you 
# encounter, you add one to the counter. By the end of the loop, you have 
# figured out how many elements there are. Start by trying to write code for 
# this!

length = 0
for elem in moviesRating:
    length += 1
print(length)

# there are also built ins that can do this for you. 
print(len(moviesRating))

#how about if you want to find out the sum of all the elements in a list?

totalSum = 0
for elem in moviesRating:
    totalSum += elem
print(totalSum)
# now it's not too hard to find out the average, is it? 
# again, the built in for this previous function is sum(moviesRating)

average = totalSum / length
print(average)

# Now all that is well and good. What about figuring out the maximum or minimum
# of a list? There is a built in function that does it, min() and max(), but
# can you figure out how to do it yourself? 

lowestRating = min(moviesRating)
highestRating = max(moviesRating)

# I think it's time to start packaging the code we write into small, reusable 
# functions. Let's make the function that can figure out what the max is

def maxFinder(movieList):
    largestElement = 0
    for elem in movieList:
        if elem > largestElement:
            largestElement = elem
    return largestElement

largest = maxFinder(moviesRating)
print(largest)

# did you realize something about the above function though? It won't work if
# the numbers are negative. That's something to keep in mind!

# let's move on to some more meaningful functions. What if you want to find 
# how many movies are above a certain rating? We'll still have to loop across
# the entire list, but this time round, we'll compare if it's above the minimum
# that you have inputted, and if it is, it counts! Let's try writing this, 
# shouldn't be too tough

moviesRating = [4.8, 4.5, 4.8, 4.2, 4.5, 4.3, 3.8, 2.4, 4.2]

def howManyAboveThisRating(ratingList, minimumNumber):
    total = 0
    for rating in ratingList:
        if rating >= minimumNumber:
            total += 1
    return total

print(howManyAboveThisRating(moviesRating))

# how about let's make a function that changes the ratings from a 5 point
# scale to a 10 point one? What do you think that would look like?

def buggyDoubleEveryNumber(ratingList):
    for elem in ratingList:
        elem *= 2

# did that work? It's not going to work because the individual numbers in the 
# list are really not modifiable. You need to change the value in a different
# way:

def doubleEveryNumber(ratingList):
    for index in range(len(ratingList)):
        ratingList[index] *= 2

print(doubleEveryNumber(moviesRating))

# INSTRUCTOR NOTE: Please try to think about two more functions to practice/write
# which uses lists in a substantive way. Exec board, if you have ideas, please 
# put them down!

def randomFunction1():
    pass

def randomFunction2():
    pass


# Now let's consider that we want to store more information about the movies
# and we want to do it in this fashion, where the first thing is the name 
# of the movie, the second is the rating, and the third is your favourite 
# actor or actress from that film. We could store information about each of 
# them like this:

favMovie1 = ["Star Wars: The Force Awakens", 4.8, "Daisy Ridley"]
favMovie2 = ["The Great Gatsby", 4.5, "Leonardo DiCaprio"]
favMovie3 = ["The Dark Knight", 4.9, "Heath Ledger"]

# so now let's say you're trying to find the average of all the ratings.
# let's first put all the information that we have into a large, 2D list.

averageOfFavMovies = (favMovie1[1] + favMovie2[1] + favMovie3[1]) / 3

# clearly, if you have a gazillion such lists, you won't be very efficient with 
# it. What we can do, though, is make a list of all your favourite movies.

allMyFavMovies = [favMovie1, favMovie2, favMovie3]

# but wait. each of the fav movies are actually a list by themselves. So what we
# actually have is:

print(allMyFavMovies)

# now that we have something like this, let's see how to access the elements 
# inside of it. In order to the name of your third favourite movie, you'll do

print(allMyFavMovies[2][0])

# and to find out your favourite actor in the second movie, you'll do

print(allMyFavMovies[1][2])

# so now we are able to iterate this 2d list if we want to find the average of
# all the movie ratings that we have. We know it's gonna be pretty high since 
# we're just that awesome right?

total = 0
for favMovie in allMyFavMovies:
    total += favMovie[1]

print(total/len(allMyFavMovies))

# I guess that was better right? But doesn't it feel weird to have to access
# a certain random index? It's not clear that index 1 has the ratings. What if 
# the order changes? What if we add more elements? We should probably have a data
# structure that allows us to name what the item that we're storing is so that
# we don't struggle with remembering where it is and we can just access it with 
# something like this:

total = 0
for favMovie in allMyFavMovies:
    total += favMovie["rating"]

print(total/len(allMyFavMovies))

# the data structure that would allow for this is called a dictionary, and 
# you'll find out more in the next part of the lab!