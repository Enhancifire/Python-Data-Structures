"""The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter constructor syntax should continue to produce an account with zero balance."""


class CreditCard:
    "A consumer credit card."

    def __init__(self, customer, bank, acnt, limit, balance=None) -> None:
        "Create a new credit card instance"

        if balance is None:
            balance = 0

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

        if price < 0:
            raise TypeError("Error: Parameter cannot be negative")

        if price + self._balance > self._limit:
            return False

        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        if amount < 0:
            raise TypeError("Error: Parameter cannot be negative")

        if isinstance(amount, int):
            self._balance -= amount

        else:
            raise TypeError("Error: Parameter is not a number")
