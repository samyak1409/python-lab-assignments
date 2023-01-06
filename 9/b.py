"""
Write functions to compute gcd, lcm of two numbers. Each function shouldn't exceed one line.
"""


# GCD: https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm: TC = O(log(min(a, b))); SC = O(1)
# https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm
# https://www.baeldung.com/cs/euclid-time-complexity
"""
def gcd(a: int, b: int) -> int:
    if b == 0:  # base case
        return a  # ans.
    return gcd(b, a % b)  # recurse in
"""


# One-liner:
def gcd(a, b):
    return gcd(b, a % b) if b else a


# LCM: https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor:
# TC = O(log(min(a, b))); SC = O(1)
def lcm(a, b):
    return a * (b // gcd(a, b))  # or `b * (a // gcd(a, b))`


num1, num2 = int(input('\nnum1: ')), int(input('num2: '))
print('\nGCD:', gcd(num1, num2))
print('LCM:', lcm(num1, num2))
