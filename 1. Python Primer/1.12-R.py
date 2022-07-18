"""
Problem:
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
"""

from random import choice


def randrange(start, stop=None):
    if not stop:
        stop = start
        start = 0

    return choice([i for i in range(start, stop)])


print(randrange(10))
print(randrange(10, 20))
print(randrange(3, 45))
