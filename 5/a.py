"""
Write a program to find the sum of all the primes below 2 million.
"""


# https://www.geeksforgeeks.org/program-to-print-first-n-prime-numbers
# https://www.geeksforgeeks.org/print-all-prime-numbers-less-than-or-equal-to-n


n = 2_000_000


"""
# Brute-force:
# TC = O(n * √n) = O(n^(3/2)); SC = O(1)

sum_ = 0
for i in range(2, n+1):
    for j in range(2, int(i**.5)+1):
        if i % j == 0:
            break
    else:
        sum_ += i
print('\nSum of all the primes below 2 million:', sum_)
"""


# Optimal:
# Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes):
# TC = O(n*log(log(n))); SC = O(n)
# https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn

is_prime = [i > 1 for i in range(n+1)]  # [False, False, True, ... True]
# print(is_prime)  #debugging
for num in range(2, int(n**.5)+1):  # [2, √n]
    if is_prime[num]:
        for multiple in range(num*num, n+1, num):
            is_prime[multiple] = False
# print(is_prime)  #debugging

print('\nSum of all the primes below 2 million:', sum(num for num, prime in enumerate(is_prime) if prime))
