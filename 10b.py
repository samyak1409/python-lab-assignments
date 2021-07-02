# Write a program to implement selection sort.


# https://youtu.be/xWBP4lzkoyM

from random import randint

n = int(input('\nArray Size: '))
l = [randint(1, n) for _ in range(n)]
print('Unsorted:', l)

len_ = len(l)
for i in range(len_):
    for j in range(i+1, len_):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print('Sorted:', l)
