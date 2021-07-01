# Write functions to compute gcd, lcm of two numbers. Each function shouldn't exceed one line.


def gcd(x, y): return gcd(y, x % y) if y else x


def lcm(x, y): return (x * y) // gcd(x, y)


num1, num2 = int(input('\nnum1: ')), int(input('num2: '))
print('\nGCD:', gcd(num1, num2))
print('LCM:', lcm(num1, num2))
