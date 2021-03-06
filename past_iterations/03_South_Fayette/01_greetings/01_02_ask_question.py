
def askQuestion():
  print("What function displays text on the screen?")

  answer = input("Type here: ")

  if answer == "print":
    print("That's right, any string you put in print() will display!")
  else:
    print("Not correct, try looking at the code for help!")

print("Now I will ask you a question.")
askQuestion()
print("Question finished.")

# Challenge 2.1: Add a number to the beginning of each of the _five_ print()
#    function calls (starting with 1, ending with 4), indicating the order
#    that the print() calls happen. Check your answer by running the code!
# Hint: the last one will be: print("4 Question finished.")

# Challenge 2.2: Change the question to
#    "What function waits for the user to type something then press enter?"
#    and make the answer
#    "input"

# Challenge 2.3: Make a new function askAnotherQuestion(), with a question and
#    answer of your own choosing!  Call it after askQuestion.

# BONUS Challenge 2.4: Call askAnotherQuestion() only if the first question is
#    answered correctly.
