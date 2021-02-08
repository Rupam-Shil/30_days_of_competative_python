"""
Print Multiplication table
"""

number = int(input("Enter the no:"))
def mul_table(no):
  for i in range(1,11):
    print("{} * {} = {}".format(no, i,(no*i)))


mul_table(number)
