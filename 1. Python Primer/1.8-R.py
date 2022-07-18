"""
Problem:
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""


def get_index(n, k):
    return n + k


st = "ABCDEF"

k = -3
print(st[k])
print(st[get_index(len(st), k)])
