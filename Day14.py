'''
How many ways can four students Ram, Anuj, Deepak and Ravi line up in
a line, if the order matters?
Print all the possible Combination.'''

from itertools import permutations

studentsName = ['Ram', 'Anuj', 'Deepak', 'Ravi']
finalList = permutations(studentsName)
for i in finalList:
  print(list(i))
