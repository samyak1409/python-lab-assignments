# Write a program to compute distance between two points taking input from the user.


print('\n(give space separated values)')
x1, y1 = map(int, input('(x1, y1): ').split())
x2, y2 = map(int, input('(x2, y2): ').split())

print(f'\nDistance b/w points ({x1}, {y1}) and ({x2}, {y2}) is:', ((x2-x1)**2 + (y2-y1)**2) ** .5)
