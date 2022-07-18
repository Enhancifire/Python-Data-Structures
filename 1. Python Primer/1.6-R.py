"""
Problem:
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""


def smol_odd_squares(n):
    total = 0
    for i in range(1, n):
        if i % 2 == 0:
            pass
        else:
            total = total + i**2

    return total


print(smol_odd_squares(3))
print(smol_odd_squares(4))
print(smol_odd_squares(5))
print(smol_odd_squares(6))
print(smol_odd_squares(7))
print(smol_odd_squares(8))
print(smol_odd_squares(9))
