"""
Problem:
Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""


def smol_odd_squares(n):

    return sum([(i**2 if i % 2 != 0 else 0) for i in range(1, n)])


print(smol_odd_squares(3))
print(smol_odd_squares(4))
print(smol_odd_squares(5))
print(smol_odd_squares(6))
print(smol_odd_squares(7))
print(smol_odd_squares(8))
print(smol_odd_squares(9))
