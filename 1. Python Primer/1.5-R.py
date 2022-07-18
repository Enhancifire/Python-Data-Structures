"""
Problem:
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""


def smol_squares(n):
    return sum([i**2 for i in range(n)])


print(smol_squares(3))
print(smol_squares(5))
print(smol_squares(7))
print(smol_squares(9))
