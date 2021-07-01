# By considering the terms in the Fibonacci sequence whose values do not exceed 4 million, write a program to find the
# sum of the even-valued terms.


a, b = 0, 1
fib_list = [a]
while a <= 4_000_000:
    a, b = b, a + b
    fib_list.append(a)
print()
# print(fib_list)

sum_ = 0
for num in fib_list:
    if num % 2 == 0:
        sum_ += num
print(sum_)
