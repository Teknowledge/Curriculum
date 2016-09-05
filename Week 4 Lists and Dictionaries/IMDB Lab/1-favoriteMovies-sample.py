# Lists are ways of collecting information together.  For example, let's say
# we want to store a list of your favorite movies.  We would do:
favMovies = ["Finding Dory", "Star Wars: The Force Awakens", "Frozen"]
print(favMovies)

# Why would we want to do that?  Well, lists have a lot of useful properties.
# For example, it can store any amount of data.  It also stores the order of
# that data.  Let's say your friend gave you a list of
# his favorite movies in order.  If you want to know his/her third favorite
# movie, you would do:
print(favMovies[2]) # Note that numbers in a computer start from 0, so the
                    # third favorite movie is actually the movie at
                    # index 2 (i.e. 0, 1, 2).

# You can also access parts of a list, called slices. Let's say you want to
# know your friend's top 3 favorite movies.  You want the elements of the
# favorite  movies list at index 0, 1, and 2 (remember, counting starts
# at 0).  You would do:
print(favMovies[0:3])
# The reason you do 0:3 is because Python includes element at the starting
# index, but not at the ending index.  Therefore, 0:3 will give you elements
# 0, 1, and 2.

# You can also add files to a list and remove files from a list easily,
# while still using the same variable name to access it.  For example:
favMovies.append("Zootopia")
print(favMovies)
favMovies.remove("Finding Dory")
print(favMovies)

# Since lists keep track of order, you can also add and remove elements by
# their index in the list.  For example, let's say you watched Jason Bourne,
# and loved it so much that it become your #1 movie (note the first element is
# in index 0).  You would do:
favMovies.insert(0, "Jason Bourne")
print(favMovies)
# Similarly, let's say you watched your third favorite movie again and realized
# you hate it.  You would do:
favMovies.pop(2)
print(favMovies)

# You can also look to find certain elements in a list.  Let’s say your friend
# gave her favorite movies list, and you want to determine if
# “X-Men: Apocalypse” is in it.
print(“X-Men: Apocalypse” in favMovies)
# You can also determine where in the list a particular movie is with:
print(list.index(“X-Men: Apocalypse”))
# This, however, crashes, because X-Men Apocalypse is not in the list.
# Therefore, to safely determine if a movie is in the favorite movies list,
# we have to use a combination of in and index.  Let’s write a function that
# does exactly that: given a list of favorite movies, determines if a
# particular movie is in it.

# What if we wanted the user of the function to specify which movie s/he wants
# to find in the list?  How would we do that?
