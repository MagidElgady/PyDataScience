# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to nest decorators.

import functools


# Repeats name string n number of times
def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Runs for loop 5 times if
            # num = 5
            for i in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat


# Prints name 5 times
@repeat(num=5)
def function(name):
    print(f"{name}")


function("python")
