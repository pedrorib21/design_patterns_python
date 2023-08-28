# You should be able to substitute a base type for a subtype


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f"Width {self.width} Height {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


# BREAKING LISKOV SUBSTITUTION PRINCIPLE
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @width.setter
    def width(self, value):
        self._width = self._height = value

    @height.setter
    def height(self, value):
        self._width = self._height = value


# When you have an interface you should be able to stick in any of its inherits
# and everything should work
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)

    print(f"Expected {expected} got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
