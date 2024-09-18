import math


class Validatable(type):
    def __new__(cls, name, bases, attrs):
        if 'validate' not in attrs:
            raise TypeError(f"Class {name} must define a 'validate' method")
        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.validate()
        return instance


class Shape(metaclass=Validatable):
    def validate(self):
        raise NotImplementedError("Subclass must implement 'validate' method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def validate(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")


# Example usage
try:
    rect = Rectangle(-1, 2)
except ValueError as e:
    print(e)  # Output: Width and height must be positive

try:
    circle = Circle(0)
except ValueError as e:
    print(e)  # Output: Radius must be positive

rect = Rectangle(1, 2)
circle = Circle(1)

try:
    class BadShape(Shape):
        pass
except Exception as e:
    print(str(e))
