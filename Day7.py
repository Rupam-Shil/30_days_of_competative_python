'''  
The city's bus system carries 1200000 people each day.
How many people does the bus system carry each year?
Solve without using *, / operator, bitwise or loop
'''
def Calc(day, peoplesPerDay):
    if day == 0:
        return 0
    elif day > 0:
        return peoplesPerDay + Calc(day-1, peoplesPerDay)
    else:
        return 0


peoplesPerDay = 1200000
days = 365
print(sum(days, peoplesPerDay))
