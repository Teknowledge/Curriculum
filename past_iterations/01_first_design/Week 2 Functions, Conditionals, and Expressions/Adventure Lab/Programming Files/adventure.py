
def startGame():
  print("This is an adventure game.")
  input("Press enter to continue the text.")
  print("When you see this you will need to respond. Here type 'ok'. Then press enter.")
  input("> ")
  input("Ready? ...")
  startRoom()

def startRoom():
  input("You are in a big empty room.")
  input("There are four doors.")
  input("Which door do you enter?")
  print("Type 1, 2, 3, or 4 then press enter.")

  door = int(input("> "))

  if door == 1:
    input("It was a TRAP door.")
    gameOver()
  elif door == 2:
    input("You walk through door 2.")
    slide()    
  elif door == 3:
    input("You walk through door 3.")
    library()
  elif door == 4:
    input("Bottomless pit.  Sorry.")
    gameOver()
  else:
    input("that's not a door, try again.")
    print()
    startRoom()

def library():
  input("You are in a library.")
  input("The librarian glares at you.")
  input("'What is the password?' she asks.")
  print("What do you say?")

  password = input("> ")

  if password == "password":
    input("'How did you know?? Okay then...'")
    input("She pulls a book out of a shelf, then the shelf moves...")
    secretPassage()
  else:
    input("'Incorrect!!' she screams, then kicks you out.")
    startRoom()

def slide():
  input("WHEEEE")
  input("It is a slide.")
  input("You slide down for what seems like ages.")
  for i in range(10):
    input("and ages...")
  input("and reach the bottom!!!")
  input("but there are spikes")
  input("whoops")
  gameOver()

def secretPassage():
  input("You enter a secret passageway.")
  input("and there is cake!")
  win()

def win()
  input("You win!!")
  print("congrats :D")

def gameOver():
  print("Game Over!")

startGame()