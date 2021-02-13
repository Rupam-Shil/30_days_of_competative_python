'''  
On a Certain day, the nurses at a hospital worked the following number of hours:
Nurse Howard worked 8 hours
Nurse Pease worked 10 hours
Nurse Campbell worked 9 hours
Nurse Grace worked 8 hours
Nurse McCarthy worked 7 hours
and Nurse Murphy worked 12 hours.
What is the average number of hours worked per nurse on this day?
Average should be a float value
'''
nurseWorked = [8, 10, 9, 8, 7, 12]
avgWorked = float(sum(nurseWorked) / len(nurseWorked))
print("The avg work is {:.2f}".format(avgWorked))
