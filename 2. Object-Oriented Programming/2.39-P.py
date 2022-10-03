"""
Develop an inheritance hierarchy based upon a Polygon class that has
abstract methods area() and perimeter(). Implement classes Triangle,
Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
class, with the obvious meanings for the area() and perimeter() methods.
Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan-
gle, and Square, that have the appropriate inheritance relationships. Fi-
nally, write a simple program that allows users to create polygons of the
various types and input their geometric dimensions, and the program then
outputs their area and perimeter. For extra effort, allow users to input
polygons by specifying their vertex coordinates and be able to test if two
"""

from abc import abstractmethod, ABCMeta
from math import sqrt


class Polygon(metaclass=ABCMeta):
    @abstractmethod
    def area(self) -> int:
        return 0

    @abstractmethod
    def perimeter(self) -> int:
        return 0


class Triangle(Polygon):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self):

        s = (self.a + self.b + self.c) / 2

        a = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return a

    def perimeter(self):

        return self.a + self.b + self.c


class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self) -> int:

        return self.a + self.b + self.c + self.d


class Pentagon(Polygon):
    def __init__(self, a, b, c, d, e) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def perimeter(self) -> int:

        return self.a + self.b + self.c + self.d + self.e


class Hexagon(Polygon):
    def __init__(self, a, b, c, d, e, f) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def perimeter(self) -> int:

        return self.a + self.b + self.c + self.d + self.e + self.f


class Octagon(Polygon):
    def __init__(self, a, b, c, d, e, f, g, h) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h

    def perimeter(self) -> int:

        return self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h


t = Triangle(3, 4, 5)

print(t.area())
print(t.perimeter())
