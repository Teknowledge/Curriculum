# three is company! ^_^  ^_^  ^_^

import copy

emptyBoard = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]]

def printBoard(board):
  stringToPrint = "Column 0 1 2 \n"
  i = 0
  for row in board:
    stringToPrint += "Row " + str(i) + "  "
    for spaceStr in row:
      stringToPrint += spaceStr
      stringToPrint += " "
    stringToPrint += "\n"
    i += 1
  print(stringToPrint)

def playGame():
  board = copy.deepcopy(emptyBoard)
  printBoard(board)

  print("Welcome to Tic-Tac-Toe!")

  print("You are X, Computer is O")

  moves = 0

  while moves <= 9:
    board = makePlayerMove(board)
    moves = moves + 1

    # write code here!

def makePlayerMove(board):
  row = int(input("Your row selection: "))
  col = int(input("Your column selection: "))

  # write code here!

  return board

def checkBoardForWin(board):
  def movesSum(moves):
    return moves[0] + moves[1] + moves[2]

  # check rows
  for row in board:
    if movesSum(row) == "XXX":
      return "X"
    elif movesSum(row) == "OOO":
      return "O"

  # check cols
  for col in range(len(board[0])):
    colList = []
    for row in range(len(board)):
      colList.append(board[row][col])
    if movesSum(colList) == "XXX":
      return "X"
    elif movesSum(colList) == "OOO":
      return "O"

  # check diagonals
  diag1 = []
  diag2 = []
  for position in [[0, 0], [1, 1], [2, 2]]:
    playerToken = board[position[0]][position[1]]
    diag1.append(playerToken)
  for position in [[0, 2], [1, 1], [2, 0]]:
    playerToken = board[position[0]][position[1]]
    diag2.append(playerToken)
  if movesSum(diag1) == "XXX" or movesSum(diag2) == "XXX":
    return "X"
  elif movesSum(diag1) == "OOO" or movesSum(diag2) == "OOO":
    return "O"

  return ""

playGame()

# Challenge 0 - Finish the function makePlayerMove(board), so you can take the
#    row and col input and update the board with an "X". Then, after your move,
#    print the board using the given printBoard(board) function.
#    (Assume the player's move is always a valid move.)

# Challenge 1 - Add a new function, makePlayer2Move(board), that does the same
#    thing as makePlayerMove(board) but places an "O".

# Challenge 2 - Use the given function, checkBoardForWin(board), that returns:
#      "X" if player 1 has three in a row
#      "O" if player 2 has three in a row
#      "" otherwise
#    And call it to find out if a player wins, and stop the loop if so.
#    Hint: to stop the loop, just have the Python keyword:
#      break
#    on its own line (you probably want this inside an if statement).
#    Then, after the loop, print which player won!

# Challenge 3 - Change makePlayer2Move(board) to makeComputerMove(board), that
#    adds a "O" to the first open space on the board, starting from the top
#    left, going left to right down the board.

# BONUS Challenge - The computer is too predictable - give it upgrades by:
#      - making the computer move to a random available space
#      - if the player has two in a row, the computer should block the player
#        from winning by making the move that keeps the player from winning
