# Write a program to count the numbers of characters in the string and store them in a dictionary data structure.


from pprint import pprint

string = 'High-level programming language'
print(f'\nString: "{string}" \n')
mapping = {}
for c in string:
    mapping[c] = mapping.get(c, 0) + 1
pprint(mapping)
