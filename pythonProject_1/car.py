"""A class that can be used to represent a car."""
class Car:
    """Simply Instruction's to design a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

    def read_odometer(self):
        """Print the mileage on the odometer"""
        print(f"This car has {self.odometer_reading} miles on it")

    def up_date_odometer(self, mileage):
        """
        Set the odometer reading to the given value. Reject the change if
        it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
