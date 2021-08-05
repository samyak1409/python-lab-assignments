# Write a program to print each line of a file in reverse order.


from sys import argv

with open(argv[0]) as f:
    for line in f.readlines():
        print(line[::-1], end='')
print()
