'''Write a python program to input centimeter
 and convert to inch, meter and kilometer.'''

def kilonmeter(n):
  print("The value in meter is {}m".format(n/100))
  print("The value in kilometer is {}km".format(n/100000))


def inch(n):
  value = n / 2.54
  print("The value in inch is {}inch.".format(value))
  kilonmeter(n)

centi = float(input("Enter the input in centimeter:"))
inch(centi)

