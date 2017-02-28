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
#      a
#      len(a)
#      range(len(a))

# Challenge 0.2 - Add "Bruce" to the list in line 3. How do the prints change?

# Challenge 0.3 - After line 3, add "Nemo" to the list by this piece of code:
#      characters.append("Nemo")

# Challenge 0.4 - Write a new function makeListExciting(a) that takes in a list
#    of strings and returns a new list with the same strings but adding "!"
#    Example: If a is ["x", "y"],
#             makeListExciting(a) returns ["x!", "y!"]

# BONUS Challenge 0.5 - Write a function reverse(a) that returns a new list
#    with all the elements of the list a but in reverse order.
