from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Trying to instantiate Shape will raise an error
# s = Shape()  # This will raise TypeError

# Create a Rectangle object and compute area
r = Rectangle(10, 5)
print("Area of rectangle:", r.area())