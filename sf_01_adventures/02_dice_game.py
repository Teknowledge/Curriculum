# "random" is a module that gives us cool extra functions
import random

# NOTE: run this file and play the game before you read the code!

def playDiceGame():
  print("Welcome to the dice game!")
  print("You have 3 rolls and 3 math operations to get exactly 5 points.")

  originalScore = 0
  scoreRound1 = playRound(originalScore)
  scoreRound2 = playRound(scoreRound1)
  finalScore = playRound(scoreRound2)
  checkWin(finalScore)

def playRound(score):
  # what does this do?
  print()
  print("Score:", score)

  # what does this do?
  roll = random.randint(1,6)
  print("Your roll:", roll)

  print("For your move, type + or - or *")
  move = input("Type here: ")

  if (move == "+"):
    score = score + roll
  # elif means "else if"
  elif (move == "-"):
    score = score - roll
  else:
    score = score * roll

  # what does this do?
  return score

def checkWin(score):
  print("Final score", score)

  if score == 5:
    print("YOU WIN!!")
  else:
    print("You lose")

playDiceGame()

# Challenge 0: Change the "what does this do?" comments to explanations of
#    what the lines below them actually do.

# Challenge 1: This game is pretty hard. Change it to be easier by making
#    the goal to be 1 point and the dice roll always either 1 or 2.

# Challenge 2: There is a bug (a coding problem)! What happens if you type
#    an invalid move? Fix the code so an invalid move does nothing.
#    Also add another print statement that says
#    "Or type something else to do nothing!" (after "For your move...")

# BONUS Challenge: Make the game better...use your own ideas or these ideas:
#    - add more rounds (for example: 5 instead of 3)
#    - have multiple goal scores (for example: 7, 9, and 11, any one wins)
#        and change the dice roll back to 1-6
#    - stop the game once you reach the goal score
#    - roll two dice each round and let the player pick which one to use
