# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lessons shows some examples of how a generator can be used.


# Function will increment i
# until i = 3 is reached
def myfunc(i):
    while i <= 3:
        yield i
        i += 1


# New generator object j
j = myfunc(2)

# Outputs 2
print(next(j))

# Outputs 3
print(next(j))

# Outputs "Stop Iteration" as i > 3
# print(next(j))


# You can only output 1 value
def ex():
    n = 3
    yield n
    n = n*n
    # Returns squared value of n
    yield n


# New generator object
v = ex()

print("First value is", next(v))

print("Second value is 3^2:", next(v))

# Outputs an error as
# function will only output 2 values
print(next(v))
