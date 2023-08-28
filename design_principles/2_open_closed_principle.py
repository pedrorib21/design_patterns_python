from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


# OCP = open for extension, closed for modification
# After you have writen a class you should extend it and not modify it

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color : yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # THIS SOLUTION DOES NOT SCALE
    # LETS SAY WE ALSO HAVE WEIGHT WE WOULD NEED A LOT OF METHODS



# BETTER SOLUTION

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self,*args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green (old)")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f"{p.name} is green")



    # BETER SOLUTION

    bf = BetterFilter()

    print("Green (new)")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f"{p.name} is green")

    print("LARGE PRODUCTS")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f"{p.name} is large")

    print("Large Blue Products")
    large_blue = AndSpecification(large,
                                  ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f"{p.name} is large and blue")


    # Overloading the and operation of the Specification Base Class
    large_blue = large and ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f"{p.name} is large and blue")