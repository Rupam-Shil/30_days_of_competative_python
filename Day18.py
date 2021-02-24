'''
Lefty keeps track of the length of eac fish that he catches
Below are the lengths in inches of the fish that he caught one day:
12, 13, 8, 10, 17
What is the largest fish length that lefty caught that day?
Solve without using conditional statements and the loop.
'''

fishSize = [12, 13, 8, 10, 17]

fishSize.sort()

print("The largest fish that Lefty caught is {}".format(fishSize[-1]))
