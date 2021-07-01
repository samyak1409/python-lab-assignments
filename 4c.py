# Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero.


num = int(input('\nCountdown to 0 from: '))
print()
while num >= 0:
    print(num)
    num -= 1
