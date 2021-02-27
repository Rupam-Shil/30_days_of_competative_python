'''The temperature recorded at 8 A.M.
 is n deg Celcius. What is the equivalent
  of this temperature in degrees Fahrenheit?
n is user entered value.'''

def celToFaren(n):
  return ((n * 9 / 5) + 32)


degree_sign= u'\N{DEGREE SIGN}'

n = float(input(f"Enter the temp in Celcius({degree_sign}C): "))
print("The temp in Farenhite is {:.2f}{}F".format(celToFaren(n), degree_sign))
