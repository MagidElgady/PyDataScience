# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to keep a track of
# states in a function using decorators. This is
# done with a singleton class.

# Required for wrapping
import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            # Gets state of cls function
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    # Resets wrapper instance
    wrapper.instance = None
    return wrapper


@singleton
# Empty class
class one:
    pass


# First = Second
first = one()
second = one()

# Outputs True as first = second
print(first is second)
