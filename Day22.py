'''Write a python program to find if a given year is a leap year or not'''
def leapYear(y):
  if y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
      print("{} is not a leap year".format(y))
    
    

    else:
      print("{} is a leap year".format(y))
    
  else:
    print("{} is not a leap year".format(y))


year = int(input("Please enter the year:"))
leapYear(year)
