"""Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class to ensure that the caller sends a number as a parameter."""


class CreditCard:
    "A consumer credit card."

    def __init__(self, customer, bank, acnt, limit) -> None:
        "Create a new credit card instance"

        self._customer = customer
        self._bank = bank
        self._accound = acnt
        self._limit = limit
        self._balance = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit"""
        if isinstance(price, int):
            pass
        else:
            raise TypeError("Error: Parameter is not a number")

        if price + self._balance > self._limit:
            return False

        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        if isinstance(amount, int):
            self._balance -= amount

        else:
            raise TypeError("Error: Parameter is not a number")
