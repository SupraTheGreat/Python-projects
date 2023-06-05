from datetime import datetime

givendate = input("Enter a month and year in the format: mm/yyyy. ")

currentdate = datetime.now()
monthlist = []
yearlist = []
month = ""
year = ""
listofdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def extract():
  global monthlist, yearlist, month, year, givendate
  for i in range(2):
    monthlist.append(givendate[i])
    givendate = givendate.replace(givendate[i], "-", 1)
  for x in range(4):
    yearlist.append(givendate[x+3])
    givendate = givendate.replace(givendate[x+3], "-", 1)
extract()

def variablize():
  global monthlist, yearlist, month, year
  for x in range(len(yearlist)):
    year += yearlist[x]
  for r in range(len(monthlist)):
    month += monthlist[r]
variablize()

day = 0
for i in range(7):
  weekday = datetime(int(year), int(month), i+1, 00, 00, 00)
  if listofdays[weekday.weekday()] == "Friday":
    day = i+1
    break
if day == '' or day == ' ':
  day = 0
else:
  day = int(day)
day += 21

date = ""
date += ""
date += str(day)
date += "/"
date += str(month)
date += "/"
date += str(year)

print(f"\nThe 4th friday of this month is {date}.")