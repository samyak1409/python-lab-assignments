# Write a program to count frequency of characters in a given file.


from sys import argv
from pprint import pprint

file = argv[0]
with open(file) as f:
    chars = f.read()

frequency = {}
for char in chars:
    frequency[char] = frequency.get(char, 0) + 1
print(f'\nCharacter frequency in file {file}: \n')
pprint(frequency)
