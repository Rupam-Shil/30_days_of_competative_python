'''There are 10 students in a class some students name are same to other students.
Print the names that occur more than one time. All names should be in a single string
Eg. str = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar'''

str = input("Enter the name of 10 students separated with space: ")
arr = str.split(' ')
my_len = len(arr)

duplicate = ''
for i in range(my_len):
    for j in range(i+1, my_len):
        if arr[i] == arr[j]:
            duplicate += f"{arr[i]} "

print(duplicate)
