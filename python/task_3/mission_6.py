import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [
    Circle(5),
    Square(4),
    Circle(2),
    Square(10),
]

for shape in shapes:
    print(f"Площа фігури: {shape.area():.2f}")
