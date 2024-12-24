import random
import colorama
from colorama import Fore

print("Welcome to Number Wordle, which is a version of Wordle, but with numbers!\n")



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

number = ""
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
variable = ""
correct = False
numofyellows = []
yellow = True
yellowindex = -1

for i in range(4):
  variable = numbers[random.randint(0, 9-i)]
  number += variable
  numbers.remove(variable)

# def check():
#   global yellow, yellowindex, guess
#   yellowindex = -1
#   if numofyellows.count(guess[x]) > 1:
#     for a in range(len(numofyellows)):
#       if numofyellows.count(numofyellows[yellowindex]) > 1 and len(numofyellows) > 0:
#         yellow = False
#         yellowindex += 1
#       else:
#         yellowindex += 1
#         # print(Fore.MAGENTA + str(yellowindex))
#         print(Fore.RED + str(numofyellows.count(numofyellows[yellowindex])))
#         # print(Fore.BLUE + numofyellows[yellowindex])
#         yellow = True
#   else:
#     pass

def calculate():
  global number, correct, yellow, yellowindex
  guess = []
  go = False
  numofyellows = []
  ogguess = input(Fore.WHITE + "\nEnter a random FOUR digit number as your guess. ")
  for i in range(4):
    guess.append(ogguess[i])
  for x in range(4):
    for z in range(4):
      if guess[z] == number[z]:
        numofyellows.append(guess[z])
        # print(Fore.RED + "test")
    if guess[x] == number[x]:
      print(color.BOLD + Fore.GREEN + guess[x], end="" + color.END)
    else:
      index = -1
      for r in range(4):
        
        yellowindex = -1
        if numofyellows.count(guess[x]) > 1:
          for a in range(len(numofyellows)):
            if numofyellows.count(numofyellows[yellowindex]) > 1 and len(numofyellows) > 0:
              yellow = False
              yellowindex += 1
            else:
              yellowindex += 1
              # print(Fore.MAGENTA + str(yellowindex))
              # print(Fore.RED + str(numofyellows.count(numofyellows[yellowindex])))
              # print(Fore.BLUE + numofyellows[yellowindex])
              yellow = True
        else:
          pass
        # print(Fore.RED + number[index])
        index += 1
        # print(Fore.MAGENTA + guess[x])
        # print(Fore.GREEN + number[index])
        if guess[x] == number[index] and yellow == True:
          # print(yellow)
          # HHHHHHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRREEEEEEEEEEEEEE
          numofyellows.append("_")
          if numofyellows.count(numofyellows[yellowindex]) > 1:
            yellow = False
          else:
            yellow = True
          numofyellows.append(guess[x])
          # print(Fore.CYAN + "test")
          if numofyellows.count(numofyellows[yellowindex]) > 1:
            yellow = False
          else:
            yellow = True
          if yellow == True:
            print(color.BOLD + Fore.YELLOW + guess[x], end="" + color.END)
            go = True
            break
        else:
          go = False
        
      if number[x] != guess[x] and go == False:
        print(color.BOLD + Fore.WHITE + guess[x], end="" + color.END)
    # print(numofyellows)
    # print(Fore.BLUE + str(yellow))
  if ogguess == number:
    print(color.BOLD + Fore.GREEN + "\nYou guessed it!" + color.END)
    correct = True
    

for y in range(5):
  if correct == True:
    break
  else:
    calculate()

if correct == False:
  print(color.BOLD + Fore.RED + f"\n\nUnfortunately, you weren't able to guess it. The answer was {number}." + color.END)
