import random
import colorama
from colorama import Fore

print("Welcome to Wordle!\n")

myWords = []
with open("words.txt", "r") as inF:
    for line in inF:
        line = line.strip()
        if line == "": continue
        myWords.append(line)
        myWordsOf5Chars = list(filter(lambda x : len(x) == 5, myWords))
        from random import choice
word = choice(myWordsOf5Chars)
# print("\n" + word + "\n")

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

variable = ""
correct = False
numofyellows = []
yellow = True
yellowindex = -1

ogalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetG = []
alphabetY = []
alphabetW = []

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
  global word, correct, yellow, yellowindex, myWordsOf5Chars, alphabet, alphabetG, alphabetY, alphabetW, ogalphabet
  guess = []
  go = False
  numofyellows = []
  ogguess = input(Fore.WHITE + "\nEnter a random FIVE letter word as your guess. ")
  if ogguess in myWordsOf5Chars:
    pass
    isaword = True
  else:
    print("Remember, your guess has to be a REAL word, and a 5 letter one.")
    calculate()
    return
  for i in range(5):
    guess.append(ogguess[i])
  for x in range(5):
    for z in range(5):
      if guess[z] == word[z]:
        numofyellows.append(guess[z])
        alphabetG.append(guess[z])
        if guess[z] in alphabetY:
          alphabetY.remove(guess[z])
        # print(Fore.RED + "test")
    if guess[x] == word[x]:
      print(color.BOLD + Fore.GREEN + guess[x], end="" + color.END)
    else:
      index = -1
      for r in range(5):
        
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
        if guess[x] == word[index] and yellow == True:
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
            alphabetY.append(guess[x])
            print(color.BOLD + Fore.YELLOW + guess[x], end="" + color.END)
            go = True
            break
        else:
          go = False
        
      if word[x] != guess[x] and go == False:
        print(color.BOLD + Fore.WHITE + guess[x], end="" + color.END)
        alphabetW.append(guess[x])
    # print(numofyellows)
    # print(Fore.BLUE + str(yellow))
  if ogguess == word:
    print(color.BOLD + Fore.GREEN + "\nYou guessed it!" + color.END)
    correct = True
  for g in range(len(alphabet)):
    if alphabetG.count(alphabet[g]) > 0 or alphabetY.count(alphabet[g]) > 0 or alphabetW.count(alphabet[g]) > 0:
      alphabet[g] = "_"
    else:
      pass
  print("\n")
  if correct != True:
    for n in range(len(ogalphabet)):
      if ogalphabet[n] in alphabet:
        print(Fore.WHITE + ogalphabet[n].upper(), end="")
        print(" ", end="")
      elif ogalphabet[n] in alphabetG:
        print(Fore.GREEN + ogalphabet[n].upper(), end="")
        print(" ", end="")
      elif ogalphabet[n] in alphabetY:
        print(Fore.YELLOW + ogalphabet[n].upper(), end="")
        print(" ", end="")
      elif ogalphabet[n] in alphabetW:
        print(Fore.RED + ogalphabet[n].upper(), end="")
        print(" ", end="")
    print("\n")

for y in range(6):
  if correct == True:
    break
  else:
    calculate()

if correct == False:
  print(color.BOLD + Fore.RED + f"\n\nUnfortunately, you weren't able to guess it. The answer was {word}." + color.END)
