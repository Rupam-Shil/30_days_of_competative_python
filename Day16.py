'''Write a program to get the sum of n numbers
Eg: Sum of 123 is 6
n is user entered value'''

print("Enter the no's:")
num = [int(i) for i in input().split()]
total = sum(num)
print(f"The total is {total}")
