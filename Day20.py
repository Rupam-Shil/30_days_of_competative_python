'''Find a square of number without using multiplication and division operator'''
def calcSquare(num):
  sum = 0
  for i in range(num):
    sum += num
  return sum

num = int(input("Please enter a no:"))
print("the square of {} is {}".format(num, calcSquare(num)))
