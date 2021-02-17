'''The number of red blood corpuscles in one
the cubic milimeter is about 5,000,000 and the
number of white blood corpuscles in one cubic
the milimetre is about 8,000. What, then, is the ratio
of white blood corpuscles to red blood corpuscles?
Aspect Ratio should be as an int value?'''

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b%a, a)    

redBloodCorpuscles = 5000000
whitebloodCorpuscles = 8000
rationDiv = gcd(redBloodCorpuscles, whitebloodCorpuscles)
print("The ratio is {}/{}".format(int(redBloodCorpuscles/rationDiv) ,int(whitebloodCorpuscles/rationDiv)))
