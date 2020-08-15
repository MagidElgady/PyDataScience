# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lessons introduces loops with generators.


def ex():
    n = 3
    yield n
    n = n * n
    yield n


v = ex()

# Allows us to print all values
# in a function at once with
# generators
for x in v:
    print(x)
