# Dictionaries are very powerful tools to store all kinda of associations.
# For example, consider a website that stores movie data like IMDB.
# Each movie is assocaited with a year, a rating, multiple genres,
# a set of stars, and much more.  A dictionary would be a perfect way to
# store such data!

# The file imdb-database.py has a dictionary which contains the data for 15
# of IMDB's top 250 movies.  Copy and paste that below.

imdbData = {
    "Zootopia": {
        "Stars":["Ginnifer Goodwin", "Jason Bateman", "Idris Elba"],
        "Rating":8.1,
        "Genre":["Animation","Action","Adventure"],
        "Year":2016,
        "Link":"http://www.imdb.com/title/tt2948356/",
    },
    "Martian": {
        "Stars":["Matt Damon", "Jessica Chastain", "Kristen Wiig"],
        "Rating":8.0,
        "Genre":["Adventure","Drama","Sci-Fi"],
        "Year":2015,
        "Link":"http://www.imdb.com/title/tt3659388",
    },
    "Hotel Rwanda": {
        "Stars":["Don Cheadle", "Sophie Okonedo", "Joaquin Phoenix"],
        "Rating":8.1,
        "Genre":["Drama","History","War"],
        "Year":2004,
        "Link":"http://www.imdb.com/title/tt0395169",
    },
    "The Lord of the Rings: The Fellowship of the Ring": {
        "Stars":["Elijah Wood", "Ian McKellen", "Orlando Bloom"],
        "Rating":8.8,
        "Genre":["Action","Adventure","Drama"],
        "Year":2001,
        "Link":"http://www.imdb.com/title/tt0120737",
    },
    "The Godfather": {
        "Stars":["Marlon Brando", "Al Pacino", "James Caan"],
        "Rating":9.2,
        "Genre":["Crime","Drama"],
        "Year":1972,
        "Link":"http://www.imdb.com/title/tt0068646",
    },
    "Back to the Future": {
        "Stars":["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"],
        "Rating":8.5,
        "Genre":["Adventure","Comedy","Sci-Fi"],
        "Year":1985,
        "Link":"http://www.imdb.com/title/tt0088763",
    },
    "The Dark Knight": {
        "Stars":["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "Rating":9.0,
        "Genre":["Action","Crime","Drama"],
        "Year":2008,
        "Link":"http://www.imdb.com/title/tt0468569",
    },
    "A Beautiful Mind": {
        "Stars":["Russell Crowe", "Ed Harris", "Jennifer Connelly"],
        "Rating":8.2,
        "Genre":["Biography","Drama","Romance"],
        "Year":2001,
        "Link":"http://www.imdb.com/title/tt0268978",
    },
    "Toy Story 3": {
        "Stars":["Tom Hanks", "Tim Allen", "Joan Cusack"],
        "Rating":8.3,
        "Genre":["Animation","Adventure","Comedy"],
        "Year":2010,
        "Link":"http://www.imdb.com/title/tt0435761/",
    },
    "Forrest Gump": {
        "Stars":["Tom Hanks", "Robin Wright", "Gary Sinise"],
        "Rating":8.8,
        "Genre":["Comedy","Drama"],
        "Year":1994,
        "Link":"http://www.imdb.com/title/tt0109830",
    },
    "Inception": {
        "Stars":["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
        "Rating":8.8,
        "Genre":["Action","Adventure","Sci-Fi"],
        "Year":2010,
        "Link":"http://www.imdb.com/title/tt1375666",
    },
    "The Matrix": {
        "Stars":["Keanu Reeves", "Laurence Fishburne", "Carie-Anne Moss"],
        "Rating":8.7,
        "Genre":["Action","Sci-Fi"],
        "Year":1999,
        "Link":"http://www.imdb.com/title/tt0133093",
    },
    "Saving Private Ryan": {
        "Stars":["Tom Hanks", "Matt Damon", "Tom Sizemore"],
        "Rating":8.6,
        "Genre":["Action","Drama","War"],
        "Year":1998,
        "Link":"http://www.imdb.com/title/tt0120815",
    },
    "Spirited Away": {
        "Stars":["Daveigh Chase", "Suzanne Pleshette", "Miyu Irino"],
        "Rating":8.6,
        "Genre":["Animation","Adventure","Family"],
        "Year":2001,
        "Link":"http://www.imdb.com/title/tt0245429",
    },
    "Captain America: Civil War": {
        "Stars":["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],
        "Rating":8.1,
        "Genre":["Action","Adventure","Sci-Fi"],
        "Year":2016,
        "Link":"http://www.imdb.com/title/tt3498820",
    },
}

# There are multiple things we might want to do with a list of best movies.
# For example, let's say you only like a particular genre of movies.  Let's
# write a function that takes in a movieDatabase and a genre, and returns a
# list of the movies from the movieDatabase in that genre.

def moviesInGenre(movieDatabase, genre):
    returnList = []
    for name, data in movieDatabase.iteritems():
        for movieGenre in data["Genre"]:
            if movieGenre == genre:
                returnList.append(name)
                break
    return returnList

print("Drama Movies: ")
print(moviesInGenre(imdbData, "Drama"))
print("")

# Or perhaps we only want to find the movies with a certain rating.  Let's
# write a function that takes in a movieDatabase and a minRating, and returns a
# list of the movies from the movieDatabase with a higher rating.

def moviesWithRating(movieDatabase, minRating):
    returnList = []
    for name, data in movieDatabase.iteritems():
        if data["Rating"] > minRating:
            returnList.append(name)
    return returnList

print("Movies with > 8.5 rating: ")
print(moviesWithRating(imdbData, 8.5))
print("")

# What is instead of caring what actor were in a particular movie, we wanted to
# know what movies a specific actor was in?  Is there any way to flip the
# dictionary, so the key is the name of a star, and the value is a list of
# movies that star has been in?  Let's write a function to do that!

def getMoviesByMovieStar(movieDatabase):
    returnDict = dict()
    for name, data in movieDatabase.iteritems():
        for star in data["Stars"]:
            if star in returnDict:
                returnDict[star].append(name)
            else:
                returnDict[star] = [name]
    return returnDict

print("Movies that stars have been in: ")
print(getMoviesByMovieStar(imdbData))
print("")

# There are multiple ways to sort movies.  What are some examples of ways you
# might want to sort movies in?

# Let's write a function that does that! Recall that dictionaries are unordered,
# whereas lists are ordered.  Therefore, in the process of sorting the imdbData,
# we must convert it into a list

def sortByYear(movieDatabase):
    sortedData = []
    for i in range(len(movieDatabase)):
        maxYear = 0
        movieName = ""
        for name, data in movieDatabase.iteritems():
            if name not in sortedData:
                if data["Year"] > maxYear:
                    maxYear = data["Year"]
                    movieName = name
        sortedData.append(movieName)
    return sortedData

print("Best movies sorted by year: ")
print(sortByYear(imdbData))
print("")
