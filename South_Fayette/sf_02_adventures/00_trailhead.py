
def startTrail():
  print("There are three trails to hike.")
  print("Type red, blue or green to choose your trail.")
  trail = input("> ")

  if trail == "red":
    result = redTrail()
  elif trail == "blue":
    result = blueTrail()
  else:
    result = greenTrail()

  print(result)
  print("The end.")

def redTrail():
  return "The red trail is adventurous."

startTrail()

# Challenge 0.0 - Define the greenTrail and blueTrail functions.
#    For each, return a string of your choice!

# Challenge 0.1 - Instead of using return in the functions, replace return with
#    print. What does result equal? Why is this?
#    (Hint: what is the function returning now?)

# Challenge 0.2 - Add back a return (on a new line) to each function, to return
#    the integer distance traveled in each trail:
#      5 for red, 2 for blue, 7 for green
#    Then before "The end.", print:
#    "You traveled 5 miles." (with the appropriate distance result!)

# BONUS CHALLENGE 0.3 - Make another function, chooseTrail, and move the
#    if-elif-else code there. Change startTrail to call chooseTrail three times
#    so you now hike three trails in a row. Then, still print:
#    "You traveled 14 miles." (you will need to add the results together!)
