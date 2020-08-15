# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at fancy decorators and how they
# work such as decorating a class.


class Square:
    def __init__(self, side):
        self.side = side
    # Example of a decorator
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side ** 2

    @classmethod
    def unit_square(cls):
        return cls(1)


s = Square(0)
print(s.side)
print(s.area)
