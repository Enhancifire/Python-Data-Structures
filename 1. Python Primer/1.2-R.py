"""
Problem:
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

"""
Sol:
    Used Bitwise operators to check the last bit after using AND
    If last bit is 0, then arg is even, else odd
"""


def is_even(k):
    val = k & 1
    if val == 0:
        return True
    else:
        return False


print(is_even(10))
