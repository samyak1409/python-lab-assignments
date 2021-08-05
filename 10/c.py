# Write a program to implement insertion sort.


# https://youtu.be/OGzPmgsI-pQ

from random import randint

n = int(input('\nArray Size: '))
l = [randint(1, n) for _ in range(n)]
print('Unsorted:', l)

for i in range(len(l)):
    x = l[i]
    for j in range(i-1, -1, -1):
        y = l[j]
        # print(x, y)  #debugging
        if x < y:
            l[i], l[j] = y, x
            i -= 1
            # print(l)  #debugging
        else:
            # print('breaking')  #debugging
            break
    # print()  #debugging
print('Sorted:', l)
