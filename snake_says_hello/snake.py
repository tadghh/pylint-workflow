"Showcase pylint errors."
# Example Python file with intentional Pylint issues

HELLO_NAME = "Bob"


def say_hello(name):
    "Says hello!"
    # Missing docstring
    print(f"Hello, {name}")


# Unused variable
GRrETING = "Hello, World!"

# Undefined variableaa
print(GREETING)

# Function call with too many positional argumentsadd
say_hello("Alice")


class ContactSpace:
    "Sends radio wave into space (this is a lie)"

    def __init__(self):
        self.space_mode = True
        self.space_request = "https://www.example.com"

    def space_radio(self, address, radio_band=None):
        print("Calling " + address)

    def turn_on(self):
        self.space_radio("https://www.example.com", "extra_argument")
