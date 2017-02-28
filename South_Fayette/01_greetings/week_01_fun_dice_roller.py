# ^_^ WEEK 01 FUN ^_^
# TAKE-HOME CHALLENGE
import random

# this function gives you a random number from 1 to 6 (different each time)
def getDieRoll():
  return random.randint(1,6)

print("Press enter to roll one die.")

roll = getDieRoll()

print("You rolled:", roll)

print("What number do you add to this roll to get 10?")
guess = int(input("Type here: "))

answer = 10 - guess

if (guess == answer):
  print("Right! You win!")
else:
  print("Wrong, you lose.")

# Challenge 1: Change the first statement "Press enter to roll one die." so
#    that you have to actually press enter first.
# Hint: What function makes the user input something? :)

# Challenge 2: If you play the game a few times you will realize the answer
#    is not being checked correctly. Change the code so it is right.
# Hint: Change line number 17 to include the variable 'roll' somehow.

# Challenge 3: After the first roll, ask the player
#    "Do you want to re-roll? "
#     And if they type "yes", then get a new die roll and print it like
#       New roll: 5
#     Otherwise, keep the old die roll and don't print anything.

# BONUS Challenge 4: Change the program to roll two dice (with an option for
#    re-rolling) and ask you
#    "What number do you add to the combined roll to get 20?"
#    and change the code accordingly to check the guess against adding to 20.
