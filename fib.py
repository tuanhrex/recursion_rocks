# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1
from functools import lru_cache

@lru_cache(maxsize = 100)

def fib(n):
    fib_cache = {}
    if type(n) != int:
        raise TypeError('Value must be a positive integer')
    if n < 1:
        raise ValueError('Value must be a positive integer')
    pass
    if n in fib_cache:
        return fib_cache[n]

    # Compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)
    
    # cache the value and return it
    fib_cache[n] = value
    return value
# print(fib(-1))
# => 0
# print(fib(0))
# => 0
# print(fib(1))
# => 1
# print(fib(2))
# => 1
print(fib(30))
# => 13