# You’ve got a list, and you want to do something useful on it. Let’s check out
# looping over them in two different ways.

favMovies = [...]
favMoviesRating = [...]
print("Here are my favourite movies:")
for movie in favMovies:
    print(movie)
# but with this you’re unable to figure out the rank of the movies
favMoviesRating = [...]
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
# new sorted list that is
