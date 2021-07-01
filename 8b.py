# Write a program to compute the number of characters, words and lines in a file.


from sys import argv

with open(argv[0]) as f:
    lines = words = chars = 0
    for line in f.readlines():
        lines += 1
        words += len(line.split())
        chars += len(line)

print('\nLine count:', lines)
print('Word count:', words)
print('Char count:', chars-lines)
