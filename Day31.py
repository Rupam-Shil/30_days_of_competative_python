'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

def FindPairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False        
A = [1, 4, 45, 6, 10, 8]
n = 100
print(FindPairs(A, n))
