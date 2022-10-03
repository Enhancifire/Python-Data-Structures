"""
Write a Python program that inputs a document and then outputs a bar-chart plot
of the frequencies of each alphabet character that appears in that document
"""

import matplotlib.pyplot as plt
from collections import Counter


def read_file(file: str):
    with open(file, "r") as f:
        data = f.read()

        return data


def calc_frequency(data) -> dict[str, int]:

    output = Counter(data)
    data = dict(output)

    del data["\n"]

    return data


def barplot(data):
    chars = list(data.keys())
    frequency = list(data.values())
    plt.bar(range(len(data)), frequency, tick_label=chars)

    plt.show()


def main():
    data = read_file("test.txt")
    data = calc_frequency(data)
    barplot(data)


if __name__ == "__main__":
    main()
