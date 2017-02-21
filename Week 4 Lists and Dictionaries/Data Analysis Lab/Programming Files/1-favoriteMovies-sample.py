
favMovies = ["Finding Dory", "Star Wars: The Force Awakens", "Frozen"]
print(favMovies)

print(favMovies[1])

# Challenge 0.0 - Change the last print to print "Finding Dory" using a
#    different index.

# Challenge 0.1 - 

print(favMovies[0:3])

favMovies.append("Zootopia")
print(favMovies)
favMovies.remove("Finding Dory")
print(favMovies)

favMovies.insert(0, "Jason Bourne")
print(favMovies)

favMovies.pop(2)
print(favMovies)

print("X-Men: Apocalypse" in favMovies)
print(list.index("X-Men: Apocalypse"))

# What if we wanted the user of the function to specify which movie s/he wants
# to find in the list?  How would we do that?
