"Showcase pylint errors."
# Example Python file with intentional Pylint issues

from fruit import Fruit_Object
from fruit_types import Fruit


class ContactSpace:
    "Sends radio wave into space (this is a lie)"

    def __init__(self):
        self.space_mode = True
        self.space_request = "https://www.example.com"

    def space_radio(self, address, radio_band=None):
        print("Calling " + address)

    def turn_on(self):
        self.space_radio("https://www.example.com", "extra_argument")


class Snake:
    def __init__(self):
        self.size = 0

    def eat(self, fruit):
        print(f"Ate a fruit")
        print(fruit)

    def feast(self):
        self.eat(Fruit.DRAGON_FRUIT)


## More examples

HELLO_NAME = "Bob"


def say_hello(name):
    "Says hello!"
    # Missing docstring
    print(f"Hello, {name}")


# Unused variable
GRrETING = "Hello, World!"

# Function call with too many positional arguments
say_hello("Alice")
fruit_example = Fruit_Object(Fruit.BLACK_SAPOTE)
fruit_example.decompose()
