'''Write a python program that accepts
 two integers from the user and then print
the sum, the difference , the product, 
the average, the maximum(the lerger of two integers)
 the minimum(the smaller of two integers).'''

 num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
my_sum = num1 + num2
# Remove abs() if you want to print exact difference of first num - second num
my_diff = abs(num1 - num2)
my_prod = num1 * num2
my_av = my_sum / 2
min_num = min(num1, num2)
max_num = max(num1, num2)

print(f"Sum: {my_sum}")
print(f"Difference: {my_diff}")
print(f"Product: {my_prod}")
print(f"Average: {my_av}")
print(f"Minumin: {min_num}")
print(f"Maximum: {max_num}")
