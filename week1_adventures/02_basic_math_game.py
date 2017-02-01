
def playMathGame():
  print("Type the answer to 13 + 24 to hear a secret")

  answer = int(input("> "))

  if answer == 13 + 24:
    print("The secret is that with code you never have to do math again")
  else:
    print("Nope sorry, no secrets for you")

print("Starting game...")
playMathGame()
print("Game Over!")