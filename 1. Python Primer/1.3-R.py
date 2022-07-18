"""
Problem:
    R-1.3 Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
"""


def minmax(data):
    mini = -1
    maxi = 0

    for item in data:
        if mini == -1:
            mini = item
        elif mini > item:
            mini = item

        if maxi < item:
            maxi = item

    return (mini, maxi)


print(minmax([10, 20, 2, 5, 13, 12]))
