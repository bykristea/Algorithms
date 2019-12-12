# def factorial(n): how do we think about this problem
# factorial 4! = 4 x 3 x 2 x 1 = 24

# what are the constraints?
# how large can n =?
# can it be negative?
# decimals?

# Expected Outputs?
# integer number

# Plan
# Recurssion?
# n! = (n)*(n-1)*(n-2)...
# base case
# if n <= 1
#     return 1
# return n* factorial(n-1)


def rec_factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= n1
    return result


print(rec_factorial(10))  # 3628800
print(rec_factorial(4))  # 24
# print(factorial(10000))  # error
