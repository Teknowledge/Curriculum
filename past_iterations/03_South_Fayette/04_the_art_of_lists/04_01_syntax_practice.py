# For each of the challenges below, write your code from scratch!
#    Hint: The syntax guide will be helpful :)

# Comment out or delete your code after finishing each challenge.


# Here is a big list of names to have fun with!!
# from: http://deron.meranda.us/data/census-derived-all-first.txt
names = [
"Rosanna", "Kristofer", "Yesenia", "Lovie", "Reita", "Merrilee", "Glenna", "Liz",
"Wen", "Danille", "Josefine", "Senaida", "Susan", "Renda", "Particia", "Stephan",
"Stormy", "Shawana", "Trinh", "Venus", "Asley", "Stanford", "Joye", "Marcelene",
"Tanisha", "Earnest", "Noble", "Twanda", "Amparo", "Houston", "Dick", 
"Thomasena", "Latina", "Catherin", "Shana", "Fabian", "Johnna", "Francine", 
"Hollie", "Jamal", "Brigid", "Bell", "Merideth", "Cristy", "Ermelinda", "Rodger", 
"Darwin", "Barabara", "Edyth", "Elicia", "Bernarda", "Esperanza", "Angella", 
"Claris", "Gaston", "Evon", "Holley", "Carolin", "Cathern", "Wilton", 
"Ernestina", "Mariano", "Andreas", "Quincy", "Frederic", "Lyndsey", "Wynell", 
"Larisa", "Inger", "Hwa", "Malisa", "Olene", "Genevie", "Douglass", "Phuong", 
"Bobbye", "Azucena", "Ezequiel", "Anita", "Jaimee", "Fidel", "Glendora", 
"Marilyn", "Mirna", "Nada", "Columbus", "Arturo", "Ashleigh", "Lupita", "Cindie", 
"Mafalda", "Annette", "Spring", "Gustavo", "Abbey", "Garnet", "Londa", "Pedro", 
"Marybelle", "Lazaro", "Elmira", "Maricela", "Shawanna", "Bernard", "Sally", 
"Paola", "Margret", "Kallie", "Jolie", "Jeniffer", "Winona", "Ginger", "Jovan", 
"Cassaundra", "Janett", "Kory", "Dalila", "Rudolf", "Portia", "Tressie", "Keva", 
"Shelba", "Cristine", "Alena", "Nicolette", "Analisa", "Jonas", "Jolene", 
"Georgetta", "Lajuana", "Constance", "Hubert", "Ines", "Brady", "Weston", 
"Marlana", "Kenyetta", "Melaine", "Darcy", "Carlene", "Maryjane", "Margarito", 
"Thaddeus", "Charolette", "Kasha", "Joni", "Lavelle", "Gwenn", "Darlena", "Cory", 
"Rod", "Towanda", "Enid", "Bruce", "Landon", "Rubye", "Jaime", "Hisako", 
"Claude", "Leigha", "Arlyne", "Archie", "Ilene", "Hilton", "Michael", "Merle", 
"Christena", "Kathline", "Cletus", "Velma", "Martina", "Desmond", "Aisha", "Lea", 
"Leah", "Eugenie", "Flo", "Lashell", "Kanisha", "Cody", "Madie", "Barbar", 
"Alisia", "Katharyn", "Velva", "Weldon", "Tory", "Walter", "Kiera", "Denver", 
"Samatha", "Mignon", "Bradley", "Marie", "Ok", "Siobhan", "Eugene", "Raquel", 
"Tamie", "Kena", 
]

# Challenge 1.1 - Print all the names in the list.

# Solution:
# for name in names:
# 	print(name)

# Challenge 1.2 - Print all the names in the list, in reverse order.
#    Hint: Remember the for loop has three parameters!

# Solution:
# for i in range(len(names)-1, -1, -1):
# 	print(names[i])

# Challenge 1.3 - Make a new list of only the names that are three letters
#    long, then print that list.
#    Hint: You may want to start with only printing those names, then making
#      the list.

# Solution (add # to the beginning of the lines once you understand it):
threeLetterNames = []
for i in range(len(names)):
	name = names[i]
	nameLength = len(name)
	if (nameLength == 3):
		threeLetterNames.append(name)

print(threeLetterNames)

# Challenge 1.4 - Ask the user to input a capital letter (remember input()?),
#    then save the letter they input into a variable (say, firstLetterInput),
#    then make a new list of names (similar to the process above, with list
#    creation and then appending names within a loop) of only names that start
#    with that inputted letter (Hint: which index of a string has the first
#    letter?), and finally print that list.



# Challenge 1.5.1 - Make a function, firstAndLastList(a), that takes a list of
#    strings, a, and returns a new list that is tuples of the first and last
#    letter of each name in the list.
#    Example: If a is ["Rosanna", "Kristofer", "Yesenia" ... ]
#      the function returns the list [("R", "a"), ("K", "r"), ("Y", "a"), ...]

def firstAndLastList(a):
	pass # write your code here

# to test it we will call the function like so (delete # to run it):
# print(firstAndLastList(names))

# Challenge 1.5.2 - Make a similar function to the above, getNameInfo(a), that
#    returns a new list that for each name has (long!) tuples of:
#    - the index of the location of the name in the original list
#    - the name in the original list
#    - the first letter of the name
#    - the last letter of the name
#    - the length of the name
#    The correct result list will print like so for the sample list of names:
#      [(0, 'Rosanna', 'R', 'a', 7), (1, 'Kristofer', 'K', 'r', 9),
#       ... (199, 'Kena', 'K', 'a', 4)]



# BONUS Challenge 1.6 - Make a game that picks a random name (using
#    random.randint) then tells you the first letter, the last letter, and the
#    length of the name, then asks you to guess the name and tells you "Right!"
#    or "Wrong :(".
#    Hint: Put import random at the top of this file to use random.randint!
#    Hint: Use your Challenge 1.4 code (press undo if you deleted it).
#    Extra Challenge: Have the game keep playing until you get 5 names correct,
#      then say "You win! It took you _ names to get 5 correct."


