# Q1(CO1) Create a program that asks the user for a number and then prints out a list of all the divisors of that
# number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For
# example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# code
n = int(input('Q1) > '))
print([i for i in range(1, n+1) if n % i == 0])

# output
'''
Q1) > 10
[1, 2, 5, 10]
'''


# Q2(CO2) Write a program (function!) that takes a list and returns a new list that contains all the elements of the
# first list minus all the duplicates.

# code
def unique(list_): return list(set(list_))


print(unique(map(int, input('\nQ2) (space separated) > ').split())))

# output
'''
Q2) (space separated) > 0 1 1 2 3
[0, 1, 2, 3]
'''
