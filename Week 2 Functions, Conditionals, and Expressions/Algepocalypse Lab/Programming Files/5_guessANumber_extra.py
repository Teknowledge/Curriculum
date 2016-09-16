
from random import randint

correct = randint(1,10)

for i in range(5):
  guess = int(input("Guess the number: "))
  if (guess == correct):
    break
  else:
    print("Nope, guess again.")

if (guess == correct):
  print("You WIN")
else:
  print("sorry you lose, the number was " + str(correct))