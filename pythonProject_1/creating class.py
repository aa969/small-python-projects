class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# A function which is part of a class is referred to as method.
# Making a object from a class is know as instantiation, hence you work with instance of a class.
# In Python names that start with a capital letter refer to class
# variables that are accessible through instances like this are called attributes.

my_dog = Dog('James', 12)
your_dog = Dog('steve', 10)

print(f"My dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
print(my_dog.sit())

print(f"Your dogs name is {your_dog.name}")
print(f"Your dogs age is {your_dog.age}")
print(your_dog.sit())












