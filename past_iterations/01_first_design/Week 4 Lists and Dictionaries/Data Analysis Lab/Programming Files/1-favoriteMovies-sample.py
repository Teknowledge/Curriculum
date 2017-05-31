# a few of my favorite things...

characters = ["Dory", "Marlin", "Bubbles"]
print("characters list:", characters)

print("index 1:", characters[1])

def printListElements(a):
  for i in range(len(a)):
    print()
    print("i:", i)
    print("a[i]", a[i])

printListElements(characters)

# Challenge 0.0 - Add two more print lines like the second one above, but for:
#      "index 2:"
#      "index 0:"

# Challenge 0.1 - What is the loop doing? Before the loop, print these things:
#      len(a)
#      range(len(a))

# Challenge 0.2 - Add "Bruce" to the list in line 3. How do the prints change?

# Challenge 0.2 - After line 3, add "Nemo" to the list by this piece of code:
#      characters.append("Nemo")

# What if we wanted the user of the function to specify which movie s/he wants
# to find in the list?  How would we do that?
