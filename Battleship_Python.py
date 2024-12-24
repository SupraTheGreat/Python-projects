import random
from colorama import Fore

print(
  "Welcome to Battleship! In this game, you will try to guess the location of an enemy ship to drop a bomb on. After a certain number of incorrect attempts, the game will end."
)

battleshiphealth = 4
battleshipstartX = random.randint(0, 7)
battleshipstartY = random.randint(0, 7)

aircrafthealth = 5
aircraftstartX = random.randint(0, 7)
aircraftstartY = random.randint(0, 7)

subhealth = 3
substartX = random.randint(0, 7)
substartY = random.randint(0, 7)

cruiserhealth = 3
cruiserstartX = random.randint(0, 7)
cruiserstartY = random.randint(0, 7)

destroyerhealth = 2
destroyerstartX = random.randint(0, 7)
destroyerstartY = random.randint(0, 7)

turns = 0
a = 0
b = 0
c = 0
d = 0
s = 0
location = 0
sum = 0

grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

yourgrid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def printEnemyGrid():
  global grid
  print('\n\n')
  for i in range(8):
    print(f'{i+1} [', end='')
    for x in range(8):
      print(f"'{str(grid[i][x])}'", end='')
      print(', ', end='')
    print(']')
  print('    1    2    3    4    5    6    7    8')


def printYourGrid():
  global yourgrid
  print('\n\n')
  for i in range(8):
    print(f'{i+1} [', end='')
    for x in range(8):
      print(f"'{str(yourgrid[i][x])}'", end='')
      print(', ', end='')
    print(']')
  print('    1    2    3    4    5    6    7    8')


def battleshipstart():
  global battleshiphealth, battleshipstartX, battleshipstartY, grid
  grid[battleshipstartY][battleshipstartX] = 'B'
  for i in range(4):
    index = 0
    if i + 1 == 1:
      for i in range(battleshiphealth - 1):
        try:
          if grid[battleshipstartY][battleshipstartX + i + 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != 3:
        pass
      else:
        pass
        for x in range(3):
          grid[battleshipstartY][battleshipstartX + x + 1] = 'B'
        return
    elif i + 1 == 2:
      for i in range(battleshiphealth - 1):
        try:
          if grid[battleshipstartY + i + 1][battleshipstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != 3:
        pass
      else:
        pass
        for x in range(3):
          grid[battleshipstartY + x + 1][battleshipstartX] = 'B'
        return
    elif i + 1 == 3:
      for i in range(battleshiphealth - 1):
        try:
          if grid[battleshipstartY][battleshipstartX - i - 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != 3:
        pass
      else:
        pass
        for x in range(3):
          grid[battleshipstartY][battleshipstartX - x - 1] = 'B'
        return
    elif i + 1 == 4:
      for i in range(battleshiphealth - 1):
        try:
          if grid[battleshipstartY - i - 1][battleshipstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != 3:
        pass
      else:
        pass
        for x in range(3):
          grid[battleshipstartY - x - 1][battleshipstartX] = 'B'
        return


def aircraftstart():
  global aircrafthealth, aircraftstartX, aircraftstartY, grid
  remaining = aircrafthealth - 1
  while grid[aircraftstartY][aircraftstartX] != " ":
    aircraftstartX = random.randint(0, 7)
    aircraftstartY = random.randint(0, 7)

  grid[aircraftstartY][aircraftstartX] = 'A'
  for i in range(4):
    index = 0
    if i + 1 == 1:
      for i in range(remaining):
        try:
          if grid[aircraftstartY][aircraftstartX + i + 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[aircraftstartY][aircraftstartX + x + 1] = 'A'
        return
    elif i + 1 == 2:
      for i in range(remaining):
        try:
          if grid[aircraftstartY + i + 1][aircraftstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[aircraftstartY + x + 1][aircraftstartX] = 'A'
        return
    elif i + 1 == 3:
      for i in range(aircrafthealth - 1):
        try:
          if grid[aircraftstartY][aircraftstartX - i - 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[aircraftstartY][aircraftstartX - x - 1] = 'A'
        return
    elif i + 1 == 4:
      for i in range(aircrafthealth - 1):
        try:
          if grid[aircraftstartY - i - 1][aircraftstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[aircraftstartY - x - 1][aircraftstartX] = 'A'
        return


def substart():
  global subhealth, substartX, substartY, grid
  remaining = subhealth - 1
  while grid[substartY][substartX] != " ":
    substartX = random.randint(0, 7)
    substartY = random.randint(0, 7)

  grid[substartY][substartX] = 'S'
  for i in range(4):
    index = 0
    if i + 1 == 1:
      for i in range(remaining):
        try:
          if grid[substartY][substartX + i + 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[substartY][substartX + x + 1] = 'S'
        return
    elif i + 1 == 2:
      for i in range(remaining):
        try:
          if grid[substartY + i + 1][substartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[substartY + x + 1][substartX] = 'S'
        return
    elif i + 1 == 3:
      for i in range(subhealth - 1):
        try:
          if grid[substartY][substartX - i - 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[substartY][substartX - x - 1] = '2'
        return
    elif i + 1 == 4:
      for i in range(subhealth - 1):
        try:
          if grid[substartY - i - 1][substartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[substartY - x - 1][substartX] = 'S'
        return


def cruiserstart():
  global cruiserhealth, cruiserstartX, cruiserstartY, grid
  remaining = cruiserhealth - 1
  while grid[cruiserstartY][cruiserstartX] != " ":
    cruiserstartX = random.randint(0, 7)
    cruiserstartY = random.randint(0, 7)

  grid[cruiserstartY][cruiserstartX] = 'C'
  for i in range(4):
    index = 0
    if i + 1 == 1:
      for i in range(remaining):
        try:
          if grid[cruiserstartY][cruiserstartX + i + 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[cruiserstartY][cruiserstartX + x + 1] = 'C'
        return
    elif i + 1 == 2:
      for i in range(remaining):
        try:
          if grid[cruiserstartY + i + 1][cruiserstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[cruiserstartY + x + 1][cruiserstartX] = 'C'
        return
    elif i + 1 == 3:
      for i in range(cruiserhealth - 1):
        try:
          if grid[cruiserstartY][cruiserstartX - i - 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[cruiserstartY][cruiserstartX - x - 1] = 'C'
        return
    elif i + 1 == 4:
      for i in range(cruiserhealth - 1):
        try:
          if grid[cruiserstartY - i - 1][cruiserstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[cruiserstartY - x - 1][cruiserstartX] = 'C'
        return


def destroyerstart():
  global destroyerhealth, destroyerstartX, destroyerstartY, grid
  remaining = destroyerhealth - 1
  while grid[destroyerstartY][destroyerstartX] != " ":
    destroyerstartX = random.randint(0, 7)
    destroyerstartY = random.randint(0, 7)

  grid[destroyerstartY][destroyerstartX] = 'D'
  for i in range(4):
    index = 0
    if i + 1 == 1:
      for i in range(remaining):
        try:
          if grid[destroyerstartY][destroyerstartX + i + 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[destroyerstartY][destroyerstartX + x + 1] = 'D'
        return
    elif i + 1 == 2:
      for i in range(remaining):
        try:
          if grid[destroyerstartY + i + 1][destroyerstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[destroyerstartY + x + 1][destroyerstartX] = 'D'
        return
    elif i + 1 == 3:
      for i in range(destroyerhealth - 1):
        try:
          if grid[destroyerstartY][destroyerstartX - i - 1] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[destroyerstartY][destroyerstartX - x - 1] = 'D'
        return
    elif i + 1 == 4:
      for i in range(cruiserhealth - 1):
        try:
          if grid[destroyerstartY - i - 1][destroyerstartX] == ' ':
            index += 1
        except IndexError:
          pass
      if index != remaining:
        pass
      else:
        pass
        for x in range(remaining):
          grid[destroyerstartY - x - 1][destroyerstartX] = 'D'
        return


def positionShips():
  battleshipstart()
  aircraftstart()
  substart()
  cruiserstart()
  destroyerstart()
  printYourGrid()


positionShips()


def pick():
  global grid, yourgrid, turns, location
  X = int(input(Fore.WHITE + "\nEnter an x position to drop a bomb on. "))
  Y = int(input("Enter a y position to drop a bomb on. "))
  location = grid[Y - 1][X - 1]
  if location != ' ' and yourgrid[Y - 1][X - 1] == ' ':
    turns += 1
    print(f"\nIt's a hit! You have {30-turns} turns left.\n")
    hitc = Fore.RED + 'X' + Fore.WHITE
    yourgrid[Y - 1][X - 1] = hitc
    hit()
    printYourGrid()
    return
  elif yourgrid[Y - 1][X - 1] != ' ':
    print("\nYou already targeted that spot. Try again.\n")
    return
  else:
    turns += 1
    print(f"\nUnfortunately, you missed. You have {30-turns} turns left.\n")
    missc = Fore.BLUE + 'O' + Fore.WHITE
    yourgrid[Y - 1][X - 1] = missc
    printYourGrid()
    return


def hit():
  global yourgrid, grid, X, Y, location, a, b, c, d, s
  if location == 'A':
    a += 1
  elif location == 'B':
    b += 1
  elif location == 'C':
    c += 1
  elif location == 'D':
    d += 1
  elif location == 'S':
    s += 1


while turns < 31:
  # print(Fore.MAGENTA + str(sum))
  if a > 4:
    print('You sank the aircraft carrier!')
    sum += a
    a = 0
  elif b > 3:
    print('You sank the battleship!')
    sum += b
    b = 0
  elif c > 2:
    print('You sank the cruiser!')
    sum += c
    c = 0
  elif d > 1:
    print('You sank the destroyer!')
    sum += d
    d = 0
  elif s > 2:
    print('You sank the submarine!')
    sum += s
    s = 0
  if sum > 16:
    print('You sank every ship!')
    print(Fore.YELLOW + 'CONGRATULATIONS!')
    print(Fore.WHITE + 'Here is the grid of all the enemy ships:\n' + grid)
  # print(Fore.RED + str(a))
  # print(Fore.YELLOW + str(b))
  # print(Fore.GREEN + str(c))
  # print(Fore.BLUE + str(d))
  # print(Fore.MAGENTA + str(s))
  pick()
