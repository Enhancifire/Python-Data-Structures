"""
Problem:
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def smol_squares(n):

    total = 0

    for i in range(n):
        total = total + i**2

    return total


print(smol_squares(3))
print(smol_squares(5))
print(smol_squares(7))
print(smol_squares(9))
