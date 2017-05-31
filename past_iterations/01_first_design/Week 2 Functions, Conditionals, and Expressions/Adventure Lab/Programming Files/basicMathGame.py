
def playMathGame():
  print("Type the answer to 13+24 to hear a secret")

  answer = int(input("> "))

  if answer == 37:
    print("The secret is that with code you never have to do math again")
  else:
    print("Nope sorry, no secrets for you")

playMathGame()
print("Game Over!")