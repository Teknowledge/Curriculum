# Lists are great for ordering information, such as ranking your favorite
# movies.  But sometimes, you want to store additional information instead
# of just a rank.  For example, instead of providing a number, n, and getting
# your n-th favorite movie, what if wanted to provide a movie name and get the
# genre of the movie?  Dictionaries are used to do that, like so:
movieGenres = {"Finding Dory":"Animation", "Star Wars: The Force Awakens":"Action", "Frozen":"Adventure"}
print(movieGenres)

# The way you refer to elements in a dictionary is by their "key".  What the
# dictionary returns is called the "value".  In the above example, the keys
# are the names of movies, and the values are genres.

# Now, if we want to find the genre of a movie, we would do:
print(movieGenres["Frozen"])

# If the movie doesn't exist in the dictionary, it will return a KeyError:
print(movieGenres["La La Land"])

# Just like lists, you can add elements to a dictionary:
movieGenres["La La Land"] = "Romance"
print(movieGenres)

# You can also modify elements:
movieGenres["Finding Dory"] = "Family"
print(movieGenres)

# Or delete them:
del movieGenres["Frozen"]
print(movieGenres)

# Note that del is not a function, like print is.  In order words, it doesn't
# take it's arguments, or the values it acts on, within parenthesis.  Instead,
# it is a statement, like if, while, and def.

# You can get just the keys of a dictionary, or just the values:
print(movieGenres.keys())
print(movieGenres.values())

# Lastly, you can iterate over all the elements of a dictionary:
for movieName in movieGenres:
    print(movieName, "is in the genre", movieGenres[movieName], ".")

# Using these building blocks, we can write functions that get data from a
# dictionary.  Let's say you want to determine how many movies of a particular
# genre you have.

def numberOfMoviesFromGenres(movieDict, targetGenre):
    numInGenre = 0
    for genre in movieGenres.values():
        if genre == targetGenre:
            numInGenre += 1
    return numInGenre

movieGenres["Catching Fire"] = "Action"
movieGenres["Big Hero 6"] = "Animation"
movieGenres["Zootopia"] = "Animation"
movieGenres["Toy Story"] = "Animation"
movieGenres["Finding Dory"] = "Animation"
movieGenres["Fast and Furious"] = "Action"
movieGenres["Matrix"] = "Action"
movieGenres["Oceans 11"] = "Action"
movieGenres["The Avengers"] = "Action"
movieGenres["The Theory of Everything"] = "Romance"
movieGenres["Titanic"] = "Romance"
movieGenres["Notebook"] = "Romance"
print(movieGenres)
print("I have", numberOfMoviesFromGenres(movieGenres, "Action"), "Action films.")
print("I have", numberOfMoviesFromGenres(movieGenres, "Romance"), "Romance films.")
print("I have", numberOfMoviesFromGenres(movieGenres, "Adventure"), "Adventure films.")
print("I have", numberOfMoviesFromGenres(movieGenres, "Animation"), "Animation films.")
