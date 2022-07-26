"""Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial."""
import sympy


class Polynomial:
    """Polynomial Class"""

    def __init__(self, poly) -> None:
        self.poly = poly

        self.polylist = poly.split()

        self.polynomial = []

        self.expression = ["+", "-"]

    def make_polynomial(self):

        for i in self.polylist:
            if "x" in i:
                x = i.index("x")
                print(i[0:x])

                if "^" in i:
                    print(i[i.index("^") + 1 :])
                else:
                    pass

            elif i in self.expression:
                "add"
                pass

            else:
                int(i)


Polynomial("23x^3 + 4").make_polynomial()
