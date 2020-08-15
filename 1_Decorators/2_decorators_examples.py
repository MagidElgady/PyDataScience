# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at examples of decorators.


def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args, **kwargs)
        print("Welcome to Edureka Python Tutorial")
    return wrapper


@function1
def function2(name):
    print(f"{name}")


function2("Waseem")


def function1(function):
    def wrapper(*args, **kwargs):
        print("Returning a function from a decorator worked!")
    return wrapper


@function1
def function2(name):
    print(f"{name}")


function2("python")
