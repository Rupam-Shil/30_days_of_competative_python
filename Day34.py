'''Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.'''



def checkOut(a):
    a.sort()
    for i in a:
        if i < 0:
            a.remove(i)
    if len(a) == 1:
        print(a[0]+1)
    elif len(a) == 0:
        print(1)
    else:
        for i in range(len(a) - 1):
            if a[i] + 1 != a[i + 1]:
                print(a[i] + 1)
                break
            elif a[i + 1] == a[-1]:
                print(a[-1] + 1)
                break

a = [3, 4, -1, 1]
checkOut(a)
