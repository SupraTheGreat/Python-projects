year = int(input("Enter a random year, and this function will detect if that year is a leap year or not."))

def calculate():
  if (year%4) == 0:
    print("It's a leap year!")
  else:
    print("It's not a leap year.")
calculate()