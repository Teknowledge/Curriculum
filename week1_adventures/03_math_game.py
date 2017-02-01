
def playMathGame():
  print("Welcome to the math game!")
  input("Press enter to continue.")
  question1()

def question1():
  print("Type the answer to 13+24 to hear a secret")
  addAnswer = int(input("> "))

  # response 1
  if addAnswer == 37:
    print("The secret is that with code you never have to do math again")
    question2()
  else:
    print("Nope sorry, no secrets for you")
    gameOver()

def question2():
  print("What function displays text on the screen?")
  printAnswer = input("> ")

  # response 2
  if printAnswer == "print":
    print("Right - print does!")
    winGame()
  else:
    print("No - that's not right.")
    gameOver()

def winGame():
  # win response
  print("Wahoo you got all questions right!")

def gameOver():
  print("Game Over!")

playMathGame()
