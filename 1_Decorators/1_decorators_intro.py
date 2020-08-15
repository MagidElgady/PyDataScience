# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson introduces decorators and how they
# can modify a function without changing it permanently.


def function(function):
    # Decorator wraps function
    # inside another function
    def wrapper():
        print("Hello")
        # Places print statement from another
        # function between these 2 statements
        function()
        print("Welcome to Python Edureka Tutorial!")
    return wrapper

# Second Way
# Syntactic sugar; easier
# way of writing a decorator
@function
def function2():
    print("pythonista")


# First Way
# Decorator puts "pythonista"
# between the two print statements in the
# wrapper function
# function2 = function(function2)

function2()
