# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson introduces generators and shows how and when they are used
# as opposed to functions.

# Generators produces items one at a time when required. They
# are a type of function that returns traversable items.


def new(dict):
    # Sets keys and values to x,y
    # respectively
    for x, y in dict.items():
        # Gives you x and y from dict
        # Yield = Return for generators
        yield x, y


# New dictionary
a = {1: "Hi", 2: "Welcome"}

# "b" is a new generator object
b = new(a)

# Prints the memory address
# of dictionary
print(b)

# Outputs the first pair of values in dictionary
print(next(b))

# Note: next(b) goes to next pair of values in dict but doesn't output anything

# Goes to next pair of values in dictionary
print(next(b))

# Can't go to next as there are no more items
# in the dictionary
print(next(b))
