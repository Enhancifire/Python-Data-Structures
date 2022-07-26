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


class Animal:
    def __init__(self, x):
        self.x = x

    def rand_move(self):
        movement = random.choice([-1, 1])
        return self.x + movement

    def move(self, x):
        self.x = x


class Bear(Animal):
    def __init__(self, x):
        super().__init__(x)

    def __repr__(self) -> str:
        return f"Bear at {self.x}"

    def ret_type(self):
        return "Bear"


class Fish(Animal):
    def __init__(self, x):
        super().__init__(x)

    def __repr__(self) -> str:
        return f"Fish at {self.x}"

    def ret_type(self):
        return "Fish"


class Array:
    def __init__(self) -> None:
        self.blocks = 20
        self.bears = 2
        self.fishes = 5
        self.array = self.create_array()

        self.play()

    def create_array(self):
        arr = []

        def create_bear(i):
            if self.bears != 0:
                self.bears = self.bears - 1
                return Bear(i)

        def create_fish(i):
            if self.fishes != 0:
                self.fishes = self.fishes - 1
                return Fish(i)

        def return_none(i):
            return None

        for i in range(self.blocks):
            fun = random.choice([create_bear, create_fish, return_none])
            arr.append(fun(i))

        return arr

    def rand_move(self):
        choice = random.choice(self.array)
        ind = self.array.index(choice)
        if choice is not None:
            x = choice.rand_move()
            if x < 0 or x > self.blocks - 1:
                pass

            else:
                if choice.ret_type() == "Fish":
                    if self.array[x].ret_type == "Bear":
                        self.array[choice] = None

                    elif self.array[x].ret_type == "Fish":
                        val = self.populate()
                        self.array[val] = Fish(val)
                        self.array[ind] = None

                    else:
                        choice.move(x)
                        self.array[ind] = None
                        self.array[x] = choice

                if choice.ret_type() == "Bear":
                    if self.array[x].ret_type() == "Fish":
                        self.array[x] = choice
                        self.array[ind] = None
                        choice.move(x)

                    if self.array[x].ret_type() == "Bear":
                        val = self.populate()
                        self.array[val] = Bear(val)
                        self.array[ind] = None

                    else:
                        choice.move(x)
                        self.array[ind] = None
                        self.array[x] = choice

    def populate(self):
        arr = []

        for i, val in enumerate(self.array):
            if val is None:
                arr.append(i)

        return random.choice(arr)

    def play(self):
        for _ in range(40):
            print(self.array)
            self.rand_move()
            time.sleep(0.1)


Array()
