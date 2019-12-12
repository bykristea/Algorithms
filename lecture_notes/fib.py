# import function tools from least-recently-used cache
from functools import lru_cache

# cache is the store
cache = {}


def fib(n):
    # check if n in cache. first check if we computed this in fib(n)
    if n in cache.keys():
        return cache[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_result = fib(n-1) + fib(n-2)
# store the result in cache
    cache[n] = fib_result

    return fib_result


@lru_cache(maxsize=500)
def lru_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))
print(lru_fib(500))


# Dynamic Programming: computing the output of a function once and storing it to use later
# memoization
