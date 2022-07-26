"""R-2.6 If the parameter to the make payment method of the CreditCard class were a negative number, that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError if a negative value is sent."""


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
