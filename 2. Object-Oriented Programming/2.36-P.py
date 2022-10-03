"""
Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).
"""
import random
import time
from pytermgui import tim


class Bear:
    "Bear Class"

    def __repr__(self) -> str:
        return f"[red bold]Bear[/bold /fg]"

    def ret_type(self):
        return "Bear"


class Fish:
    "Fish Class"

    def __repr__(self) -> str:
        return f"[green bold]Fish[/bold /fg]"

    def ret_type(self):
        return "Fish"


class Ecosystem:
    "Ecosystem class"

    def __init__(self) -> None:
        self.blocks = 20
        self.bears = 5
        self.fishes = 10
        self.array = self.create_array()

    def create_array(self):
        arr = []

        for _ in range(0, self.bears):
            arr.append(Bear())

        for _ in range(0, self.fishes):
            arr.append(Fish())

        for _ in range(self.fishes + self.bears, self.blocks):
            arr.append(None)

        random.shuffle(arr)

        return arr

    def rand_move(self):
        choice = random.choice(self.array)
        ind = self.array.index(choice)

        if choice is not None:
            mov = random.choice([-1, +1])
            if mov + ind > 0 and mov + ind < self.blocks:
                if choice.ret_type() == "Fish":
                    if self.array[mov + ind] is not None:
                        if self.array[mov + ind].ret_type() == "Fish":
                            val = self.populate()
                            self.array[val] = Fish()

                        elif self.array[mov + ind].ret_type() == "Bear":
                            self.array[ind] = None

                    else:
                        self.array[mov + ind], self.array[ind] = Fish(), None

                elif choice.ret_type() == "Bear":
                    if self.array[mov + ind] is not None:
                        if self.array[mov + ind].ret_type() == "Bear":
                            val = self.populate()
                            self.array[val] = Bear()

                        elif self.array[mov + ind].ret_type() == "Fish":
                            self.array[ind + mov], self.array[ind] = (
                                self.array[ind],
                                None,
                            )

                    else:
                        self.array[mov + ind], self.array[ind] = Bear(), None

    def populate(self):
        arr = []

        for i, val in enumerate(self.array):
            if val is None:
                arr.append(i)

        return random.choice(arr)

    def play(self):
        for _ in range(40):
            tim.print(self.array)
            self.rand_move()
            time.sleep(0.1)

        self.calc_population()

    def calc_population(self):
        bears = 0
        fishes = 0
        for i in self.array:
            if i is None:
                pass
            elif isinstance(i, Bear):
                bears += 1
            elif isinstance(i, Fish):
                fishes += 1

        print("Population:")
        print(f"Initial Fishes: {self.fishes}")
        print(f"Initial Bears: {self.bears}")
        print(f"Current Fishes: {fishes}")
        print(f"Current Bears: {bears}")


Ecosystem().play()
