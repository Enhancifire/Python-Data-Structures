"""Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the name of the flower, its num- ber of petals, and its price. Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type."""


class Flower:
    def __init__(self, name, petals, price) -> None:
        self.name: str = name
        self.petals: int = petals
        self.price: float = price

    def set_values(self, name=None, petals=None, price=None):
        "Sets value using keyword arguements"
        if name is not None:
            self.name = name

        if petals is not None:
            self.petals = petals

        if price is not None:
            self.price = price

    def get_vals(self):
        "Returns values of attributes"
        return (self.name, self.petals, self.price)
