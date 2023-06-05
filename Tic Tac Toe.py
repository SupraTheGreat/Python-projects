import random

row = 0
column = 0
symbols = 0
player1 = ""
player2 = ""
winner = ""
win = False
continued = True
grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
def intro():
  print("Welcome to Tic Tac Toe\n")
  print("In this 2 player game, you will enter coordinates that you want to place your X or O in.")
  print("Get three Xs or Os in a row, column, or diagonal line to win. Good luck!")
intro()


def decidePieces():
  global symbols, player1, player2
  symbols = random.randint(1, 2)
  if symbols == 1:
    player1 = "X"
    player2 = "O"
  elif symbols == 2:
    player1 = "O"
    player2 = "X"
  print(f"\nPlayer one is {player1}, and Player two is {player2}.")
decidePieces()

def playerOne():
  global grid, symbols, player1, player2
  turnOneX = int(input("\nPlayer 1, enter the row. 1 is the top row, 2 is the middle row, and three is the bottom row. "))
  turnOneY = int(input("\nNext, enter the column. 1 is the left column, 2 is the middle column, and three is the right column. "))
  if 'X' in grid[turnOneX-1][turnOneY-1] or 'O' in grid[turnOneX-1][turnOneY-1]:
    print(f"\n This is already occupied by a {grid[turnOneX-1][turnOneY-1]}. Enter different coordinates.")
    playerOne()
    return
  else:
    grid[turnOneX-1][turnOneY-1] = player1
  for i in range(3):
    print(grid[i])


def playerTwo():
  global grid, symbols, player1, player2
  turnTwoX = int(input("\nPlayer 2, enter the row. 1 is the top row, 2 is the middle row, and three is the bottom row. "))
  turnTwoY = int(input("\nNext enter the column. 1 is the left column, 2 is the middle column, and three is the right column. "))
  if 'X' in grid[turnTwoX-1][turnTwoY-1] or 'O' in grid[turnTwoX-1][turnTwoY-1]:
    print(f"\n This is already occupied by a {grid[turnTwoX-1][turnTwoY-1]}. Enter different coordinates.")
    playerTwo()
  else:
    grid[turnTwoX-1][turnTwoY-1] = player2
  for i in range(3):
    print(grid[i])

def horizontalCheck():
  global player1, player2, grid, winner, continued, win
  for i in range(3):
    if grid[i].count("X") == 3 or grid[i].count("O") == 3:
      winner = grid[i][1]
      if winner == "X" and "X" == player1:
        print("Player 1 WON!")
        continued = False
        win = True
        return
      else:
        print("Player 2 WON!")
        continued = False
        return

def verticalCheck():
  global player1, player2, grid, winner, continued, win
  for i in range(3):
    for x in range(3):
      if grid[i][x] != " ":
        if input == 0:  
          if grid[i][x] == grid[i+1][x] and grid[i][x] == grid[i+2][x] and grid[i+1][x] == grid[i+2][x]:
            if winner == "X" and "X" == player1:
              print("Player 1 WON!")
              continued = False
              win = True
              return
            else:
              print("Player 2 WON!")
              continued = False
              win = True
              return
        elif i == 1:
          if grid[i][x] == grid[i-1][x] and grid[i][x] == grid[i+1][x] and grid[i+1][x] == grid[i-1][x]:
            if winner == "X" and "X" == player1:
              print("Player 1 WON!")
              win = True
              continued = False
              return
            else:
              print("Player 2 WON")
              win = True
              continued = False
              return
        elif i == 2:
          if grid[i][x] == grid[i-1][x] and grid[i][x] == grid[i-2][x] and grid[i-1][x] == grid[i-2][x]:
            if winner == "X" and "X" == player1:
              print("Player 1 WON!")
              win = True
              continued = False
              return
            else:
              print("Player 2 WON!")
              win = True
              continued = False
              return

def diagonalCheck():
  global grid, player1, player2, winner, continued, win
  common = ""
  for i in range(4):
    if i < 2:
      common = player1
    else:
      common = player2
    if grid[1][1] == common:
      if (common == grid[2][2] and common == grid[0][0]) or (common == grid[0][2] and common == grid[2][0]):
          if winner == "X" and "X" == player1:
            print("Player 1 WON!")
            continued = False
            win = True
            return
          else:
            print("Player 2 WON!")
            continued = False
            win = True
            return
      else:
        return
    else:
      return

def turns():
  global grid, symbols, player1, player2, winner, continued, win
  while grid.count(" ") == 0:
    horizontalCheck()
    verticalCheck()
    diagonalCheck()
    index = 0
    for i in range(3):
      for x in range(3):
        if grid[i][x] != " ":
          index += 1
        else:
          pass
    if index == 9:
      print("\nLooks like none of you won! The game has resulted in a draw.")
      return
    if continued == True:
      playerOne()
    else:
      return
    horizontalCheck()
    verticalCheck()
    diagonalCheck()
    index = 0
    for i in range(3):
      for x in range(3):
        if grid[i][x] != " ":
          index += 1
        else:
          pass
    if index == 9 and win == False:
      print("\nLooks like none of you won! The game has resulted in a draw.")
      return
    if continued == True:
      playerTwo()
    else:
      return
    if index == 9 and win == False:
      print("\nLooks like none of you won! The game has resulted in a draw.")
      return
turns()