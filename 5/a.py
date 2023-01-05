# Write a program to find the sum of all the primes below 2 million.


n = 2_000_000


"""
# Brute-force:

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

is_prime = [i > 1 for i in range(n+1)]  # [0, 1, 2 ... n]
for num in range(2, int(n**.5)+1):  # [2, √n]
    if is_prime[num]:
        for multiple in range(num*num, n+1, num):
            is_prime[multiple] = False
# print(is_prime)  #debugging

print('\nSum of all the primes below 2 million:', sum(num for num, prime in enumerate(is_prime) if prime))
