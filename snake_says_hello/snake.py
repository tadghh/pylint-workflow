# Example Python file with intentional Pylint issues


def say_hello(name):
    # Missing docstring
    print(f"Hello, {name}")


# Unused variable
greeting = "Hello, World!"

# Undefined variable
print(greet)

# Function call with too many positional arguments
say_hello("Alice", "Bob")

# Function call with too few positional arguments
say_hello()


# Unused parameter
def unused_param_example(param1, param2):
    print(param1)


# Variable redefined
number = 42
number = "forty-two"


# Function call with too many positional arguments
make_request("https://www.example.com", "extra_argument")

# Function call with too few positional arguments
make_request()  # Missing required argument
