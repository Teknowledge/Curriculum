# "random" is a module that gives us cool extra functions
import random

def playDiceGame():
  print("Welcome to the dice game!")
  print("You have 3 rolls and 3 math operations to get exactly 3 points.")

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
  roll = random.randint(0,6)
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

  if score == 3:
    print("YOU WIN!!")
  else:
    print("You lose")

playDiceGame()

# Challenge 0: Change the "what does this do?" comments to explanations of
#    what the lines below them actually do.

# Challenge 1: This game is pretty hard. Change it to be easier by making
#    the goal to be 0 points and the dice roll always either 0, 1, or 2.

# Challenge 2: There is a bug (a coding problem)! What happens if you type
#    an invalid move? Fix the code so an invalid move does nothing.
#    Also add another print statement that says
#    "Or type something else to do nothing!"

# BONUS Challenge: Make the game better...use your own ideas or these ideas:
#    - add more rounds
#    - stop the game once you reach the goal score
#    - roll two dice each round and let the player pick which one to use
