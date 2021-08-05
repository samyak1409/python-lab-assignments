# Write a program to find the sum of all the primes below 2 million.


n = 2_000_000

# Sieve of Eratosthenes
prime = [True for i in range(n+1)]
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p*p, n+1, p):
            prime[i] = False
    p += 1

sum_ = 0
for p in range(2, n+1):
    if prime[p]:
        sum_ += p
print('\nSum of all the primes below 2 million:', sum_)


"""
# Naive
sum_ = 0
for i in range(2, n+1):
    for j in range(2, int(i**.5)+1):
        if i % j == 0:
            break
    else:
        sum_ += i
print('\nSum of all the primes below 2 million:', sum_)
"""
